"""
monkeytype run _start.py
monkeytype run _start.py

"""
from src import event
import subprocess

tab = event(["yemen"])
# run pytest
subprocess.run(["pytest", "-m", "slow"])
