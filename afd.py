from typing import Dict, List, Set
from regex import Regex

class AFD:
    def __init__(self, states: List[Regex], alphabet: List[str], trans: Dict[str, Dict[str, str]], start: Regex, finals: Set) -> None:
        self.states = states
        self.alphabet = alphabet
        # state: {symbol: state}
        self.trans = trans
        self.finals = finals
        self.start = start
    
    def run(self, string: str) -> bool:
        pass

    def __str__(self) -> str:
        return f"""
states: {list(map(str, self.states))},
sigma:  {self.alphabet},
trans:  {self.trans},
start:  {self.start},
finals: {list(map(str, self.finals))}
"""