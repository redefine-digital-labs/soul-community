#!/usr/bin/env python3
"""Verify pinned Community from a fresh offline copy using its original VM tests."""
import hashlib, json, os, platform, re, shutil, subprocess, sys, tempfile
from pathlib import Path
SUI_SHA256='1d7baa7c7314113671415acfa20279b1eedb6ae6d04f286988a00da285e769c3'
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def require(condition,message):
 if not condition:raise ValueError(message)
def inventory(root):
 return {str(p.relative_to(root)):sha(p) for folder in ['move','.deps'] for p in (root/folder).rglob('*') if p.is_file() and 'build' not in p.parts}
def main():
 sui=Path(os.environ.get('SUI_BINARY','')).resolve()
 require(sui.is_file() and not sui.is_symlink() and sha(sui)==SUI_SHA256,'SUI_BINARY must be pinned Sui v1.80.1')
 pins=json.loads((ROOT/'source-candidate-pins.json').read_text())
 require(not pins['project_dependencies'],'Community cannot consume business or Standard packages')
 require(inventory(ROOT)==pins['inputs'],'source/dependency inventory or hash drift')
 require(not any(p.is_symlink() for p in ROOT.rglob('*')),'repository symlinks refused')
 output=ROOT/'output';output.mkdir(exist_ok=True)
 run=Path(tempfile.mkdtemp(prefix='community-independent-',dir=output))
 source=run/'source';source.mkdir()
 for folder in ['move','.deps']:shutil.copytree(ROOT/folder,source/folder)
 for p in source.rglob('*'):
  if p.is_file():p.chmod(0o644)
 # Every declared dependency resolves inside this fresh input closure, without Git or siblings.
 closure=[]
 for manifest in source.rglob('Move.toml'):
  text=manifest.read_text();name=re.search(r'^name\s*=\s*"([^"]+)"',text,re.M)
  require(name is not None,'package name missing');closure.append(name[1])
  section=re.search(r'(?ms)^\[dependencies\]\s*\n(.*?)(?=^\[|\Z)',text)
  for line in section[1].splitlines() if section else []:
   if not line.strip() or line.lstrip().startswith('#'):continue
   dep=re.fullmatch(r'\s*\w+\s*=\s*\{\s*local\s*=\s*"([^"]+)"\s*(?:,\s*override\s*=\s*true)?\s*\}\s*',line)
   require(dep is not None,'only exact local dependencies permitted')
   local=Path(dep[1]);require(not local.is_absolute(),'absolute build dependency refused')
   target=(manifest.parent/local).resolve()
   require(target.is_relative_to(source) and (target/'Move.toml').is_file(),'dependency escapes independent source closure')
 require(sorted(closure)==['MoveStdlib','SoulidityCommunity','Sui'],'unexpected package in closure')
 home=run/'home';home.mkdir()
 env=os.environ.copy();env.update(HOME=str(home),MOVE_HOME=str(home/'.move'),XDG_CONFIG_HOME=str(home/'.config'),TMPDIR=str(run))
 if platform.system()=='Darwin':prefix=['/usr/bin/sandbox-exec','-p','(version 1)(allow default)(deny network*)']
 elif platform.system()=='Linux':prefix=['unshare','--net','--']
 else:raise ValueError('no supported enforced offline sandbox on this platform')
 def execute(name,argv):
  cmd=prefix+argv
  result=subprocess.run(cmd,cwd=source,env=env,capture_output=True,timeout=300)
  log=run/(name+'.log');log.write_bytes(result.stdout+result.stderr)
  row={'argv':cmd,'exit_code':result.returncode,'log':str(log.relative_to(ROOT)),'log_sha256':sha(log)}
  return row,result.stdout+result.stderr
 version,out=execute('version',[str(sui),'--version']);require(version['exit_code']==0 and b'1.80.1-671ba71e69c7' in out,'Sui version mismatch')
 # A direct socket attempt under the same policy must be refused.
 network_probe,out=execute('network-denial',[sys.executable,'-c','import socket; socket.create_connection(("127.0.0.1", 9), timeout=1)'])
 require(network_probe['exit_code']!=0 and (b'Operation not permitted' in out or b'Network is unreachable' in out),'network denial was not demonstrated')
 package=source/'move/soulidity_community'
 build,_=execute('production',[str(sui),'move','build','--path',str(package),'--install-dir',str(run/'production')])
 test=None;summary=None;artifacts={}
 if build['exit_code']==0:
  test,out=execute('tests',[str(sui),'move','test','--path',str(package),'--install-dir',str(run/'test')])
  match=re.search(rb'Test result: (\w+)\. Total tests: (\d+); passed: (\d+); failed: (\d+)',out)
  if match:summary={'result':match[1].decode(),'total':int(match[2]),'passed':int(match[3]),'failed':int(match[4])}
  for p in (run/'production/build/SoulidityCommunity/bytecode_modules').glob('*.mv'):artifacts[p.stem]=sha(p)
 after=inventory(source);before=pins['inputs'];stable={k:v for k,v in before.items() if not k.endswith('Move.lock')}=={k:v for k,v in after.items() if not k.endswith('Move.lock')}
 ok=build['exit_code']==0 and test and test['exit_code']==0 and summary=={'result':'OK','total':pins['expected_tests'],'passed':pins['expected_tests'],'failed':0} and sorted(artifacts)==sorted(pins['owned_modules']) and artifacts==pins['production_artifacts'] and stable
 report={'result':'PASS' if ok else 'FAIL','source_pins_sha256':sha(ROOT/'source-candidate-pins.json'),'sui_sha256':sha(sui),'sui_version':version,'python':{'version':sys.version,'executable':sys.executable,'sha256':sha(Path(sys.executable))},'platform':platform.platform(),'network_policy':prefix,'network_denial_probe':network_probe,'fresh_source':str(source.relative_to(ROOT)),'empty_HOME':str(home.relative_to(ROOT)),'packages':sorted(closure),'project_dependencies':[],'build':build,'test':test,'summary':summary,'production_artifacts':artifacts,'inputs_before':before,'inputs_after':after,'source_and_manifest_unchanged':stable,'lock_mutations':[k for k in sorted(set(before)|set(after)) if before.get(k)!=after.get(k)],'budget':'unchanged Sui default; no gas-limit or package-size override','scope':'Local production compile and original VM regressions; no source activation, release, type-origin compatibility, chain publication, UI acceptance or audit','transactions':0,'remote_ci':False}
 evidence=run/'evidence.json';evidence.write_text(json.dumps(report,sort_keys=True,indent=2)+'\n')
 print(json.dumps({'result':report['result'],'summary':summary,'evidence':str(evidence.relative_to(ROOT))}))
 return 0 if ok else 1
if __name__=='__main__':
 try:raise SystemExit(main())
 except (ValueError,OSError,KeyError,subprocess.TimeoutExpired) as error:
  print('Community independent verification failed: '+str(error),file=sys.stderr);raise SystemExit(1)
