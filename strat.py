from typing import List, Tuple
from enum import Enum
import random

class Action(Enum):
    TRUST = 0
    CHEAT = 1

def strategy(past_self: List[Action], past_opponent: List[Action]) -> Action:
    if len(past_self) == 0:
        return Action.TRUST
    elif past_opponent[-1] == Action.CHEAT:
        return Action.CHEAT
    else:
        return Action.TRUST if random.random() < 0.9 else Action.CHEAT
