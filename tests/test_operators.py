from flumix.interpreter import exec_string

def test_print(capsys):
    exec_string("(print (== 1 1))")
    captured = capsys.readouterr()
    assert(captured.out == "True\n")