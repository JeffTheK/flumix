from .types import Expression, Env, Symbol, Float, Int, Function, PythonFunction, String
from . import lexer
from . import parser
from .stdlib.env import STD_ENV
from .error import raise_error

def function_call(expression: Expression, env: Env):
    function: Function = eval(expression[0], env)
    
    args = expression[1:]
    if function.eval_args:
        for x in range(len(args)):
            args[x] = eval(args[x], env)

    local_env = Env(env)
    for i in range(len(function.params)):
            local_env[function.params[i]] = args[i]
    
    return function.exec(args, local_env)

def is_variable_reference(expression: Expression):
    return isinstance(expression, Symbol)

def is_atom(expression: Expression):
    return isinstance(expression, Float) or isinstance(expression, Int) or isinstance(expression, String)

def analyze(expression: Expression, env: Env):
    if is_variable_reference(expression):
        variable = env.find(expression)
        if variable is None:
            raise_error("Interpreter", f"variable '{expression}' not found")
    elif is_atom(expression):
        pass
    else:
        function_symbol = expression[0]
        if env.find(function_symbol) is None:
            raise_error("Interpreter", f"function '{expression}' not defined")
        args = expression[1:]
        function: Function = env.find(function_symbol)
        if (not function.any_number_of_args) and len(args) != len(function.params):
            raise_error("Interpreter", f"wrong number of arguments when calling '{function_symbol}', expected {len(function.params)} got {len(args)}")

def eval(expression: Expression, env: Env):
    analyze(expression, env)

    if is_variable_reference(expression):
        return env.find(expression)
    elif is_atom(expression):
        return expression
    else:
        return function_call(expression, env)

def exec_string(string: str, env=STD_ENV):
    tokens = lexer.tokenize(string)
    expression = parser.parse_tokens(tokens)
    return eval(expression, STD_ENV)