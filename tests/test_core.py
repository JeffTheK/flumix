from flumix.interpreter import exec_string

def test_print(capsys):
    exec_string("(print 10)")
    captured = capsys.readouterr()
    assert(captured.out == "10\n")

def test_do(capsys):
    code = """(do
    (print 1)
    (print 2)
    (print 3)
)
"""
    exec_string(code)
    captured = capsys.readouterr()
    assert(captured.out == "1\n2\n3\n")