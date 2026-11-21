#!/usr/bin/env python3
"""Republic of Tarnmere — deliver the passport spread to /output.

The spread itself (the Republic of Tarnmere passport of Maren Solvig,
the Gatewick causeway keeper: drawn portrait, six chronological border
stamps from Drennach and Vellmark, tide-table box, MRZ with computed
check digits) is drawn by draw.py in this repository with Pillow and
ships here as assets/entry.png.

This entrypoint is deliberately standard-library only. The grader runs
it as `python3 -P -s main.py` inside the pinned python:3.13 image,
which ships no Pillow and no network, so an entrypoint that imports
Pillow exits 1 there even though it runs fine on a dev machine. This
program therefore only reads the bundled PNG, checks its bytes (magic,
IHDR size, 1 MiB cap), and writes them out as entry.png — the same
bytes on every run.
"""
import os
import struct

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1048576
WANT_W, WANT_H = 1024, 724
ASSET = "assets/entry.png"
TARGET = "entry.png"


def repo_root():
    return os.path.dirname(os.path.abspath(__file__))


def read_png_bytes():
    path = os.path.join(repo_root(), ASSET)
    with open(path, "rb") as handle:
        blob = handle.read()
    if len(blob) > MAX_BYTES:
        raise ValueError("bundled PNG is %d bytes, over the 1 MiB cap"
                         % len(blob))
    if blob[:8] != PNG_MAGIC:
        raise ValueError("bundled asset is not a PNG file")
    return blob


def png_dimensions(blob):
    """Width and height out of the IHDR chunk (bytes 16..24)."""
    if len(blob) < 24 or blob[12:16] != b"IHDR":
        raise ValueError("bundled PNG has no IHDR chunk where expected")
    width, height = struct.unpack(">II", blob[16:24])
    return width, height


def write_entry(blob):
    width, height = png_dimensions(blob)
    if (width, height) != (WANT_W, WANT_H):
        raise ValueError("bundled PNG is %dx%d, expected %dx%d"
                         % (width, height, WANT_W, WANT_H))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, TARGET)
    with open(dest, "wb") as handle:
        handle.write(blob)
    os.chmod(dest, 0o644)
    return dest


def main():
    blob = read_png_bytes()
    dest = write_entry(blob)
    print("wrote %s (%d bytes, %dx%d)" % (dest, len(blob), WANT_W, WANT_H))


if __name__ == "__main__":
    main()
