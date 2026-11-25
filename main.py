"""One Line, Big Laugh: write a single funny line to /output/entry.txt.

The line is one self-contained joke. It opens on a mundane printer
complaint, then turns: the printer is treated like an employee afraid
of being replaced, and the payoff lands in the final words.
"""

LINE = (
    "I taped a photo of its replacement above my printer, "
    "and now it prints out of sheer terror."
)


def main() -> None:
    import os

    # The grader sets MAKEFUN_OUTPUT_DIR to its /output mount; locally,
    # fall back to ./output so a shared /output on this machine is
    # never touched (other workers verify against the same path).
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(
        "output"
    )
    target = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
