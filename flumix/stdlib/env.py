from .core import STDLIB_CORE
from .operators import STDLIB_OPERATORS
from ..types import Env

STD_ENV: Env = Env(None)
STD_ENV.update(STDLIB_CORE),
STD_ENV.update(STDLIB_OPERATORS)