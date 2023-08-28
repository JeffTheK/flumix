from flumix.interpreter import exec_string

def test_new_py_class(capsys):
    code = """(do
    (py-wrapper/new-py-class-wrapper plist list)
    (var list1 (py-wrapper/new-py-class-instance plist ()))
    (print plist)
    (print list1)
    (py-wrapper/call-method append list1 (1))
    (print list1)
)
"""
    exec_string(code)
    captured = capsys.readouterr()
    assert(captured.out == "<class 'list'>\n[]\n[1]\n")