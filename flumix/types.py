class Symbol(str):
    def __new__(cls, *args, **kw):
        return super().__new__(cls, *args, **kw)

class Int(int):
    def __new__(cls, *args, **kw):
        return super().__new__(cls, *args, **kw)

class Float(float):
    def __new__(cls, *args, **kw):
        return super().__new__(cls, *args, **kw)

Env = dict

class Function:
    def __init__(self, name: Symbol, body, eval_args: bool, params=[]) -> None:
        self.name = name
        self.body = body
        self.eval_args = eval_args
        self.params = params
    
    def exec(self, args, env: Env):
        for i in range(len(self.params)):
            env[self.params[i]] = args[i]

        from . import interpreter
        for expr in self.body[:-1]:
            interpreter.eval(expr, env)
        return interpreter.eval(self.body[-1], env)

class PythonFunction(Function):
    def __init__(self, name: Symbol, body, eval_args: bool) -> None:
        super().__init__(name, body, eval_args)
    
    def exec(self, args, env: Env):
        return self.body(args, env)

Atom = (Symbol, Int, Float)
List = list
Expression = (Atom, List)