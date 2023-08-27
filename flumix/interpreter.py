from .types import Expression, Env, Symbol, Float, Int, Function
from . import lexer
from . import parser
from .stdlib.env import STD_ENV

def _if(expression: Expression, env: Env):
    condition = expression[1]
    on_true = expression[2]
    on_false = expression[3]
    if eval(condition, env) == True:
        return eval(on_true, env)
    else:
        return eval(on_false, env)

def function_call(expression: Expression, env: Env):
    function: Function = eval(expression[0], env)
    
    args = expression[1:]
    if function.eval_args:
        for x in range(len(args)):
            args[x] = eval(args[x], env)
    
    return function.exec(args, env)

def eval(expression: Expression, env: Env):
    if isinstance(expression, Symbol):
        return env[expression]
    elif isinstance(expression, Float) or isinstance(expression, Int):
        return expression
    else:
        function_call(expression, env)

def exec_string(string: str, env=STD_ENV):
    tokens = lexer.tokenize(string)
    expression = parser.parse_tokens(tokens)
    eval(expression, STD_ENV)