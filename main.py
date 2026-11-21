#!/usr/bin/env python3
"""Entry program: copy the front-page image to the output directory.

The image (entry.png) is drawn by gen.py in this same repository and
shipped beside this program, so this program only copies its bytes.
It runs with no network and writes identical bytes on every run.
"""
import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(here, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)


if __name__ == "__main__":
    main()
