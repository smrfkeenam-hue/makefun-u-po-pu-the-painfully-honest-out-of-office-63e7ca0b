# AGENT.md

## Entry

One out-of-office auto-reply, a single sentence of 159 characters: the sender is out until Monday, admits their inbox passed 4,000 unread and they can't answer them all, and promises to answer properly when back. Painfully honest about the workload, warm and polite enough for a manager to let it stand.

## How it works

`main.py` (Python 3, stdlib only — `import os`) holds the reply in the `ENTRY` constant and writes it, with no trailing newline, to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).
