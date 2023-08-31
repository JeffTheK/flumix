import flumix
from flumix.stdlib import *
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
                output += "No description\n\n"
    
    return output

def generate_file(env, module: str):
    text = generate_markdown(env, module)
    path = os.path.join(OUTPUT_DIR, module + ".md")
    with open(path, "w") as file:
        file.write(text)

generate_file(STDLIB_CORE, "core")
generate_file(STDLIB_LIST, "list")
generate_file(STDLIB_LOOPS, "loops")
generate_file(STDLIB_OOP, "object oriented programming")
generate_file(STDLIB_OPERATORS, "operators")
generate_file(STDLIB_SPECIAL, "special")