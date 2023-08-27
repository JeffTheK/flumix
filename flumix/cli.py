import sys
from . import lexer
from . import parser
from . import interpreter 
from .std_env import STD_ENV

def main():
    exec(sys.argv)
    
def exec(args):
    file_path = args[1]
    exec_file(file_path)

def exec_file(file_path: str):
    file = open(file_path, 'r')
    contents = file.read()
    file.close()
    exec_string(contents)

def exec_string(string: str):
    tokens = lexer.tokenize(string)
    expression = parser.parse_tokens(tokens)
    interpreter.eval(expression, STD_ENV)