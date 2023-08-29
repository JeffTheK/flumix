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
    
    def find_env(self, object):
        if object in self:
            return self
        elif self.outer != None:
            return self.outer.find_env(object)
        else:
            return None
    
    def global_env(self):
        if self.outer == None:
            return self
        else:
            return self.outer.global_env()
        
class Function:
    def __init__(self, name: Symbol, body, eval_args: bool, params=[], any_number_of_args=False) -> None:
        self.name = name
        self.body = body
        self.eval_args = eval_args
        self.params = params
        self.any_number_of_args = any_number_of_args
    
    def exec(self, args, env: Env):
        from . import interpreter
        for expr in self.body[:-1]:
            interpreter.eval(expr, env)
        return interpreter.eval(self.body[-1], env)

class PythonFunction(Function):
    def __init__(self, name: Symbol, body, eval_args: bool, params=[], any_number_of_args=False) -> None:
        super().__init__(name, body, eval_args, params, any_number_of_args)
    
    def exec(self, args, env: Env):
        return self.body(args, env)

class Class:
    def __init__(self, name, instance_variables) -> None:
        self.name = name
        self.instance_variables = instance_variables

class Instance:
    def __init__(self, _class, variables) -> None:
        self._class = _class
        self.variables = variables

String = str
Atom = (Symbol, Int, Float, String)
ListExpression = list
Expression = (Atom, ListExpression)