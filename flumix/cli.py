import sys
from . import lexer
from . import interpreter 

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
    interpreter.exec_string(contents)