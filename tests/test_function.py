from flumix.interpreter import exec_string

def test_function_no_args(capsys):
    code = """(do 
    (func my-func ()
        (print 1)
        (print 2)
        (print 3)
    )
    (my-func)
)
"""
    exec_string(code)
    captured = capsys.readouterr()
    assert(captured.out == "1\n2\n3\n")

def test_function_with_args(capsys):
    code = """(do 
    (func my-func (a b c)
        (print a)
        (print b)
        (print c)
    )
    (my-func 1 2 3)
)
"""
    exec_string(code)
    captured = capsys.readouterr()
    assert(captured.out == "1\n2\n3\n")