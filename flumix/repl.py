from . import interpreter

def repl_loop():
    while True:
        string = input("flumix > ")
        try:
            print(interpreter.exec_string(string))
        except Exception as e:
            print(e.with_traceback)