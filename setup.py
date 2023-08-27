from setuptools import setup, find_packages

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
        ],
    }
)