from ..types import Function, PythonFunction, Class
from .. import interpreter

def env_contains(args, env):
    return env.find(args[0]) != None

def global_env(args, env):
    return env.global_env()

STDLIB_SPECIAL = {
    "*global-env*": PythonFunction("*global-env*", global_env, False),
    "*env-contains*": PythonFunction("*env-contains*", env_contains, False, ["object"])
}