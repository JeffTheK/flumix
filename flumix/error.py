def source_code_error_showcase(line: int, source_code: str):
    lines = source_code.split('\n')
    line_string = lines[line]
    message = f"\t{str(line)} | {line_string} <-- error here"
    print()
    print(message)

def raise_error(type: str, message: str, line: int=None, file_name: str=None, source_code: str=None):
    full_message = f"[{type}]"
    if file_name is not None:
        full_message += f" in {file_name} "
    if line is not None:
        full_message += f" on line {str(line)} "
    full_message += f"Error: {message}"
    print(full_message)

    if source_code is not None and line is not None:
        source_code_error_showcase(line, source_code)

    exit(1)