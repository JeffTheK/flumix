from ..types import Function, PythonFunction, Class
from .. import interpreter
import sys
import importlib

class PyClassWrapper:
    def __init__(self, python_class):
        self.python_class = python_class
    
    def __repr__(self) -> str:
        return str(self.python_class)

def new_py_class_wrapper(args, env):
    wrapper_name = args[0]
    python_class_name = args[1]
    python_class = eval(python_class_name) # FIXME: a bit hackish and unsafe
    constructor_function_name = f"{wrapper_name}/new"
    env.global_env()[wrapper_name] = PyClassWrapper(python_class)
    env.global_env()[constructor_function_name] = PythonFunction(constructor_function_name, lambda a, e, cl=python_class: python_class(), False)

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

def py_import_module(args, env):
    module_name = args[0]
    module = importlib.import_module(module_name)
    globals()[module_name] = module

STDLIB_PY_WRAPPER = {
    "py-wrapper/new-class-wrapper": PythonFunction("py-wrapper/new-class-wrapper", new_py_class_wrapper, False, ["wrapper-name", "python-class-name"]),
    "py-wrapper/new-instance": PythonFunction("py-wrapper/new-instance", new_py_class_instance, False, ["class-name", "init-args"]),
    "py-wrapper/call-method": PythonFunction("py-wrapper/call-method", call_method, False, ["method-name", "instance-name", "method-args"]),
    "py-wrapper/eval": PythonFunction("py-wrapper/eval", py_eval_string, True, ["string"]),
    "py-wrapper/import": PythonFunction("py-wrapper/import", py_import_module, True, ["module-name"]),
}