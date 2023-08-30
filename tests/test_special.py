from flumix.cli import exec_file
from flumix.stdlib.list import List

def test_new_py_class(capsys):
    exec_file("tests/argv.fl", List(["hello", "world"]))
    captured = capsys.readouterr()
    assert(captured.out == "['hello', 'world']\n")