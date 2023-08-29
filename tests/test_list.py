from flumix.interpreter import exec_string

def test_function_no_args(capsys):
    code = """(do 
    (print (list/new 1 2 3 4 5))
)
"""
    exec_string(code)
    captured = capsys.readouterr()
    assert(captured.out == "[1, 2, 3, 4, 5]\n")