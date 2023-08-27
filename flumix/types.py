class Symbol(str):
    def __new__(cls, *args, **kw):
        return super().__new__(cls, *args, **kw)

class Int(int):
    def __new__(cls, *args, **kw):
        return super().__new__(cls, *args, **kw)

class Float(float):
    def __new__(cls, *args, **kw):
        return super().__new__(cls, *args, **kw)

class Env(dict):
    def __init__(self, outer: dict, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.outer = outer
    
    def find(self, object):
        if object in self:
            return self[object]
        elif self.outer != None:
            return self.outer.find(object)
        else:
            return None
        
class Function:
    def __init__(self, name: Symbol, body, eval_args: bool, params=[]) -> None:
        self.name = name
        self.body = body
        self.eval_args = eval_args
        self.params = params
    
    def exec(self, args, env: Env):
        from . import interpreter
        for expr in self.body[:-1]:
            interpreter.eval(expr, env)
        return interpreter.eval(self.body[-1], env)

class PythonFunction(Function):
    def __init__(self, name: Symbol, body, eval_args: bool) -> None:
        super().__init__(name, body, eval_args)
    
    def exec(self, args, env: Env):
        return self.body(args, env)

String = str
Atom = (Symbol, Int, Float, String)
List = list
Expression = (Atom, List)