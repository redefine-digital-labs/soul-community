# Independent read-only Community source cutover v2 review

SCOPED_PASS. No actionable finding in the frozen source-only cutover scope. This review is independent of the coordinator prerequisite receipt and is not human source activation authorization, qualified external audit, remote CI acceptance, chain acceptance or full-goal completion.

## Exact candidate

- Frozen manifest: `92e3426aed0648b8274954e79d7528c5198065011d7beb5c20b9f730140a3cef` (446 files).
- Operations: `7e19ed3274b74f070222bc7d38dded6e7725019a92c18987f3229beff716230c` (194 exact operations; 30 protected paths).
- Control: `704e2f7919a085270666678cc90ce1c6a2e0f9bdb47e46bb8a13edf903841b65`.
- Terminal evidence: `5d17feeff9c13fd789c5bd5a568b18f1ad2ddf1762c1802c4c69fd6db0e85abe` (123 receipts).
- Owning target: `/Users/naoer/Documents/Claude/Projects/soulidity-ecosystem/soul-community`.

## Verified evidence and code

Read ACT AGENTS.md, PROJECT_MEMORY, CURRENT and its sole handoff; candidate SPEC/REPORT/APPROVAL, operations, frozen/control/semantic runners, raw semantic logs, all 53 CAS probe logs, approvals, journals and backups. Applied handbook1.0 sections1–5,7,8.3–8.4,9,12 and Operating Model8; reviewed an attachment to original DOF-001/P01/P09, without creating a task board or changing Owners.

Recomputed all 446 frozen file SHA/mode/size states and all 123 terminal states. Independently compared every actual target operation to before-state and all 30 protected files to exact expected bytes/modes. Ran the original frozen control's read-only `check` with the exact manifest pin: BASELINE_PASS, zero drift. No actual approval exists; actual source activation remains false at review.

The code binds approval schema, approved flag, scope, exact target, manifest, operations, control and command; actual activation additionally requires the human authorization flag. The journal binds the exact approval file SHA and the same transaction identity. Rehearsal authorization cannot authorize actual writes. Target/path confinement, reserved Git/control operation paths, ancestor symlinks, file hardlinks, target aliases, frozen input drift and concurrent flock are refused. Fault injection and seed are restricted to isolated rehearsals.

Before first source mutation the control checks the entire before baseline and every protected file, records a preparing journal, materializes independently copied before blobs, checks all blobs, and transitions to applying. On recovery, every operation is checked as exact before/after and every required backup is revalidated before source changes. Each source mutation repeats protected/CAS checks, uses atomic replacement or deletion with readback, and saves the atomic fsynced journal. Rollback restores original bytes/modes and deletes originally absent files. Recovery accepts the precise after-write/before-journal outcome and repeats safely; unknown bytes or corrupt/missing backups refuse. Completed apply/resume and rollback are idempotent; restored journals refuse reapply.

Reviewed the actual recorded 53 invocations, including intended refusal diagnostics and hard exits73/74. Independently checked all194 before-state operations and30 protected states after normal, after-write interruption/resume/rollback, after-journal interruption/recovery and lock-release recovery. All four terminal journals are restored with all194 rollback indices; three before blobs per transaction are SHA-exact, mode0444, single-link and different inodes from actual and recovered source. The probes did real file writes in isolated outputs, not simulated success. No attack fixtures, replacement executable or repeated mutation runs were created in this review.

The unchanged semantic runner verifies exact198 input closure (187 framework files plus11 Community manifests/source/tests), rejects non-local/outside dependencies, copies to a fresh source tree with empty HOME, and runs pinned Sui1.80.1 under network denial with unchanged default budgets. The registered CI log and frozen raw build/test/network/version logs support fresh production build plus the original106/106 tests. Exactly three contained packages are present: MoveStdlib, Sui, SoulidityCommunity. No project/Standard/sibling dependency is needed. All four compiled module bytes match the immutable P5 preparation snapshot SHA395ce5bcbc4d6a333c8ab7c4e30b48d62b82b7db9fd234b776181923d5f310ce. P5 live state advanced during review; immutable preparation evidence was used, not a stale pending-state assumption.

All nine original production source/test files match actual owning source, candidate and P5 source exactly. The hosted maintenance workflow remains SHA0c8d128d5f4a7b616716a7bb8f4e52d33dfe083eea0dcf206c59d472a512b659. Module management, agent contract, engineering permissions, write boundary and release readiness match actual unchanged. v1 manifest20ae322d and all452 entries are preserved; whole-plan source guard SHA26a3654ccc07581df2c301e82363a1e17db09987dd9f3835236ec8ff46e3f99f is unchanged.

## Limits and remaining gates

PASS covers reviewed local source/build and process interruption recovery with exact frozen evidence. It does not claim whole-filesystem transactions, power-loss testing, resistance to privileged concurrent filesystem tampering, or cryptographic authenticity of a self-written approval JSON; Root must supply approval from the independently reviewed candidate and existing human authorization. Preserved generated empty directories and .cas recovery evidence are intentional.

Remote semantic CI is unfinished; unchanged hosted maintenance CI is not semantic acceptance. Source activation/owning backup, Gate0/effective authority/old callable rejection/type migration, complete chain/publication requirements, qualified independent acceptance/release, original SDK/UI/recovery and full157/30 acceptance remain separate unfinished requirements. The coordinator reported the first retained isolated Community publication completed under its separate publication review; this source review neither re-approves it nor implies further signatures/publications. Full157/30 remains ACTIVE; Owners and original DOF-001/P01/P09 remain unchanged.

Review wrote only this review directory. Candidate, owning/source repositories, Git, keys and network were not modified.
