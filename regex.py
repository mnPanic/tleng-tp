from dataclasses import dataclass

@dataclass
class Regex:
    pass

@dataclass
class Or(Regex):
    'left | right'
    left: Regex
    right: Regex

@dataclass
class Concat(Regex):
    'left . right'
    left: Regex
    right: Regex

@dataclass
class QMark(Regex):
    'expr?'
    expr: Regex

@dataclass
class Star(Regex):
    'expr*'
    expr: Regex

@dataclass
class Plus(Regex):
    'expr+'
    expr: Regex

@dataclass
class Dot(Regex):
    '.'
    pass

@dataclass
class Char(Regex):
    value: str

@dataclass
class Parentheses(Regex):
    '(E)'
    expr: Regex
