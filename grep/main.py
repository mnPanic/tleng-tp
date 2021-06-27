import grep
import sys
from ply import yacc

from typing import Set, List
from dataclasses import dataclass

from regex import *
from afd import *

DEBUG = False

def regex_to_afd(expr: Regex):
    expr = expr.simplify()

    # expr
    finals: List[Regex] = []
    start = expr
    states: List[Regex] = [expr]
    trans = {}

    pending_states = [expr] # expr = L0
    alphabet = sorted(list(expr.alphabet()))

    while (len(pending_states) != 0):
        current = pending_states.pop()
        #print(current)
        s_current = str(current)
        if s_current not in trans:
            trans[s_current] = {}

        for char in alphabet:
            next = current.der(char).simplify()
            #print(f"{current} -{char}> {next}")
            if next.is_empty():
                # "AFD"
                continue

            if next not in states:
                pending_states.append(next)
                states.append(next)

            trans[s_current][char] = str(next)

    for state in states:
        if state.nullable():
            finals.append(str(state))
    
    return AFD(states, alphabet, trans, start, finals)

def print_debug(s):
    if DEBUG:
        print(s)

def main():
    filename = sys.argv[1]
    regex = sys.argv[2]
    try:
        yacc.parse(f".*({regex}).*")
    except Exception as e:
        print("Couldn't parse expression:", e)
        return

    print_debug(grep.expr.__repr__())

    afd = regex_to_afd(grep.expr)

    print_debug(afd)

    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip()
            if afd.match(line):
                print(line)

if __name__ == "__main__":
    main()