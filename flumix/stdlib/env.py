from .core import STDLIB_CORE
from .operators import STDLIB_OPERATORS
from .oop import STDLIB_OOP
from .special import STDLIB_SPECIAL
from ..types import Env

STD_ENV: Env = Env(None)
STD_ENV.update(STDLIB_CORE),
STD_ENV.update(STDLIB_OPERATORS)
STD_ENV.update(STDLIB_OOP)
STD_ENV.update(STDLIB_SPECIAL)