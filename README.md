# KarmenLoop Memory Ledger

**Reconcile scoped memory records while exposing conflicts and expiry.**

Built by **[KarmenLoop](https://github.com/KarmenLoop)**. Reconcile scoped memory records while exposing conflicts and expiry.

[![Release](https://img.shields.io/github/v/release/KarmenLoop/skill-memory-ledger)](https://github.com/KarmenLoop/skill-memory-ledger/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](docs/INPUT.md)
[![Platform](https://img.shields.io/badge/Platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey.svg)](docs/COMPATIBILITY.md)

[Download](https://github.com/KarmenLoop/skill-memory-ledger/releases) · [Quick start](#quick-start) · [Documentation](#documentation) · [Contribute](CONTRIBUTING.md) · [Contact](https://github.com/KarmenLoop/skill-memory-ledger/issues) · English

**License:** MIT. Free to use, modify, redistribute, and use commercially with the required copyright and license notice. The included local helper needs no subscription or provider API key.

## Introduction

Use an explicit memory scope and source-linked observations. Record only information the user wants retained. Credentials and execution permissions do not belong in memory records. Records are grouped by scope and key, then ordered by explicit observation time. Equal-time disagreement remains a conflict; expiry and tombstones suppress recall.

This repository ships one independently installable agent skill, an original deterministic helper, example input, and executable tests. A capable agent handles interpretation and tool selection; the helper performs the repeatable work described below.

## Capabilities

- Select current observations within an explicit scope.
- Honor expiry and deletion records.
- Surface equal-time conflicts instead of silently choosing a value.

## Quick start

Requirements: Python 3.9+. Git is needed only for cloning; downloading the release archive also works. On Windows, replace python3 with py -3 if that is your installed launcher.

```sh
git clone https://github.com/KarmenLoop/skill-memory-ledger.git
cd skill-memory-ledger
python3 scripts/run.py --input examples/input.json
python3 -m unittest discover -s tests -v
```

The helper returns a structured result. Compare it with [examples/expected.json](examples/expected.json). Read the [field contract](docs/INPUT.md) before supplying your own data. Any documented relative file paths resolve from the process working directory.

To save a result without overwriting an existing file:

```sh
python3 scripts/run.py --input examples/input.json --output result.json
```

### Install the agent skill

Choose one host:

```sh
python3 install.py --host codex
# Alternatives: --host deepseek, --host grok, or --host agents
```

The installer copies this skill into the selected user's skill directory and refuses an existing destination. It does not change host settings, permissions, credentials, or other skills. Use --destination with an exact new directory for a custom installation.

In Codex, invoke $karmen-memory-ledger. In Grok Build, invoke /karmen-memory-ledger. In another compatible host, select the installed skill by name. Example request:

> Reconcile these project memories and show any conflicts.

Refresh your host's skill discovery if needed. See [compatibility and its verification limits](docs/COMPATIBILITY.md).

## How it works

Records are grouped by scope and key, then ordered by explicit observation time. Equal-time disagreement remains a conflict; expiry and tombstones suppress recall.

JSON results can be inspected, archived, or passed to another tool. The helper never interprets input as a shell command. Exit code 0 means processing completed; findings may still require action. Exit code 2 means invalid input or a filesystem error. Existing output files are preserved.

## Documentation

- [Agent instructions](SKILL.md): selection, workflow, and completion criteria.
- [Input and output](docs/INPUT.md): fields and complete example.
- [Compatibility](docs/COMPATIBILITY.md): installation targets and host limits.
- [Validation](docs/VALIDATION.md): observed local results and acceptance scenarios.
- [Sources](docs/SOURCES.md): public research references and design decisions.
- [Changelog](CHANGELOG.md): release history.

## Limitations

The helper reconciles a supplied ledger; it does not automatically save personal data, synchronize devices, or grant access between users. Secret-key screening is a small denylist, not a complete secret scanner.

Examples are synthetic. Local tests establish the covered helper behavior; they do not establish an authenticated provider integration or the quality of every future model response. Tools and account access remain those of the host.

## Contributing

Bug reports, focused improvements, documentation fixes, and pull requests are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md), include a sanitized reproduction, and run the tests. Development needs no third-party runtime dependency.

## Support

Use [GitHub Issues](https://github.com/KarmenLoop/skill-memory-ledger/issues) for bugs and feature requests. [SUPPORT.md](SUPPORT.md) explains what to include. Never attach keys, customer records, or private conversations.

## License

Copyright © 2026 KarmenLoop. [MIT](LICENSE) permits commercial use and secondary development under its terms. Third-party services retain their own terms; see [NOTICE.md](NOTICE.md).

## Acknowledgements

This is an independent KarmenLoop implementation. [Research notes](docs/SOURCES.md) identify public design references from the Meta, DeepSeek, and xAI ecosystems as applicable. No upstream code or brand assets are bundled, and no affiliation or endorsement is claimed.

## Contact

[KarmenLoop](https://github.com/KarmenLoop) · [Issues](https://github.com/KarmenLoop/skill-memory-ledger/issues) · [Security reporting](SECURITY.md)
