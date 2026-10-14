# Contributing

Thanks for helping keep this list useful and accurate!

## Scope

This list covers **specifications for software** in the era of large language models:

- inferring or generating specifications from code, tests, documentation, or natural language
- contracts, pre/postconditions, loop and class invariants, type-level and memory-safety annotations
- test oracles, assertions, property-based tests, and metamorphic relations used as executable specifications
- translating requirements and intent into formal artifacts (LTL/STL, TLA+, Alloy, state machines)
- verification, proof synthesis, and repair pipelines that consume those specifications
- benchmarks, datasets, empirical studies, surveys, and tooling for the above

Out of scope:

- purely mathematical autoformalization and theorem proving with no software artifact
- hardware/RTL assertion and specification generation
- fuzzing, test-input generation, and vulnerability detection with no specification component
- general code generation that does not produce or consume a specification

## Adding a paper

1. Put the paper in the **most specific** matching section. If several fit, prefer the section that matches the paper's main contribution.
2. Keep each section in **reverse-chronological order** (newest first), by the `Date` field.
3. Link the **arXiv abstract page** when one exists; otherwise use the publisher page or an official PDF.
4. Use this exact entry format:

```markdown
- [Paper Title](https://arxiv.org/abs/2310.01831)
  - Author(s): First Author, Second Author, Third Author
  - Date: 2023-10
  - Venue: FSE
  - Code: [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/org/repo)
```

Field rules:

- **Author(s):** all authors, in order, comma separated.
- **Date:** `YYYY-MM` of the first public version (usually the v1 preprint).
- **Venue:** short acronym (`ICSE`, `FSE`, `ASE`, `PACMPL`, `CAV`, `NeurIPS`, ...) or `-` for preprints.
- **Code:** GitHub badge linking to the artifact, or `-` when none exists. Verify the link resolves.

A helper script generates a correct entry from an arXiv ID or URL:

```bash
python3 scripts/fetch_entry.py 2310.01831
python3 scripts/fetch_entry.py https://arxiv.org/abs/2310.01831
```

## Other changes

- Fixing a wrong venue, date, author list, or dead link is always welcome.
- If you think a section is missing or a paper is miscategorized, open an issue first so we can agree on the structure.
- Please keep one logical change per pull request.

## Self-promotion

Adding your own paper is fine and encouraged — just make sure it is in scope and correctly formatted.
