from ..types import Function, PythonFunction
from .. import interpreter

def _print(args, env):
    for a in args:
        print(a)

def _do(args, env):
    for a in args:
        interpreter.eval(a, env)

def _func(args, env):
    name = args[0]
    params = args[1]
    body = args[2:]
    func = Function(name, body, False, params)
    env.outer[name] = func

STDLIB_CORE = {
    "do": PythonFunction("do", _do, False),
    "func": PythonFunction("func", _func, False),
    "print": PythonFunction("print", _print, True)
}