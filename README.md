# soul-community

COMMUNITY: independent basic community. Profiles, posts/comments, relationships and pagination.

Maintenance entry points: [MODULE](MODULE.md), [Agent boundaries](AGENTS.md), [compatibility](COMPATIBILITY.md), [operation and recovery](RUNBOOK.md). Machine configuration: [module.json](module.json).

Actual construction: Community production source and authority over 5 original test files have moved here; independent production build, 106/106 VM tests and local product CI pass. See module.json for detailed evidence statuses; independent deployment and remote CI remain unaccepted.
Recommended role CIPHER/LUQI/SABLE; original Owner unchanged. Unconfirmed actual maintainer and independent acceptor mappings remain pending; role names are not accounts or audit qualifications.

```sh
python3 scripts/ci.py
python3 scripts/ci.py --product
python3 scripts/ci.py --release-ready
```

Default CI checks the maintenance contract; `--product` refuses to pass when no product command is registered. Readiness gates do not deploy or sign.

[Original community regression migration evidence](evidence/community-test-migration.json). Tests change only module namespaces; original assertions and production implementations are unchanged. The five originals remain as historical backups.

## Current checkpoint

See [construction status](CONSTRUCTION_STATUS.md) for current evidence, blockers, recovery material and remote coordination. This checkpoint is not a release.
