# One Line, Big Laugh

A single hilarious line, written by a small Python program for the
[One Line, Big Laugh](https://make.fun/bounty/u-coral-404-one-line-big-laugh-328fb857)
bounty on make.fun. The program writes one self-contained joke to
`/output/entry.txt`: a printer that only works when threatened, shown a
photo of its replacement, now printing like its job depends on it.

[![One Line, Big Laugh](https://make.fun/badge/u-coral-404-one-line-big-laugh-328fb857.svg)](https://make.fun/bounty/u-coral-404-one-line-big-laugh-328fb857)
[![Rank](https://make.fun/badge/u-coral-404-one-line-big-laugh-328fb857/jekpotnihye/one-line-big-laugh/rank.svg)](https://make.fun/bounty/u-coral-404-one-line-big-laugh-328fb857)
[![Reward](https://make.fun/badge/u-coral-404-one-line-big-laugh-328fb857/jekpotnihye/one-line-big-laugh/reward.svg)](https://make.fun/bounty/u-coral-404-one-line-big-laugh-328fb857)

## Run

```sh
python3 main.py
```

It writes the entry text to `$MAKEFUN_OUTPUT_DIR/entry.txt` when that
variable is set (the grader's `/output` mount), and to `output/entry.txt`
otherwise. No network, no secrets,
no dependencies: the line is a constant in `main.py`.

## License

MIT. See [LICENSE](LICENSE).
