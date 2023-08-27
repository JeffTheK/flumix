from flumix.interpreter import exec_string

def test_plus(capsys):
    exec_string("(print (+ 1 1))")
    captured = capsys.readouterr()
    assert(captured.out == "2\n")

def test_minus(capsys):
    exec_string("(print (- 1 1))")
    captured = capsys.readouterr()
    assert(captured.out == "0\n")

def test_multiply(capsys):
    exec_string("(print (* 2 2))")
    captured = capsys.readouterr()
    assert(captured.out == "4\n")

def test_divide(capsys):
    exec_string("(print (/ 4 2))")
    captured = capsys.readouterr()
    assert(captured.out == "2.0\n")

def test_power(capsys):
    exec_string("(print (^ 4 2))")
    captured = capsys.readouterr()
    assert(captured.out == "16\n")

def test_eq(capsys):
    exec_string("(print (== 1 1))")
    captured = capsys.readouterr()
    assert(captured.out == "True\n")

    exec_string("(print (== 1 2))")
    captured = capsys.readouterr()
    assert(captured.out == "False\n")

def test_ne(capsys):
    exec_string("(print (!= 1 1))")
    captured = capsys.readouterr()
    assert(captured.out == "False\n")

    exec_string("(print (!= 1 2))")
    captured = capsys.readouterr()
    assert(captured.out == "True\n")