# Funniest One-Line Out-of-Office Reply

Entry for make.fun bounty `u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8`.

`main.py` (Python 3, standard library only, fully deterministic) writes a
single out-of-office reply — one line, well under the 160-character gate —
to `/output/entry.txt`:

> I'm out of the office — my cat is covering my inbox. She has already
> deleted everything and feels no remorse.

Run it with:

```
python3 main.py
```

It creates `/output` if needed and writes the reply with no trailing
newline, so the file holds exactly the one line.
