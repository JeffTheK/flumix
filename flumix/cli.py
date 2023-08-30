import sys
from . import lexer
from . import interpreter 
from . repl import repl_loop

def main():
    exec(sys.argv)

def exec(args: "list[str]"):
    if len(args) == 1:
        repl_loop()
    else:
        file_path = args[-1]

        if "--tokenize" in args:
            tokenize_file(file_path)
        else:
            exec_file(file_path, sys.argv[2:])

def tokenize_file(file_path):
    file = open(file_path, 'r')
    contents = file.read()
    file.close()
    print(lexer.tokenize(contents, file_path))

def exec_file(file_path: str, argv=None):
    file = open(file_path, 'r')
    contents = file.read()
    file.close()
    interpreter.exec_string(contents, argv=argv)