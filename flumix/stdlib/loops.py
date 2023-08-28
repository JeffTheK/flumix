from ..types import Function, PythonFunction, Class
from .. import interpreter
from .core import _var

def _for(args, env):
    _var(args[0][1:], env)
    condition = args[1]
    increment = args[2]
    action = args[3]
    while interpreter.eval(condition, env) == True:
        interpreter.eval(increment, env)
        interpreter.eval(action, env)

STDLIB_LOOPS = {
    "for": PythonFunction("for", _for, False),
}