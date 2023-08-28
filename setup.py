from setuptools import setup, find_packages
import atexit
import os
import shutil

setup(
    name="flumix",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        # List any dependencies here
    ],
    entry_points={
        'console_scripts': [
            'flumix = flumix.cli:main',
            'fl-to-cpp = fl_to_cpp.cli:main'
        ],
    }
)

home_directory = os.path.expanduser("~")
DATA_DIR = os.path.join(home_directory, ".flumix")
PKG_DIR = os.path.join(DATA_DIR, "pkg")
STDLIB_PKG_DIR = os.path.join(PKG_DIR, "stdlib")
DIRS = [DATA_DIR, PKG_DIR, STDLIB_PKG_DIR]
STDLIB_PACKAGE_SOURCE_FILES = ["tk.fl", "operators.fl"]

def create_directories():
    for dir in DIRS:
        if not os.path.exists(dir):
            os.makedirs(dir)

def copy_stdlib_package():
    for file in STDLIB_PACKAGE_SOURCE_FILES:
        shutil.copy(os.path.join("flumix", "stdlib", file), os.path.join(STDLIB_PKG_DIR, file))

atexit.register(create_directories)
atexit.register(copy_stdlib_package)