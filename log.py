
def log_code(code_type, string):
    return_text = '['
    return_text += code_type
    return_text += '] '
    return_text += string
    print(return_text)


def debug(string):
    log_code('DEBUG', string)


def error(string):
    log_code('ERROR', string)


def info(string):
    log_code('INFO', string)


def warning(string):
    log_code('WARNING', string)
