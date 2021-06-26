import grep
from ply import yacc

from typing import Set
from dataclasses import dataclass

from regex import *
from afd import *


def main():
    while True:
        try:
            s = input('regex> ')
        except EOFError:
            break
        yacc.parse(s)
        print(grep.expr)
        print(regex_to_afd(grep.expr))


def regex_to_afd(expr: Regex):
    expr = expr.simplify()

    # expr
    finals: List[Regex] = []
    start = expr
    states: List[Regex] = []
    trans = {}

    pending_states = [expr] # expr = L0
    alphabet = expr.alphabet()

    while (len(pending_states) != 0):
        current = pending_states.pop()
        states.append(current)

        for char in alphabet:
            next = current.der(char).simplify()
            if next not in states:
                pending_states.append(next)

            s_current = str(current)
            if s_current not in trans:
                trans[s_current] = {}

            trans[s_current][char] = str(next)

    for state in states:
        if state.nullable():
            finals.append(state)
    
    return AFD(states, alphabet, trans, start, finals)

if __name__ == "__main__":
    main()    