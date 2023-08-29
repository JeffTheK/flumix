from .types import Expression, Int, Float, Symbol, Atom, String
from .lexer import Token
from .error import raise_error

def parse_tokens(tokens: "list[Token]") -> Expression:
    if len(tokens) == 0:
        raise_error("Parser", "Unexpected EOF")
    
    try:
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
    except Exception as e:
        raise_error("Parser", f"Unexpected exception {e}", line=token.line)

def number(token: Token) -> Atom:
    if token.count('.') > 0:
        return Float(token.value)
    else:
        return Int(token.value)

def string(token: Token) -> String:
    return token[1:-1]

def atom(token: Token) -> Atom:
    if token[0] in list("1234567890"):
        return number(token)
    elif token[0] == "-" and len(token) > 1 and token[1] in list("1234567890"):
        return number(token)
    elif token[0] == '"':
        return string(token)
    else:
        return Symbol(token)
