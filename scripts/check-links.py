"""Check that every parmana-core link in this repository points to a file that exists at its pinned commit.

Run from the repository root, with a clone of parmana-core at PARMANA_CORE (default: ../parmana-core).
Exit status 1 when a link does not resolve.
"""

import os
import pathlib
import re
import subprocess
import sys

CORE = os.environ.get("PARMANA_CORE", str(pathlib.Path(__file__).resolve().parents[2] / "parmana-core"))
LINK = re.compile(r"https://github\.com/pavancharak/parmana-core/blob/([0-9a-f]{8,40})/([^)\s]+)")


def exists(sha: str, path: str) -> bool:
    result = subprocess.run(
        ["git", "-C", CORE, "cat-file", "-e", f"{sha}:{path}"],
        capture_output=True,
    )
    return result.returncode == 0


def main() -> int:
    missing = []
    for md in pathlib.Path(".").rglob("*.md"):
        if ".git" in md.parts:
            continue
        for match in LINK.finditer(md.read_text(encoding="utf-8")):
            sha, path = match.group(1), match.group(2)
            if not exists(sha, path):
                missing.append(f"{md}: {sha} {path}")
    if missing:
        print("Links that do not resolve at their pinned commit:")
        print("\n".join(missing))
        return 1
    print("All parmana-core links resolve at their pinned commits.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
