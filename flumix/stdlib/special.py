from ..types import Function, PythonFunction, Class
from .. import interpreter

def env_contains(args, env):
    return env.find(args[0]) != None

def global_env(args, env):
    return env.global_env()

STDLIB_SPECIAL = {
    "special/global-env": PythonFunction("special/global-env", global_env, False),
    "special/env-contains": PythonFunction("special/env-contains", env_contains, False, ["object"])
}