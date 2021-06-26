from ply import lex, yacc

from regex import *

"""
E -> E|C | C
C -> CU | U
U -> A* | A+ | A? | A
A -> . | char | (E)
"""

tokens = (
    'STAR',
    'OR',
    'PLUS',
    'QMARK',
    'RPAREN',
    'LPAREN',
    'CHAR',
    'DOT'
)

# Tokens
t_STAR = r'\*'
t_OR = r'\|'
t_PLUS = r'\+'
t_QMARK = r'\?'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_CHAR = r'[a-zA-Z0-9 ]'
t_DOT = r'.'

# Ignored characters
t_ignore = "\n\t"

def t_error(t):
    print(f"Illegal character {t.value[0]!r}")
    t.lexer.skip(1)

# Build the lexer
lex.lex()

expr = {}

def p_start(p):
    "expr2 : expr"
    global expr
    expr = p[1]

def p_expression_or(p):
    'expr : expr OR concat'
    p[0] = Or(p[1], p[3])
    
def p_expresssion_concat(p):
    'expr : concat'
    p[0] = p[1]

def p_concat(p):
    'concat : concat unary'
    p[0] = Concat(p[1], p[2])

def p_concat_unary(p):
    'concat : unary'
    p[0] = p[1]

def p_unary(p):
    '''unary : atomic STAR
             | atomic PLUS
             | atomic QMARK'''
            
    if p[2] == '*'  : p[0] = Star(p[1])
    elif p[2] == '+': p[0] = Plus(p[1])
    elif p[2] == '?': p[0] = QMark(p[1])

def p_unary_atomic(p):
    'unary : atomic'
    p[0] = p[1]

def p_atomic_dot(p):
    'atomic : DOT'
    p[0] = Dot()

def p_atomic_char(p):
    'atomic : CHAR'
    p[0] = Char(p[1])

def p_atomic_exp_paren(p):
    'atomic : LPAREN expr RPAREN'
    p[0] = Parentheses(p[2])

def p_error(p):
    print(f"Syntax error at {p.value!r}")

yacc.yacc()
