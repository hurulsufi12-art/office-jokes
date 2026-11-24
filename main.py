"""Make the AI Judge Laugh: Office Jokes — entry program.

Writes one one-line joke about office life (under 200 characters)
to /output/entry.txt. Stdlib only, deterministic.
"""
import os

TEXT = (
    "I put 'per my last email' in my will so my family knows "
    "I already answered that question."
)


def main():
    # Enforce the scorer's gate (RULES.txt): UTF-8, 1-199 chars, one line,
    # not whitespace-only. Fail loudly instead of writing an invalid entry.
    if not 1 <= len(TEXT) <= 199 or "\n" in TEXT or not TEXT.strip():
        raise SystemExit("entry text violates the 1-199 char single-line gate")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
