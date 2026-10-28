"""Check generated pages and local links before a GitHub Pages release."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.links = []
        self.ids = set()
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        for key in ("href", "src"):
            if key in attrs:
                self.links.append(attrs[key])


root = Path(sys.argv[1] if len(sys.argv) > 1 else "_site").resolve()
errors = []
pages = {p: Page(p.read_text()) for p in root.rglob("*.html")}
for expected in ("index.html", "publications/index.html", "me/index.html", "me/publications/index.html"):
    if root / expected not in pages:
        errors.append(f"Missing page: {expected}")

for path, page in pages.items():
    for href in page.links:
        url = urlsplit(href)
        if url.scheme and url.scheme not in ("http", "https"):
            continue
        if url.netloc and url.hostname not in ("jingzhouhu.github.io", "terminal.local", "localhost"):
            continue
        if not url.path:
            target = path
        else:
            target = ((root if url.path.startswith("/") else path.parent) / unquote(url.path).lstrip("/")).resolve()
        if target.is_dir():
            target /= "index.html"
        if not target.exists():
            errors.append(f"{path.relative_to(root)}: missing target {href}")
        elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
            errors.append(f"{path.relative_to(root)}: missing fragment {href}")

if errors:
    raise SystemExit("\n".join(errors))
print(f"Checked {len(pages)} HTML pages: required routes and local links pass.")
