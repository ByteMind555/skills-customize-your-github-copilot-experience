"""Starter scaffold for Intro to File I/O assignment.

Usage:
    python starter-code.py input.txt output.txt [--stats]

This scaffold shows how to read and write files safely and compute simple stats.
"""

import sys
from pathlib import Path


def preview_lines(path: Path, n: int = 5):
    try:
        with path.open("r", encoding="utf-8") as f:
            for i, line in enumerate(f, start=1):
                if i > n:
                    break
                print(f"{i:3}: {line.rstrip()}")
    except Exception as e:
        print(f"Error reading {path}: {e}")


def transform_lines(lines):
    # Example transform: strip trailing whitespace and convert to lowercase
    return [ln.rstrip().lower() for ln in lines]


def read_all(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return f.readlines()


def write_all(path: Path, lines):
    with path.open("w", encoding="utf-8") as f:
        f.writelines(line + "\n" if not line.endswith("\n") else line for line in lines)


def file_stats(lines):
    text = "".join(lines)
    words = text.split()
    return {
        "lines": len(lines),
        "words": len(words),
        "chars": len(text),
    }


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 1

    input_path = Path(argv[1])
    output_path = Path(argv[2])
    show_stats = "--stats" in argv

    if not input_path.exists():
        print(f"Input file not found: {input_path}")
        return 2

    print("Preview (first 5 lines):")
    preview_lines(input_path, n=5)

    lines = read_all(input_path)
    transformed = transform_lines([ln.rstrip("\n") for ln in lines])

    if show_stats:
        stats = file_stats(lines)
        print("\nFile statistics:")
        for k, v in stats.items():
            print(f"  {k}: {v}")

    try:
        write_all(output_path, transformed)
        print(f"Written transformed content to {output_path}")
    except Exception as e:
        print(f"Error writing to {output_path}: {e}")
        return 3

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
