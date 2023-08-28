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

def test_var(capsys):
    code = """(do
    (var a 1)
    (print a)
)
"""
    exec_string(code)
    captured = capsys.readouterr()
    assert(captured.out == "1\n")

def test_include_file(capsys):
    code = """(do
    (include-file "tests/testfile.fl")
    (print (my-add 2 3))
)
"""
    exec_string(code)
    captured = capsys.readouterr()
    assert(captured.out == "5\n")

def test_if_true(capsys):
    code = """(do
    (if (== 1 1)
        (print "yes")
        (print "no")
    )
)
"""
    exec_string(code)
    captured = capsys.readouterr()
    assert(captured.out == "yes\n")

def test_if_false(capsys):
    code = """(do
    (if (== 2 1)
        (print "yes")
        (print "no")
    )
)
"""
    exec_string(code)
    captured = capsys.readouterr()
    assert(captured.out == "no\n")

def test_if_no_else(capsys):
    code = """(do
    (if (== 1 1)
        (print "yes")
        ()
    )
)
"""
    exec_string(code)
    captured = capsys.readouterr()
    assert(captured.out == "yes\n")