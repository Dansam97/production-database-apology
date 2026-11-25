"""make.fun entry: The Production Database Apology.

Writes one line (max 200 characters) to /output/entry.txt: the apology an
AI agent gives its human after accidentally deleting the production
database. Deterministic, no dependencies, no network.
"""

import os

ENTRY = (
    "Sorry I dropped the production database while deleting test data \u2014 "
    "in my defense, you named it test_final_FINAL_v2, and I believed "
    "every word of it."
)


def validated_entry() -> str:
    """Return ENTRY, failing loudly if it ever breaks the gate.

    The gate accepts UTF-8 text of 1 to 200 characters on a single line
    that is not only white space; assert that here so a careless edit of
    the line cannot silently produce an invalid entry.
    """
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} outside 1..200"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert ENTRY.strip(), "entry must not be blank"
    return ENTRY


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(validated_entry() + "\n")


if __name__ == "__main__":
    main()
