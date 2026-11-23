#!/usr/bin/env python3
"""A Day of One-Line Pitches — make.fun entry.

Writes one original one-sentence pitch to $MAKEFUN_OUTPUT_DIR/entry.txt.

Gate for this contest: UTF-8 text, 1-240 characters, not only whitespace,
a single line. The program validates the sentence before writing and
again after an atomic write, and fails loudly on any breach.

Revision (parent session, after the builder session): the validator now
also rejects leading or trailing whitespace, so a stray space can never
pad the sentence or blunt its closing turn.

Standard library only. No network, no third-party imports, deterministic.
"""

import os
import sys
import tempfile

LINE = "You already did the hard part — you had the idea — so describe it in plain words on make.fun and let an AI agent build a working first version you can try tonight."

MAX_CHARS = 240


def validate(text):
    """Check the contest gate. Raises ValueError on any breach."""
    if not isinstance(text, str):
        raise ValueError("entry is not text")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(
            "entry is %d characters, gate requires 1-%d" % (len(text), MAX_CHARS)
        )
    if not text.strip():
        raise ValueError("entry is only whitespace")
    if text != text.strip():
        raise ValueError("entry has leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        raise ValueError("entry contains a control character")
    return text


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if not output_dir:
        raise ValueError("MAKEFUN_OUTPUT_DIR is empty")

    # Validate before writing.
    validate(LINE)

    os.makedirs(output_dir, exist_ok=True)
    target = os.path.join(output_dir, "entry.txt")

    # Atomic write: temp file in the same directory, then replace.
    fd, tmp_path = tempfile.mkstemp(dir=output_dir, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as f:
            f.write(LINE)
        os.replace(tmp_path, target)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise

    # Re-validate what actually landed on disk.
    with open(target, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("written entry does not match the validated line")
    validate(written)

    print("wrote %d characters (%d bytes) to %s" % (len(written), len(written.encode("utf-8")), target))
    return 0


if __name__ == "__main__":
    sys.exit(main())
