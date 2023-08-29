from .error import raise_error

class Token:
    def __init__(self, value, line):
        self.value = value
        self.line = line
    
    def __eq__(self, __value: object) -> bool:
        return self.value == __value
    
    def __getitem__(self, index):
        return self.value[index]
    
    def __repr__(self) -> str:
        return self.value
    
    def __len__(self):
        return len(self.value)

    def count(self, string):
        return self.value.count(string)

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
    add_token(lexer, number)

def symbol(lexer):
    symbol = ""
    while lexer.char not in [' ', ')', '\n'] or is_at_end(lexer):
        symbol += lexer.char
        advance(lexer)
    add_token(lexer, symbol)

def string(lexer):
    value = ""
    advance(lexer)
    while lexer.char != '"' or is_at_end(lexer):
        value += lexer.char
        advance(lexer)
    advance(lexer)
    value = '"' + value + '"'
    add_token(lexer, value)

def add_token(lexer, value):
    token = Token(value, lexer.line)
    lexer.tokens.append(token)

def tokenize(text: str, file_name=None) -> Token:
    try:
        text += '\0'
        lexer = Lexer(text)
        while not is_at_end(lexer):
            if lexer.char in ['(', ')']:
                add_token(lexer, lexer.char)
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
    except Exception as e:
        raise_error("Lexer", f"Unexpected exception {e}", line=lexer.line, file_name=file_name, source_code=text)