# -*- coding: utf-8 -*-

import ply.lex as lex

# List of token names.   This is always required
tokens = [
   'NUMBER',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'LPAREN',
   'RPAREN',
   'IGUALIGUAL',
   'IGUAL',
   'IDENT'
]

reserved = {
   'if': 'IF',
   'then': 'THEN',
   'else': 'ELSE',
   'while': 'WHILE',
   'end': 'END'
}

tokens = tokens + list(reserved.values())

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_IGUALIGUAL = r'=='
t_IGUAL = r'='
#t_IDENT = r'[a-zA-Z_][a-zA-Z_0-9]*'


def t_IDENT(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENT')    # Check for reserved words
    return t

# A regular expression rule with some action code


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule so we can track line numbers


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)


t_ignore = ' \t'
t_ignore_COMMENT = r'\#.*'

# Error handling rule


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def main(argv):
    pass

lexer = lex.lex()

if __name__ == '__main__':
    import sys
    main(sys.argv)