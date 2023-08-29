from .core import STDLIB_CORE
from .operators import STDLIB_OPERATORS
from .oop import STDLIB_OOP
from .loops import STDLIB_LOOPS
from .special import STDLIB_SPECIAL
from .py_wrapper import STDLIB_PY_WRAPPER
from .list import STDLIB_LIST
from ..types import Env

STD_ENV: Env = Env(None)
STD_ENV.update(STDLIB_CORE)
STD_ENV.update(STDLIB_OPERATORS)
STD_ENV.update(STDLIB_OOP)
STD_ENV.update(STDLIB_LOOPS)
STD_ENV.update(STDLIB_SPECIAL)
STD_ENV.update(STDLIB_PY_WRAPPER)
STD_ENV.update(STDLIB_LIST)