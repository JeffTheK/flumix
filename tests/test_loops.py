from flumix.interpreter import exec_string

def test_function_no_args(capsys):
    code = """(do 
    (for (var i 0) (< i 5) (set i (+ i 1))
        (print i)
    )
)
"""
    exec_string(code)
    captured = capsys.readouterr()
    assert(captured.out == "1\n2\n3\n4\n5\n")