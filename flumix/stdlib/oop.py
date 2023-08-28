from ..types import Function, PythonFunction, Class, Instance
from .. import interpreter

def constructor(args, env, _class):
    variable_values = args[0]
    variable_names = _class.instance_variables
    variables = {}
    for x in range(len(variable_values)):
        variables[variable_names[x]] = variable_values[x]

    instance = Instance(_class, variables)
    return instance

def create_constructor(_class, env):
    func_name = f"{_class.name}/new"
    env.outer[func_name] = PythonFunction(func_name, lambda a, e, c=_class: constructor(a, e, c), False)

def define_class(args, env):
    name = args[0]
    instance_variables = []
    for v in args[1]:
        instance_variables.append(v)
    _class = Class(name, instance_variables)
    env.outer[name] = _class
    create_constructor(_class, env)

def get_property(args, env):
    property_name = args[0]
    instance_name = args[1]
    instance: Instance = env.find(instance_name)
    property = instance.variables[property_name]
    return property

STDLIB_OOP = {
    "class": PythonFunction("class", define_class, False),
    "getp": PythonFunction("getp", get_property, False),
}