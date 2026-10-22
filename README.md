# Memory Ledger

English | [简体中文](README.zh-CN.md)

Resolve a set of saved facts at a particular time and scope. Corrections, conflicts, expiry, and deletion stay visible, so an agent can distinguish a current preference from an old observation.

[Download v0.2.1](https://github.com/KarmenLoop/skill-memory-ledger/releases/tag/v0.2.1) · [Tutorial](docs/tutorial.en.md) · [Input reference](docs/INPUT.md) · [Report an issue](https://github.com/KarmenLoop/skill-memory-ledger/issues)

## What it does

For project:demo, the later correction selects CSV as report_format and retains its source and timestamp.

The ledger evaluates supplied observations. It is not a database service, model training system, or automatic cross-device memory sync.

![Memory Ledger sample JSON output from version 0.2.1](docs/images/example-output-v0.2.1.svg)

*Actual local output from v0.2.1, rendered as an image. [Complete result](examples/expected.json) · [Image provenance](docs/images/provenance.json).*

## Start here

Download `karmen-memory-ledger-v0.2.1.zip` and its `.sha256` file from the release, verify the hash, then extract the ZIP. In the extracted directory, use Python 3.9 or later:

```sh
python3 scripts/run.py --version
python3 scripts/run.py --input examples/input.json
```

Expected version: `karmen-memory-ledger 0.2.1`. For project:demo, the later correction selects CSV as report_format and retains its source and timestamp.

To install the complete skill into a host that reads `~/.agents/skills`:

```sh
python3 install.py --host agents
```

The installer refuses an existing destination. Host discovery and invocation vary; see the [full setup and practice guide](docs/tutorial.en.md). You can run the helper directly without an AI host.

## Use it with your own work

Give each observation a key, exact scope, source, and offset-aware updated_at. Use as_of for a reproducible view; add expires_at or deleted where needed.

Add conflicting values at the same timestamp, then test a different scope and an expired record. Inspect conflicts and inactive instead of flattening every observation into one unqualified fact.

Read the [field contract](docs/INPUT.md) before preparing a new input. The helper runs locally with the Python standard library; it needs no model account, API key, or network connection. An AI host has its own data and permission settings.

## Questions

**Will my AI remember this automatically?** Only if its host explicitly stores these records and supplies the relevant result later. Running the helper alone does not change an AI account.

**Where does the result go?** JSON is printed to stdout unless you request a new file with `--output`. Existing output files are preserved. The helper reads only the submitted records and any local paths documented in its input contract.

## Documentation and support

- [Download, install, configure, practice, upgrade, and remove](docs/tutorial.en.md)
- [Input/output contract](docs/INPUT.md) and [compatibility](docs/COMPATIBILITY.md)
- [Changelog](CHANGELOG.md), [contributing](CONTRIBUTING.md), [support](SUPPORT.md), and [security reports](SECURITY.md)

## License

[MIT](LICENSE). Keep the license and [notice](NOTICE.md) with redistributed copies. Maintained by [KarmenLoop](https://karmenloop.com).
