from ..types import Function, PythonFunction, Class
from .. import interpreter

def env_contains(args, env):
    return env.find(args[0]) != None

STDLIB_SPECIAL = {
    "special/env-contains": PythonFunction("special/env-contains", env_contains, False),
}