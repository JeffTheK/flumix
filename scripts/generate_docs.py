import flumix
from flumix.stdlib import STDLIB_MODULES, STD_ENV
from flumix.types import PythonFunction
from flumix import interpreter
from contextlib import redirect_stdout
import os
import io

OUTPUT_DIR = os.path.join("docs", "_docs", "stdlib")
EXAMPLES_DIR = os.path.join("docs", "examples")

def generate_example(env, module: str, value: str):
    output = ""
    # example
    example_file_path = os.path.join(EXAMPLES_DIR, module, value.name.replace('/', '-') + '.fl')
    if os.path.exists(example_file_path):
        output += "##### Example\n"
        code = open(example_file_path, 'r').read()
        result = ""
        out = io.StringIO()
        with redirect_stdout(out):
            result += str(interpreter.exec_string(code, STD_ENV)) + "\n"
            if result == "None\n":
                result = ""
        result += out.getvalue()
        output += f"""```lisp
{code}
--> {result}
```
"""
    return output

def generate_markdown(env, module: str):
    output = f"""---
title: "{module.capitalize()}"
description: "{module.capitalize()} functions and variables"
---

# {module.capitalize()}

## Table

"""

    functions = sorted(env.values(), key=lambda obj: obj.name)

    for value in functions:
        if isinstance(value, PythonFunction):
            output += f"[`({value.name})`](#{value.name})  "
    output += "\n"

    for value in functions:
        if isinstance(value, PythonFunction):
            output += f"## `({value.name}"
            for param in value.params:
                output += f" {param}"
            output += ")`\n"
            output += f'<a id="{value.name}"></a>\n'
            if value.description != "":
                output += "```\n"
                output += f"{value.description}\n"
                output += "```\n"
            else:
                print(f"{module}/{value.name} has no description")
                output += "```\nNo description\n```\n\n"
            output += generate_example(env, module, value)
            output += "<br>\n"
    
    return output

def generate_file(env, module: str):
    text = generate_markdown(env, module)
    path = os.path.join(OUTPUT_DIR, module + ".md")
    with open(path, 'w') as file:
        file.write(text)

def generate_toc(modules: "list[str]"):
    path = os.path.join("docs", "_data", "toc.yml")
    modules_text = ""
    for module in modules:
        modules_text += f'        - title: "{module.capitalize()}"\n'
        modules_text += f'          url: "docs/stdlib/{module}"\n'

    text = f"""- title: Documentation
  url: docs
  links:
    - title: "Installation"
      url: "docs/installation"
    - title: "Standard Library"
      children:
{modules_text}
    - title: "About"
      url: "about"

"""
    with open(path, 'w') as file:
        file.write(text)

for name, value in STDLIB_MODULES.items():
    generate_file(value, name)

generate_toc(STDLIB_MODULES.keys())