# Sources and provenance

Research date: 2026-10-19.

## Public references

- [Grok Build: memory](https://github.com/xai-org/grok-build/blob/2bdd1d6a6369de0e8c68132ea4539e9abd9e14a8/crates/codegen/xai-grok-pager/docs/user-guide/13-memory.md)
- [Meta: Introducing Muse](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/)

## Design decision

The implementation uses a transparent versioned ledger rather than claiming hidden model memory or implicit cross-account sharing.

## Distribution

KarmenLoop wrote these instructions, helpers, examples, tests, and packaging. No upstream source tree, model weights, proprietary prompts, logos, or credentials are bundled. Python's standard library is the only runtime dependency.

Links identify research sources, not endorsement or certification. GitHub references are pinned to the revisions reviewed. Meta's Muse announcement describes a product; it does not establish that the personal-agent implementation is available as source.

Any future imported code must record its exact revision, files, copyright, license, and modifications in NOTICE.md.
