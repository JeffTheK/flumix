Token = str

def tokenize(text: str) -> Token:
    return text.replace('(', ' ( ').replace(')', ' ) ').split()