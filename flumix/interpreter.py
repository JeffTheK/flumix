from .types import Expression, Env, Symbol, Float, Int, Function

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
    args = []
    for x in expression[1:]:
        args.append(eval(x, env))
    
    return function.exec(args, env)

def eval(expression: Expression, env: Env):
    if isinstance(expression, Symbol):
        return env[expression]
    elif isinstance(expression, Float) or isinstance(expression, Int):
        return expression
    elif expression[0] == "if":
        _if(expression, env)
    else:
        function_call(expression, env)