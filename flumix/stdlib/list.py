from ..types import Function, PythonFunction, Class
from .. import interpreter
from .core import _var

class List(list):
    def __init__(self, *args):
        super().__init__(*args)

def _list_new(args, env):
    return List(args)

STDLIB_LIST = {
    "list/new": PythonFunction("list/new", _list_new, True, [], any_number_of_args=True),
}