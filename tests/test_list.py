from flumix.interpreter import exec_string

def test_new(capsys):
    code = """(do 
    (print (list/new 1 2 3 4 5))
)
"""
    exec_string(code)
    captured = capsys.readouterr()
    assert(captured.out == "[1, 2, 3, 4, 5]\n")

def test_get_at(capsys):
    code = """(do 
    (var l (list/new 1 2 3 4 5))
    (print (list/get-at l 0))
    (print (list/get-at l 1))
    (print (list/get-at l -1))
)
"""
    exec_string(code)
    captured = capsys.readouterr()
    assert(captured.out == "1\n2\n5\n")

def test_set_at(capsys):
    code = """(do 
    (var l (list/new 1 2 3 4 5))
    (list/set-at l 2 99)
    (print (list/get-at l 2))
)
"""
    exec_string(code)
    captured = capsys.readouterr()
    assert(captured.out == "99\n")