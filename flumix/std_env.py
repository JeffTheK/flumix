from .types import PythonFunction

def _print(args, env):
    for a in args:
        print(a)

STD_ENV = {
    "print": PythonFunction("print", _print)
}