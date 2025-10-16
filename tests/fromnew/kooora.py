import sys
from fromnet import kooora_team, kooora_player

# python3 core8/pwb.py make/kooora test Osceola, Fond du Lac County, Wisconsin
# python3 core8/pwb.py make/kooora test kristianstad
# ---

if "team" in sys.argv:
    Olist = sys.argv
    Olist.remove(sys.argv[0])
    Olist.remove("team")
    # ---
    Name = " ".join(Olist)
    kooora_team(Name)

# python3 core8/pwb.py make/kooora player Lasse Nilsson
elif "player" in sys.argv:
    Olist = sys.argv
    Olist.remove(sys.argv[0])
    Olist.remove("player")
    # ---
    Name = " ".join(Olist)
    kooora_player(Name)
