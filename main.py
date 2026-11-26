import os

# Painfully honest out-of-office auto-reply: admits the inbox is
# unanswerable, takes the rest anyway, and promises a proper answer.
# One sentence, 159 characters, no trailing newline in the output.
ENTRY = "I'm out until Monday — my inbox passed 4,000 unread and I finally admitted I can't answer them all, so I'm resting and will answer them properly when I'm back."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
with open(output_dir + "/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
