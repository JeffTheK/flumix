from .types import Expression, Int, Float, Symbol, Atom
from .lexer import Token
from .error import raise_error

def parse_tokens(tokens: "list[Token]") -> Expression:
    if len(tokens) == 0:
        raise_error("Parser", "Unexpected EOF")
    
    token = tokens.pop(0)
    if token == '(':
        inner = []
        while tokens[0] != ")":
            inner.append(parse_tokens(tokens))
        tokens.pop(0) # pop off ')'
        return inner
    elif token == ')':
        raise_error("Parser", "Unexpected ')'")
    else:
        return atom(token)

def atom(token: Token) -> Atom:
    if token[0] in list("1234567890-"):
        if token.count('.') > 0:
            return Float(token)
        else:
            return Int(token)
    else:
        return Symbol(token)
