import sys
from . import lexer
from . import parser
from . import interpreter 
from .std_env import STD_ENV

def main():
    exec(sys.argv)

def exec(args: "list[str]"):
    file_path = args[-1]
    if "-tokenize" in args:
        tokenize_file(file_path)
    else:
        exec_file(file_path)

def tokenize_file(file_path):
    file = open(file_path, 'r')
    contents = file.read()
    file.close()
    print(lexer.tokenize(contents))

def exec_file(file_path: str):
    file = open(file_path, 'r')
    contents = file.read()
    file.close()
    exec_string(contents)

def exec_string(string: str):
    tokens = lexer.tokenize(string)
    expression = parser.parse_tokens(tokens)
    interpreter.eval(expression, STD_ENV)