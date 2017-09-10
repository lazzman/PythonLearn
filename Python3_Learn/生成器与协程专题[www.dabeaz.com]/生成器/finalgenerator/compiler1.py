# compiler1.py
#
# Compiler that builds a simple AST and evaluates it using the visitor pattern

import re
from collections import namedtuple

# ---- Tokenizer

tokens = [
    r'(?P<NUM>\d+)',
    r'(?P<PLUS>\+)',
    r'(?P<MINUS>-)',
    r'(?P<TIMES>\*)',
    r'(?P<DIVIDE>/)',
    r'(?P<WS>\s+)',
    ]

master_re = re.compile('|'.join(tokens))
Token = namedtuple('Token', ['type','value'])
def tokenize(text):
    scan = master_re.scanner(text)
    return (Token(m.lastgroup, m.group()) 
            for m in iter(scan.match, None) if m.lastgroup != 'WS')

# ---- AST Nodes

class Node:
    _fields = []
    def __init__(self, *args):
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

class BinOp(Node):
    _fields = ['op', 'left', 'right']

class Number(Node):
    _fields = ['value']

# ---- Simple recursive descent parser

def parse(toks):
    lookahead, current = next(toks, None), None
    def accept(*toktypes):
        nonlocal lookahead, current
        if lookahead and lookahead.type in toktypes:
            current, lookahead = lookahead, next(toks, None)
            return True

    def expr():
        left = term()
        while accept('PLUS','MINUS'):
            left = BinOp(current.value, left)
            left.right = term()
        return left

    def term():
        left = factor()
        while accept('TIMES','DIVIDE'):
            left = BinOp(current.value, left)
            left.right = factor()
        return left

    def factor():
        if accept('NUM'):
            return Number(int(current.value))
        else:
            raise SyntaxError()
    return expr()

# ---- Visitor pattern

class NodeVisitor:
    def visit(self, node):
        return getattr(self, 'visit_' + type(node).__name__)(node)

class Evaluator(NodeVisitor):
    def visit_Number(self, node):
        return node.value

    def visit_BinOp(self, node):
        leftval = self.visit(node.left)
        rightval = self.visit(node.right)
        if node.op == '+':
            return leftval + rightval
        elif node.op == '-':
            return leftval - rightval
        elif node.op == '*':
            return leftval * rightval
        elif node.op == '/':
            return leftval * rightval

# ---- Examples
if __name__ == '__main__':
    text = '2 + 3*4 - 5'
    toks = tokenize(text)
    tree = parse(toks)

    print('---- Evaluation')
    result = Evaluator().visit(tree)
    print('Result:', result)

    def explosion():
        'Run me to see a spectacular fail'
        text = '+'.join(str(x) for x in range(1000))   # Make '0+1+2+3+...+999'
        toks = tokenize(text)
        tree = parse(toks)
        val = Evaluator().visit(tree)
        print('Result:', val)



