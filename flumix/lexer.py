from .error import raise_error

Token = str

class Lexer:
    def __init__(self, text) -> None:
        self.text = text
        self.current = 0
        self.line = 1
        self.char = text[0]
        self.tokens = []

def is_at_end(lexer):
    return lexer.char == '\0'

def advance(lexer):
    lexer.current += 1
    if lexer.char == '\n':
                lexer.line += 1
    lexer.char = lexer.text[lexer.current]

def peek(lexer) -> str:
    return lexer.text[lexer.current + 1]

def number(lexer):
    number = ""
    while lexer.char not in [' ', ')', '\n'] or is_at_end(lexer):
        number += lexer.char
        advance(lexer)
    lexer.tokens.append(number)

def symbol(lexer):
    symbol = ""
    while lexer.char not in [' ', ')', '\n'] or is_at_end(lexer):
        symbol += lexer.char
        advance(lexer)
    lexer.tokens.append(symbol)

def string(lexer):
    value = ""
    advance(lexer)
    while lexer.char != '"' or is_at_end(lexer):
        value += lexer.char
        advance(lexer)
    advance(lexer)
    value = '"' + value + '"'
    lexer.tokens.append(value)

def tokenize(text: str, file_name=None) -> Token:
    text += '\0'
    lexer = Lexer(text)
    while not is_at_end(lexer):
        if lexer.char in ['(', ')']:
            lexer.tokens.append(lexer.char)
            advance(lexer)
        elif lexer.char in [' ', '\n']:
            advance(lexer)
        elif lexer.char == '-':
            if peek(lexer) in list("0123456789"):
                number(lexer)
            else:
                symbol(lexer)
        elif lexer.char in list("0123456789"):
            number(lexer)
        elif lexer.char.isalpha() or lexer.char in list("!=<>*/^+-"):
            symbol(lexer)
        elif lexer.char == '"':
            string(lexer)
        elif lexer.char == '\0':
            continue
        else:
            raise_error("Lexer", f"Unexpected character '{lexer.char}'", line=lexer.line, source_code=lexer.text, file_name=file_name)
    return lexer.tokens