# -*- coding: utf-8 -*-

import cmd
import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from lexer import tokens

names = {}


def p_statement_assign(p):
    'statement : IDENT IGUAL expression'
    names[p[1]] = p[3]


def p_statement_expression(p):
    'statement : expression'
    p[0] = p[1]


def p_expression_plus(p):
    'expression : expression PLUS term'
    try:
        p[0] = p[1] + p[3]
    except:
        print("Ahhhh")

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]


def p_expression_term(p):
    'expression : term'
    p[0] = p[1]


def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]


def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]


def p_term_factor(p):
    'term : factor'
    p[0] = p[1]


def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]


def p_factor_ident(p):
    'factor : IDENT'
    try:
        p[0] = names[p[1]]
    except LookupError:
        print("undefined name '%s'" % p[1])
        #p[0] = 0

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]


# Error rule for syntax errors


def p_error(p):
    #print("Syntax error in input!")
    print p
    raise SyntaxError


# Build the parser
parser = yacc.yacc()


class int(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "int >"
        self.intro = "Hi !!"
        self.__doc__ = "DOC"

    def do_exit(self, args):
        """Exits from the console"""
        return -1

    def do_EOF(self, args):
        """Exit on system end of file character"""
        print("Good bye!")
        return self.do_exit(args)

    def do_help(self, args):
        print((self.__doc__))

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def default(self, line):
        """Called on an input line when the command prefix
           is not recognized.
           In that case we execute the line as Python code.
        """
        try:
            result = parser.parse(line)
        except SyntaxError:
            print("Syntax error!")
        else:
            names['last'] = result
            print(result)

    def do_names(self, args):
        """List names"""
        print(names)


i = int()

i.cmdloop()