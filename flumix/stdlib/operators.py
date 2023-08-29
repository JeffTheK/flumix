from ..types import PythonFunction

STDLIB_OPERATORS = {
    "+": PythonFunction("+", lambda args, env: args[0] + args[1], True, ["a", "b"]),
    "-": PythonFunction("-", lambda args, env: args[0] - args[1], True, ["a", "b"]),
    "*": PythonFunction("*", lambda args, env: args[0] * args[1], True, ["a", "b"]),
    "/": PythonFunction("/", lambda args, env: args[0] / args[1], True, ["a", "b"]),
    "^": PythonFunction("^", lambda args, env: args[0] ** args[1], True, ["a", "b"]),

    "==": PythonFunction("==", lambda args, env: args[0] == args[1], True, ["a", "b"]),
    "!=": PythonFunction("!=", lambda args, env: args[0] != args[1], True, ["a", "b"]),
    ">": PythonFunction(">", lambda args, env: args[0] > args[1], True, ["a", "b"]),
    "<": PythonFunction("<", lambda args, env: args[0] < args[1], True, ["a", "b"]),
    ">=": PythonFunction(">=", lambda args, env: args[0] >= args[1], True, ["a", "b"]),
    "<=": PythonFunction("<=", lambda args, env: args[0] <= args[1], True, ["a", "b"]),

    "not": PythonFunction("not", lambda args, env: not all(args), True, any_number_of_args=True),
    "and": PythonFunction("and", lambda args, env: all(args), True, any_number_of_args=True),
    "or": PythonFunction("or", lambda args, env: any(args), True, any_number_of_args=True),
}