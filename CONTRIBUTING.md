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
- blog posts, essays, and talks from research groups and practitioners on the same topics

Out of scope:

- purely mathematical autoformalization and theorem proving with no software artifact
- hardware/RTL assertion and specification generation
- fuzzing, test-input generation, and vulnerability detection with no specification component
- general code generation that does not produce or consume a specification

## How the list is organized

Sections are grouped into parts by what the work is *for*:

| Part | Contains |
| --- | --- |
| 🧭 Start Here | Surveys, position papers, blog posts, and talks |
| 🔍 Where Specifications Come From | Inference and generation: specs, contracts, invariants, API/protocol models, and natural-language formalization |
| ✅ What Specifications Are For | Verification and proof synthesis; tests and oracles |
| 📊 Measuring Progress | Benchmarks, datasets, and empirical studies |
| 🛠️ Tools & Frameworks | LLM-based tools, and the traditional tools they build on |

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

## Adding a blog post or talk

Blog posts, engineering-blog articles, essays, and recorded talks go in **Blog Posts, Talks & Essays**. They must be technical, from a credible source, and specifically about specifications, proofs, contracts, invariants, or oracles in connection with AI. Use this format:

```markdown
- [Post Title](https://example.com/post)
  - Author(s): Author Name, Organization
  - Date: 2025-04
  - One sentence on why it is worth reading.
```

Link the canonical original URL, not a mirror or aggregator. Use `n/a` for the date only when the page genuinely shows none.

## Adding a tool

Tools go under **LLM-Based Tools** if a language model is part of how they work, and under **Traditional Specification & Verification Tools** otherwise. Traditional tools are included only when LLM work actually targets, extends, or benchmarks against them. One line per tool, describing what it does rather than how good it is.

## Other changes

- Fixing a wrong venue, date, author list, or dead link is always welcome.
- If you think a section is missing or a paper is miscategorized, open an issue first so we can agree on the structure.
- Please keep one logical change per pull request.

## Self-promotion

Adding your own paper is fine and encouraged — just make sure it is in scope and correctly formatted.
