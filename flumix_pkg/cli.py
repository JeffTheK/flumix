import sys
import os
from .template.package_json import PKG_JSON_TEXT
from .template.main_fl import MAIN_FL_TEXT

class Package:
    def __init__(self, name, type) -> None:
        self.name = name
        self.type = type

def main():
    exec(sys.argv)

def exec(args: "list[str]"):
    command = args[1]

    if command == "new":
        name = args[2]
        type = "library"
        if args.count("--lib") > 0:
            type = "library"
        elif args.count("--exe") > 0:
            type = "executable"
        pkg = Package(name, type)
        new_package(pkg)

def create_file_from_template(template_text, file_path, pkg: Package):
    template_text = template_text.replace("$PKG_NAME", pkg.name)
    template_text = template_text.replace("$PKG_TYPE", pkg.type)
    with open(file_path, "w") as file:
        file.write(template_text)

def new_package(pkg: Package):
    SRC_DIR = os.path.join(pkg.name, "src")
    PKG_DIRS = [pkg.name, SRC_DIR]
    for dir in PKG_DIRS:
        os.mkdir(dir)
    create_file_from_template(PKG_JSON_TEXT, os.path.join(pkg.name, "package.json"), pkg)
    create_file_from_template(PKG_JSON_TEXT, os.path.join(SRC_DIR, "main.fl"), pkg)