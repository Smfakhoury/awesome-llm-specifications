#!/usr/bin/env python3
"""Print a correctly formatted list entry for an arXiv paper.

Usage:
    python3 scripts/fetch_entry.py 2310.01831
    python3 scripts/fetch_entry.py https://arxiv.org/abs/2310.01831v2
"""

import json
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET

ATOM = {"a": "http://www.w3.org/2005/Atom"}
ARXIV_API = "http://export.arxiv.org/api/query?id_list="
S2_API = ("https://api.semanticscholar.org/graph/v1/paper/arXiv:{aid}"
          "?fields=venue,publicationVenue,year")
BADGE = ("[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat"
         "&logo=github&logoColor=white)]({url})")

VENUE_MAP = [
    (r"International Conference on Software Engineering", "ICSE"),
    (r"Foundations of Software Engineering|ESEC/SIGSOFT FSE|Proc\. ACM Softw\. Eng\.", "FSE"),
    (r"Automated Software Engineering", "ASE"),
    (r"Proc\. ACM Program\. Lang\.|OOPSLA|POPL|Programming Language Design", "PACMPL"),
    (r"Software Testing and Analysis", "ISSTA"),
    (r"IEEE Transactions on Software Engineering", "TSE"),
    (r"ACM Transactions on Software Engineering", "TOSEM"),
    (r"Computer Aided Verification", "CAV"),
    (r"Formal Methods in Computer-Aided Design", "FMCAD"),
    (r"Formal Methods", "FM"),
    (r"Neural Information Processing", "NeurIPS"),
    (r"Learning Representations", "ICLR"),
    (r"International Conference on Machine Learning", "ICML"),
    (r"Association for Computational Linguistics", "ACL"),
    (r"Empirical Methods in Natural Language", "EMNLP"),
    (r"Requirements Engineering", "RE"),
]


def arxiv_id(arg: str) -> str:
    m = re.search(r"(\d{4}\.\d{4,5})", arg)
    if not m:
        sys.exit(f"could not parse an arXiv id from: {arg}")
    return m.group(1)


def fetch_arxiv(aid: str) -> dict:
    with urllib.request.urlopen(ARXIV_API + aid, timeout=60) as resp:
        entry = ET.fromstring(resp.read()).find("a:entry", ATOM)
    if entry is None or entry.find("a:title", ATOM) is None:
        sys.exit(f"no arXiv entry found for {aid}")
    text = entry.find("a:summary", ATOM).text or ""
    comment = entry.find("{http://arxiv.org/schemas/atom}comment")
    if comment is not None and comment.text:
        text += " " + comment.text
    repos = re.findall(r"https?://github\.com/[A-Za-z0-9_.\-]+/[A-Za-z0-9_.\-]+", text)
    return {
        "title": " ".join(entry.find("a:title", ATOM).text.split()),
        "authors": [a.find("a:name", ATOM).text for a in entry.findall("a:author", ATOM)],
        "date": entry.find("a:published", ATOM).text[:7],
        "code": repos[0].rstrip(".,);") if repos else None,
    }


def fetch_venue(aid: str) -> str:
    try:
        with urllib.request.urlopen(S2_API.format(aid=aid), timeout=60) as resp:
            data = json.load(resp)
    except Exception:
        return "-"
    venue = (data.get("publicationVenue") or {}).get("name") or data.get("venue") or ""
    if not venue or venue.lower().startswith("arxiv"):
        return "-"
    for pattern, short in VENUE_MAP:
        if re.search(pattern, venue, re.I):
            return short
    return venue


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    aid = arxiv_id(sys.argv[1])
    paper = fetch_arxiv(aid)
    code = BADGE.format(url=paper["code"]) if paper["code"] else "-"
    print(f"- [{paper['title']}](https://arxiv.org/abs/{aid})")
    print(f"  - Author(s): {', '.join(paper['authors'])}")
    print(f"  - Date: {paper['date']}")
    print(f"  - Venue: {fetch_venue(aid)}")
    print(f"  - Code: {code}")


if __name__ == "__main__":
    main()
