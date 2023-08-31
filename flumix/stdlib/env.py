from .core import STDLIB_CORE
from .operators import STDLIB_OPERATORS
from .oop import STDLIB_OOP
from .loops import STDLIB_LOOPS
from .special import STDLIB_SPECIAL
from .py_wrapper import STDLIB_PY_WRAPPER
from .list import STDLIB_LIST
from ..types import Env

STDLIB_MODULES = {
    "core": STDLIB_CORE,
    "operators": STDLIB_OPERATORS,
    "object-oriented-programming": STDLIB_OOP,
    "loops": STDLIB_LOOPS,
    "special": STDLIB_SPECIAL,
    "py-wrapper": STDLIB_PY_WRAPPER,
    "list": STDLIB_LIST
}

STD_ENV: Env = Env(None)

for module in STDLIB_MODULES.values():
    STD_ENV.update(module)