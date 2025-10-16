"""
python3 core8/pwb.py make/others/fixnat

"""

from pathlib import Path
import json
import tqdm

Dir2 = Path(__file__).parent.parent / "ma_lists"
# ---
with open(f"{Dir2}/jsons/All_Nat_o.json", "r", encoding="utf-8") as f:
    All_Nat_o = json.load(f)
# ---
with open(f"{Dir2}/jsons/nats.json", "r", encoding="utf-8") as f:
    nats = json.load(f)
# ---
deleted = 0
# ---
# code to del keys from nats if it has same value in All_Nat_o
# use tqdm
for x in tqdm.tqdm(nats.keys()):
    if All_Nat_o.get(x) == nats[x]:
        del nats[x]
        deleted += 1
# ---
print(f"deleted {deleted} keys from nats")
# ---
with open(f"{Dir2}/jsons/nats1.json", "w", encoding="utf-8") as f:
    json.dump(nats, f, indent=2, ensure_ascii=False)
