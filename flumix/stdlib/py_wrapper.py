from ..types import Function, PythonFunction, Class
from .. import interpreter
import sys

class PyClassWrapper:
    def __init__(self, python_class):
        self.python_class = python_class
    
    def __repr__(self) -> str:
        return str(self.python_class)

def new_py_class_wrapper(args, env):
    wrapper_name = args[0]
    python_class_name = args[1]
    python_class = eval(python_class_name) # FIXME: a bit hackish and unsafe
    env.outer[wrapper_name] = PyClassWrapper(python_class)

def new_py_class_instance(args, env):
    _class_name = args[0]
    init_args = args[1]
    _class = env.find(_class_name)
    instance = _class.python_class(*init_args)
    return instance

def call_method(args, env):
    method_name = args[0]
    instance_name = args[1]
    method_args = args[2]
    instance = interpreter.eval(instance_name, env)
    method = getattr(instance, method_name)
    method(*method_args)

def py_eval_string(args, env):
    return eval(args[0])

STDLIB_PY_WRAPPER = {
    "py-wrapper/new-py-class-wrapper": PythonFunction("py-wrapper/new-py-class-wrapper", new_py_class_wrapper, False),
    "py-wrapper/new-py-class-instance": PythonFunction("py-wrapper/new-py-class-instance", new_py_class_instance, False),
    "py-wrapper/call-method": PythonFunction("py-wrapper/call-method", call_method, False),
    "py-wrapper/py-eval": PythonFunction("py-wrapper/py-eval", py_eval_string, True)
}