import string

from typing import Set
from dataclasses import dataclass

ALL_DIGITS = list(string.ascii_lowercase + string.ascii_uppercase + string.digits + " ")

@dataclass
class Regex:
    def nullable(self) -> bool:
        pass

    def alphabet(self) -> Set[str]:
        pass

    def der(self, symbol: str): # -> Regex
        pass

    def is_empty(self) -> bool:
        return isinstance(self, Empty)
    
    def is_lambda(self) -> bool:
        return isinstance(self, Lambda)
    
    def simplify(self): # -> Regex
        return self

    def __str__(self) -> str:
        pass

    def __eq__(self, o: object) -> bool:
        return str(self) == str(o)

@dataclass
class Or(Regex):
    'left | right'
    left: Regex
    right: Regex

    def nullable(self) -> bool:
        return self.left.nullable() or self.right.nullable()
    
    def alphabet(self) -> Set[str]:
        return self.left.alphabet().union(self.right.alphabet())

    def der(self, symbol: str):
        return Or(self.left.der(symbol), self.right.der(symbol))

    def simplify(self):
        r_sim = self.right.simplify()
        l_sim = self.left.simplify() 
        if l_sim.is_empty() and r_sim.is_empty():
            return Empty()

        if l_sim.is_empty():
            return r_sim
        
        if r_sim.is_empty():
            return l_sim

        return Or(l_sim, r_sim)
    
    def __str__(self) -> str:
        return f"{str(self.left)}|{str(self.right)}"

@dataclass
class Concat(Regex):
    'left . right'
    left: Regex
    right: Regex

    def nullable(self) -> bool:
        return self.left.nullable() and self.right.nullable()
    
    def alphabet(self) -> Set[str]:
        return self.left.alphabet().union(self.right.alphabet())
    
    def der(self, symbol: str):
        if self.left.nullable():
            return Or(
                Concat(self.left.der(symbol), self.right),
                self.right.der(symbol),
            )

        return Concat(self.left.der(symbol), self.right)

    def simplify(self):
        r_sim = self.right.simplify()
        l_sim = self.left.simplify() 
        if l_sim.is_empty() or r_sim.is_empty():
            return Empty()

        if l_sim.is_lambda():
            return r_sim
        
        if r_sim.is_lambda():
            return l_sim

        return Concat(l_sim, r_sim)

    def __str__(self) -> str:
        return str(self.left) + str(self.right)

@dataclass
class QMark(Regex):
    'expr?'
    expr: Regex

    def nullable(self) -> bool:
        return True
    
    def alphabet(self) -> Set[str]:
        return self.expr.alphabet()

    def der(self, symbol: str):
        return self.expr.der(symbol)

    def __str__(self) -> str:
        return f"{str(self.expr)}?"

@dataclass
class Star(Regex):
    'expr*'
    expr: Regex

    def nullable(self) -> bool:
        return True
    
    def alphabet(self) -> Set[str]:
        return self.expr.alphabet()
    
    def der(self, symbol: str):
        return Concat(
            self.expr.der(symbol),
            self,
        )

    def __str__(self) -> str:
        return f"{str(self.expr)}*"

@dataclass
class Plus(Regex):
    'expr+'
    expr: Regex

    def nullable(self) -> bool:
        return False

    def alphabet(self) -> Set[str]:
        return self.expr.alphabet()
    
    def der(self, symbol: str):
        # u+ = uu*
        return Concat(self.expr, Star(self.expr)).der(symbol)
    
    def __str__(self) -> str:
        return f"{str(self.expr)}+"

@dataclass
class Dot(Regex):
    '.'

    def nullable(self) -> bool:
        return False

    def alphabet(self) -> Set[str]:
        #return set()
        return ALL_DIGITS

    def der(self, symbol: str):
        return Lambda()
    
    def __str__(self) -> str:
        return "."

@dataclass
class Char(Regex):
    value: str

    def nullable(self) -> bool:
        return False
    
    def alphabet(self) -> Set[str]:
        return set(self.value)
    
    def der(self, symbol: str):
        return Lambda() if self.value == symbol else Empty()
    
    def __str__(self) -> str:
        return self.value

@dataclass
class Parentheses(Regex):
    '(E)'
    expr: Regex

    def nullable(self) -> bool:
        return self.expr.nullable()
    
    def alphabet(self) -> Set[str]:
        return self.expr.alphabet()

    def der(self, symbol: str):
        return self.expr.der(symbol)
    
    def __str__(self) -> str:
        return f"({str(self.expr)})"

@dataclass
class Empty(Regex):
    '∅'

    def nullable(self) -> bool:
        return False

    def alphabet(self) -> Set[str]:
        return set()
    
    def der(self, symbol: str):
        return self
    
    def __str__(self) -> str:
        return "∅"

@dataclass
class Lambda(Regex):
    'λ'

    def nullable(self) -> bool:
        return True

    def alphabet(self) -> Set[str]:
        return set()

    def der(self, symbol: str):
        return Empty()
    
    def __str__(self) -> str:
        return "λ"
