# Community publication/recovery candidate v5 independent review

SCOPED_PASS for the exact first Community candidate and execution/recovery controls bound below. No blocking findings remain in this bounded review. This is an independent internal AI review of source controls and public evidence; it is not an execution approval, qualified external audit, actual publication proof or full-product acceptance.

## Corrected findings

- V4-R1 passes: `submit_exact.mjs` lines 25–37 enforce signer/review/frozen-candidate/control identity, CLI SHA equality with approved state, and every reviewed state/digest/intent binding. Lines 66–83 enforce actual state SHA, pending digest/intent, Community allowlist and actual intent SHA before reservation/key access. A different intent or state requires a new bound review. The existing six benign mismatch logs and positive assertion fixture were independently inspected; no approval was created.
- V4-R2 passes: `driver.py` lines 34–42 validate the signed record even when lifecycle exists. Line 90 reports reserved-plus-signed-record as effectively signed, while any lifecycle or record blocks new signing. Eight independently evaluated pure JSON cases cover reservation alone, simultaneous record, signed lifecycle, submission started, record-only recovery, mismatched digest, absent digest and invalid JSON. Malformed/mismatched records fail closed.

## Independently verified evidence

- Frozen manifest SHA and all 1,703 preparation plus 26 execution file SHA/lengths match. All reviewed candidate/source/runtime inputs are regular files/directories. The 1,681 source input hashes equal the accepted Maker manifest `ae46753969065c00edc443888eef11fb82a8333ab44eb68adc599baee1d85a39` exactly, with zero current source deltas. `baseline.json.source_delta_count:3` is retained historical preparation metadata; it is not the current comparison result.
- The 14 guarded controls match their pins. The runtime Node executable and all 20 SDK roots/1,825 files match exact inventories. Static signer ordering places inventory checks before SDK dynamic imports. Independent transaction inspection also checked runtime inventories before importing SDK code.
- Read-only `driver.gate()` passes actual source/runtime/tool, chain/protocol, external-package and protected-original Soul/Config/Admin checks. Driver main/lock/preflight writers and signer were not invoked.
- Community is first in the dependency order, has no project dependencies, and owns exactly `community_posts`, `community_votes`, `profile`, `social`. Both predecessor compiler artifacts equal pending publication artifacts exactly. The unsigned 13,148-byte BCS data reconstructs the exact two-command publish/UpgradeCap transfer kind, sender, single gas reference, 5,000,000,000 budget and digest. Dependencies are only 0x1/0x2. Live public reads confirm chain ae60751d/protocol137, current gas reference, successful dry run and original digest NOT_FOUND at review time.
- Signing reserves `SIGNING_INTENT_RESERVED` with exclusive `wx`, file fsync and directory fsync before any custody-file read or signing (signer lines 110–124). Signed recovery is saved exclusively and durably before submission-start status and the single submit call. Existing lifecycle/record presence blocks new signing; interruption after reservation or unknown transport outcome directs original-digest readback. This review validates code ordering, not a signer run or concurrent live signing experiment.
- Historical successful effects without optional objectChanges independently reconcile six created objects, one exact immutable package reference and four live shared registry types/custody. This proves the scoped reconciliation path, not this unpublished candidate's effects or historical mutable initial contents. Driver recovery still requires exact raw transaction bytes, relocated modules, type origins, linkage, UpgradeCap and init custody before advancing state. Failure/unknown/ambiguous results preserve pending state, and recovery has no submit path.
- A normalized v4→v5 source comparison confirms only exact binding enforcement and simultaneous lifecycle/record projection changed in the signer/driver; earlier mandatory guard/recovery code remains intact. No actual coordinator approval, lifecycle or signed record exists for this candidate. State and frozen candidate inputs were rechecked unchanged at completion.

## Existing delivery record attachment and boundaries

Attach this evidence to existing DOF-001/P01/P09; original Owners and backlog remain unchanged. Current stage: Test / Release evidence. Task status and full reconstruction goal remain in progress. Handbook 1.0 sections 1–5, 7, 8.3–8.4, 9, 10 and 12 plus operating-model section 8 apply. The acceptance exit here is exact candidate review, not Deploy/Operate/Monitor completion.

Payment/model/EVM checks are not applicable to this bounded isolated publication-control review. Effective on-chain governance, actual retained key custody and signer selection, initialized candidate objects, old callable rejection, type/source migration and product business journeys remain pending with the authorized executor and existing Owners. No multisig, timelock or business-policy immutability is asserted. Public object readback is distinct from custody-file access.

Only first `soulidity_community` execution is covered. Every other publication/dependency release, the eventual 19-root/74-module graph, Standard-dependent activation/publication and full157-responsibility/30-duty acceptance are outside this pass. Root must separately create the exact review-hash-pinned Community-only execution approval under existing human authorization and retain all mandatory preflight/recovery gates. Recheck gas/state before signing; after interruption, recover the original digest rather than replacing/replaying the intent. Actual publication, source activation, migration, UI/SDK integration, independent CI/releases and full-goal acceptance remain unfinished.

No custody file was read or hashed, no keys/signatures/submissions, no approval, source/runtime/SDK/Git/DB/standard mutation, no process/network restart, no production or remote mutation. All writes are review artifacts in this directory; public RPC reads/dry runs only. No replacement executable fixture or exploit was generated.

## Exact reviewed bindings

- `frozen_candidate_sha256`: `35e9ca4355919f86d2c1fa85cf17d28063b1081b43e52669594e8446a0b088a7`
- `signer_sha256`: `7574b4bc17160d7eaa58f7490a4bc14e3ccf6e57808b28a05799c392440d6f26`
- `preparation_controls_sha256`: `99720c963e3528bd33019c1da5cc92f3f6b07cc64196ceb38aec8130680bea27`
- `state_sha256`: `395ce5bcbc4d6a333c8ab7c4e30b48d62b82b7db9fd234b776181923d5f310ce`
- `digest`: `EqefAQPJodhGbfyaCisqWPSAKKqfYooowCmrXUiXUean`
- `intent_sha256`: `c4f84c556f800c1bf67a6c06c22385223423627a1ae8fdacd053d9ece03c4fb4`
- `allowed_folders`: `["soulidity_community"]`
