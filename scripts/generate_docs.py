import flumix
from flumix.stdlib import STDLIB_MODULES
from flumix.types import PythonFunction
import os

OUTPUT_DIR = os.path.join("docs", "_docs", "stdlib")

def generate_markdown(env, module: str):
    output = f"""---
title: "{module.capitalize()}"
description: "{module.capitalize()} functions and variables"
---

# {module.capitalize()}

"""

    for value in env.values():
        if isinstance(value, PythonFunction):
            output += f"### {value.name}\n"
            output += "\n"
            output += "```lisp\n"
            output += f"({value.name}"
            for param in value.params:
                output += f" {param}"
            output += ")\n"
            output += "```\n"
            if value.description != "":
                output += "\n"
                output += f"{value.description}\n"
                output += "\n"
            else:
                print(f"{module}/{value.name} has no description")
                output += "No description\n\n"
    
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