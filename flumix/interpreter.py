from .types import Expression, Env, Symbol, Float, Int, Function, String
from . import lexer
from . import parser
from .stdlib.env import STD_ENV

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

def eval(expression: Expression, env: Env):
    if isinstance(expression, Symbol):
        return env.find(expression)
    elif isinstance(expression, Float) or isinstance(expression, Int) or isinstance(expression, String):
        return expression
    else:
        return function_call(expression, env)

def exec_string(string: str, env=STD_ENV):
    tokens = lexer.tokenize(string)
    expression = parser.parse_tokens(tokens)
    return eval(expression, STD_ENV)