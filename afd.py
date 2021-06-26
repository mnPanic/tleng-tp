from typing import Dict, List, Set
from regex import Regex

class AFD:
    def __init__(self, states: List[Regex], alphabet: List[str], trans: Dict[str, Dict[str, str]], start: Regex, finals: Set[str]) -> None:
        self.states = states
        self.alphabet = alphabet
        # state: {symbol: state}
        self.trans = trans
        self.finals = finals
        self.start = start
    
    def match(self, string: str) -> bool:
        current = str(self.start)

        for c in string:
            if c not in self.trans[current]:
                # estado "trampa"
                return False

            current = self.trans[current][c]

        return current in self.finals

    def __str__(self) -> str:
        return f"""
states: {list(map(str, self.states))},
sigma:  {self.alphabet},
trans:  {self.trans},
start:  {self.start},
finals: {list(map(str, self.finals))}
"""