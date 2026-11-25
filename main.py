import os

LINE = "Fixed: humans no longer wake at 3 a.m. to replay every embarrassing thing they said in 2014."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
if not (1 <= len(LINE) <= 160) or "\n" in LINE or not LINE.strip():
    raise SystemExit("entry line outside the 1-160 char single-line gate")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
