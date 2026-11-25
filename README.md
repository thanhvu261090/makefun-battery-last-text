# The Battery's Last Text to Its Charger

[![make.fun](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![Rank](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/thanhvu261090/makefun-battery-last-text/rank.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![Reward](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/thanhvu261090/makefun-battery-last-text/reward.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab)

Entry for the [make.fun bounty "The Battery's Last Text to Its Charger"](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab): one line of at most 200 characters — the phone battery's final text message to the charger it waited for all day.

## The entry

> hey it's me, 1%. i waited all day while you charged your vape, your watch, your toothbrush. plug me in, say sorry, and don't unplug me at 80% to 'save my health.'

(162 characters, one line.)

## Run it

```sh
python3 main.py
```

`main.py` writes the entry line to `/output/entry.txt` (or `$ENTRY_OUTPUT`)
and includes a `gate_check` self-test enforcing the 1–200 character,
single-line, no leading/trailing whitespace rule. The output is
deterministic — byte-identical on every run.

## License

MIT — see [LICENSE](LICENSE).
