from ..types import PythonFunction

STDLIB_OPERATORS = {
    "+": PythonFunction("+", lambda args, env: args[0] + args[1], True),
    "-": PythonFunction("-", lambda args, env: args[0] - args[1], True),
    "*": PythonFunction("*", lambda args, env: args[0] * args[1], True),
    "/": PythonFunction("/", lambda args, env: args[0] / args[1], True),
    "^": PythonFunction("^", lambda args, env: args[0] ** args[1], True),

    "==": PythonFunction("==", lambda args, env: args[0] == args[1], True),
    "!=": PythonFunction("!=", lambda args, env: args[0] != args[1], True),

    "not": PythonFunction("not", lambda args, env: not all(args), True),
    "and": PythonFunction("and", lambda args, env: all(args), True),
    "or": PythonFunction("or", lambda args, env: any(args), True),
}