from ..types import PythonFunction

STDLIB_OPERATORS = {
    "==": PythonFunction("==", lambda args, env: args[0] == args[1], True),
}