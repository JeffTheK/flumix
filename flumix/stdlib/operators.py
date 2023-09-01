from ..types import PythonFunction

STDLIB_OPERATORS = {
    "+": PythonFunction("+", lambda args, env: args[0] + args[1], True, ["a", "b"], description="Add"),
    "-": PythonFunction("-", lambda args, env: args[0] - args[1], True, ["a", "b"], description="Subtract"),
    "*": PythonFunction("*", lambda args, env: args[0] * args[1], True, ["a", "b"], description="Multiply"),
    "/": PythonFunction("/", lambda args, env: args[0] / args[1], True, ["a", "b"], description="Divide"),
    "^": PythonFunction("^", lambda args, env: args[0] ** args[1], True, ["a", "b"], description="Raise to the power of"),

    "==": PythonFunction("==", lambda args, env: args[0] == args[1], True, ["a", "b"], description="True if objects are equal"),
    "!=": PythonFunction("!=", lambda args, env: args[0] != args[1], True, ["a", "b"], description="True if objects are NOT equal"),
    ">": PythonFunction(">", lambda args, env: args[0] > args[1], True, ["a", "b"], description="True if greater then"),
    "<": PythonFunction("<", lambda args, env: args[0] < args[1], True, ["a", "b"], description="True if less then"),
    ">=": PythonFunction(">=", lambda args, env: args[0] >= args[1], True, ["a", "b"], description="True if greater or equal"),
    "<=": PythonFunction("<=", lambda args, env: args[0] <= args[1], True, ["a", "b"], description="True if less then or equal"),

    "not": PythonFunction("not", lambda args, env: not all(args), True, ["conditions..."], any_number_of_args=True, description="True if all conditions are false"),
    "and": PythonFunction("and", lambda args, env: all(args), True, ["conditions..."],  any_number_of_args=True, description="True if all conditions are true"),
    "or": PythonFunction("or", lambda args, env: any(args), True, ["conditions..."], any_number_of_args=True, description="True if any of condition is true"),
}