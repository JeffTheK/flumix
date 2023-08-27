from .core import STDLIB_CORE
from .operators import STDLIB_OPERATORS

STD_ENV = {
    **STDLIB_CORE,
    **STDLIB_OPERATORS
}