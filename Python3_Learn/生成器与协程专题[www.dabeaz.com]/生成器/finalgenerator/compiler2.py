import re
from collections import namedtuple
import types

# ---- Tokenizer

tokens = [
    r'(?P<NUMBER>\d+)',
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
        if accept('NUMBER'):
            return Number(int(current.value))
        else:
            raise SyntaxError()
    return expr()

# ---- Nonrecursive visitor pattern using generators

class NodeVisitor:
    def visit(self, node):
        stack = [ self.genvisit(node) ]
        result = None
        while stack:
            try:
                node = stack[-1].send(result)
                stack.append(self.genvisit(node))
                result = None
            except StopIteration as exc:
                stack.pop()
                result = exc.value
        return result

    def genvisit(self, node):
        result = getattr(self, 'visit_' + type(node).__name__)(node)
        return (yield from result) if isinstance(result, types.GeneratorType) else result

class Evaluator(NodeVisitor):
    def visit_Number(self, node):
        return node.value

    def visit_BinOp(self, node):
        leftval = yield node.left
        rightval = yield node.right
        if node.op == '+':
            return leftval + rightval
        elif node.op == '-':
            return leftval - rightval
        elif node.op == '*':
            return leftval * rightval
        elif node.op == '/':
            return leftval * rightval

# ---- Example

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

    print('---- Evil Evaluation')
    explosion()
