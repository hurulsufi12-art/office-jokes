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
    # Write atomically: a crash mid-write must never leave a truncated
    # entry.txt for the grader to read. Write to a temp file in the same
    # directory, flush it to disk, then rename over the target.
    tmp_path = os.path.join(out_dir, ".entry.txt.tmp")
    final_path = os.path.join(out_dir, "entry.txt")
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(TEXT)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp_path, final_path)
    # Read back and verify: the file the grader reads must be byte-identical
    # to the gated text, down to the exact UTF-8 byte count.
    with open(final_path, encoding="utf-8") as f:
        if f.read() != TEXT:
            raise SystemExit("entry.txt read-back mismatch after atomic write")
    if os.path.getsize(final_path) != len(TEXT.encode("utf-8")):
        raise SystemExit("entry.txt byte-length mismatch after atomic write")


if __name__ == "__main__":
    main()
