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
    def __init__(self, name: Symbol, body) -> None:
        self.name = name
        self.body = body
    
    def exec(self, args, env: Env):
        pass

class PythonFunction(Function):
    def __init__(self, name: Symbol, body) -> None:
        super().__init__(name, body)
    
    def exec(self, args, env: Env):
        self.body(args, env)

Atom = (Symbol, Int, Float)
List = list
Expression = (Atom, List)