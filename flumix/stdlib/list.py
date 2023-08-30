from ..types import Function, PythonFunction, Class
from .. import interpreter
from .core import _var

class List(list):
    def __init__(self, *args):
        super().__init__(*args)

def _list_new(args, env):
    return List(args)

def _get_at(args, env):
    list = args[0]
    index = args[1]
    return list[index]

def _set_at(args, env):
    list = args[0]
    index = args[1]
    value = args[2]
    list[index] = value

STDLIB_LIST = {
    "list/new": PythonFunction("list/new", _list_new, True, [], any_number_of_args=True),
    "list/get-at": PythonFunction("list/get-at", _get_at, True, ["list", "index"]),
    "list/set-at": PythonFunction("list/set-at", _set_at, True, ["list", "index", "value"])
}