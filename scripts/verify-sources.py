#!/usr/bin/env python3
"""Check that the verbatim statute quotes in references/ still match their sources.

The central claim of this repo is that a reader can re-check every finding against
primary text. That claim is worth exactly as much as the ability to test it, so this
script tests it: it re-fetches each source and confirms every quoted passage still
appears, character for character after whitespace normalisation.

Where a source cannot be fetched it says so and prints how to check by hand. It does
NOT pass silently. A verifier that reports success for something it did not read would
be the same defect the skills are built to avoid.

Usage:  python3 scripts/verify-sources.py [--verbose]
Exit:   0 all fetched sources match | 1 a quote drifted | 2 nothing could be fetched
"""
import html, re, sys, urllib.error, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")

# reference file -> the pages that carry its text.
SOURCES = {
    "device-claims/skills/device-claims-review/references/hwg.md": [
        "https://www.gesetze-im-internet.de/heilmwerbg/__1.html",
        "https://www.gesetze-im-internet.de/heilmwerbg/__3.html",
        "https://www.gesetze-im-internet.de/heilmwerbg/__3a.html",
        "https://www.gesetze-im-internet.de/heilmwerbg/__11.html",
    ],
    "device-claims/skills/device-claims-review/references/uwg.md": [
        "https://www.gesetze-im-internet.de/uwg_2004/__5.html",
        "https://www.gesetze-im-internet.de/uwg_2004/__6.html",
    ],
    "device-claims/skills/device-claims-review/references/mdr-ivdr-art7.md": [
        "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32017R0745",
    ],
    "mpdg-germany/skills/german-additions/references/mpdg.md": [
        "https://www.gesetze-im-internet.de/mpdg/__4.html",
        "https://www.gesetze-im-internet.de/mpdg/__8.html",
        "https://www.gesetze-im-internet.de/mpdg/__73.html",
    ],
    "mdr-classification/skills/software-classification/references/annex-viii-software.md": [
        "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32017R0745",
    ],
}

# EUR-Lex serves a stub to non-browser clients: HTTP 202 with ~2 KB of shell. Size
# alone cannot detect it -- gesetze-im-internet legitimately serves each section as its
# own 3-8 KB page. The tell is the status code, plus how much text survives tag
# stripping. Treat those as UNFETCHED, never as a failed match.
MIN_TEXT = 500


def normalise(s: str) -> str:
    """Collapse the differences that are not the text: whitespace and quote glyphs."""
    s = html.unescape(s)
    for a, b in [("‘", "'"), ("’", "'"), ("“", '"'), ("”", '"'),
                 ("—", "-"), ("–", "-"), ("−", "-"), ("\xa0", " ")]:
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip()


def page_text(url: str):
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-GB,en;q=0.9,de;q=0.8",
    })
    try:
        with urllib.request.urlopen(req, timeout=45) as r:
            raw = r.read().decode("utf-8", errors="replace")
            status = r.status
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        return None, f"fetch failed: {e}"
    if status != 200:
        return None, f"HTTP {status} — served a stub, not the document (bot protection)"
    body = re.sub(r"<(script|style).*?</\1>", " ", raw, flags=re.S | re.I)
    text = normalise(re.sub(r"<[^>]+>", " ", body))
    if len(text) < MIN_TEXT:
        return None, f"HTTP {status} but only {len(text)} chars of text — stub, not the document"
    return text, None


def quotes_in(path: Path):
    """Every markdown blockquote line is a verbatim claim. Group into passages."""
    out, buf = [], []
    for line in path.read_text().splitlines():
        if line.lstrip().startswith(">"):
            buf.append(re.sub(r"^\s*>\s?", "", line))
        elif buf:
            out.append(" ".join(buf)); buf = []
    if buf:
        out.append(" ".join(buf))
    cleaned = []
    for q in out:
        # An elision marks a deliberate gap. The fragments either side are each
        # verbatim, but the joined string is not -- matching it whole would fail by
        # construction. Verify each fragment instead.
        parts = re.split(r"\[\s*(?:\.\.\.|…)\s*\]", q)
        frags = []
        for part in parts:
            part = re.sub(r"\*\*|`", "", part)                    # emphasis
            part = re.sub(r"\[[^\]]*\]", "", part)                # citation tags
            part = re.sub(r"^\s*\(?\d+\.?\d*[a-z]?\)?\.?\s*", "", part)  # leading numbering
            part = normalise(part).strip(" ;:,.\u2014-")
            if len(part) >= 30:
                frags.append(part)
        if frags:
            cleaned.append(frags)
    return cleaned


def longest_run(quote: str, corpus: str) -> str:
    """Longest leading fragment of `quote` present in corpus — shows where drift starts."""
    lo, hi = 0, len(quote)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if quote[:mid] in corpus:
            lo = mid
        else:
            hi = mid - 1
    return quote[:lo]


def main():
    verbose = "--verbose" in sys.argv
    corpora, notes = {}, {}
    for url in sorted({u for v in SOURCES.values() for u in v}):
        corpora[url], notes[url] = page_text(url)

    drifted = fetched_any = 0
    print()
    for rel, urls in SOURCES.items():
        path = ROOT / rel
        if not path.exists():
            print(f"  MISSING FILE  {rel}"); drifted += 1; continue
        corpus = " ".join(corpora[u] for u in urls if corpora[u])
        if not corpus:
            print(f"  UNVERIFIED    {rel}")
            for u in urls:
                print(f"                {notes[u]}")
                print(f"                check by hand: {u}")
            qs = quotes_in(path)
            if qs and qs[0]:
                print(f"                search the page for: \"{qs[0][0][:70]}...\"")
            continue
        fetched_any += 1
        qs = quotes_in(path)
        nfrag = sum(len(f) for f in qs)
        bad = [f for frags in qs for f in frags if f not in corpus]
        if bad:
            print(f"  DRIFTED       {rel}  ({len(bad)} of {nfrag} fragments no longer match)")
            for f in bad[:3]:
                run = longest_run(f, corpus)
                print(f"                quoted: \"{f[:80]}...\"")
                print((f"                on page up to: \"...{run[-60:]}\"") if run else
                      "                no part of this fragment is on the page")
            drifted += 1
        else:
            print(f"  OK            {rel}  ({nfrag} fragments across {len(qs)} quotes match)")
            if verbose:
                for frags in qs:
                    for f in frags:
                        print(f"                · {f[:90]}")
    print()
    if drifted:
        print(f"{drifted} reference file(s) no longer match their source. Re-retrieve and "
              f"update the retrieval date before relying on them.")
        return 1
    if not fetched_any:
        print("No source could be fetched. Nothing was verified — do not read this as a pass.")
        return 2
    print("Every quote from every fetched source matches. Unverified files are listed above.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
