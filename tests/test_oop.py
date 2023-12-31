from flumix.interpreter import exec_string

def test_plus(capsys):
    code = """(do
    (class person (name age))
    (print (*env-contains* "person"))
    (print (*env-contains* "person/new"))

    (var jeff (person/new "Jeff" 16))
    (print (getp name jeff))

    (setp name jeff "Jeffry")
    (print (getp name jeff))
)
"""
    exec_string(code)
    captured = capsys.readouterr()
    assert(captured.out == "True\nTrue\nJeff\nJeffry\n")