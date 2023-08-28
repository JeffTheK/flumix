from ..types import Function, PythonFunction
from .. import interpreter

def _print(args, env):
    for a in args:
        print(a)

def _do(args, env):
    for a in args:
        interpreter.eval(a, env)

def _var(args, env):
    from ..types import Symbol
    name = args[0]
    value = interpreter.eval(args[1], env)
    env.outer[name] = value

def _func(args, env):
    name = args[0]
    params = args[1]
    body = args[2:]
    func = Function(name, body, False, params)
    env.outer[name] = func

def _include_file(args, env):
    path = args[0]
    with open(path, 'r') as file:
        contents = file.read()
        interpreter.exec_string(contents)

def _if(args, env):
    condition = args[0]
    on_true = args[1]
    on_false = args[2]

    if interpreter.eval(condition, env) == True:
        interpreter.eval(on_true, env)
    else:
        interpreter.eval(on_false, env)

STDLIB_CORE = {
    "do": PythonFunction("do", _do, False),
    "var": PythonFunction("var", _var, False),
    "func": PythonFunction("func", _func, False),
    "print": PythonFunction("print", _print, True),
    "if": PythonFunction("if", _if, False),
    "include-file": PythonFunction("include-file", _include_file, True),
}