from .types import PythonFunction
from . import interpreter

def _print(args, env):
    for a in args:
        print(a)

def _do(args, env):
    for a in args:
        interpreter.eval(a, env)

STD_ENV = {
    "do": PythonFunction("do", _do, False),
    "print": PythonFunction("print", _print, True)
}