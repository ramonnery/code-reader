import re

def is_valid_code(code):
    pattern = r'(\d{8}-\d{8}-C\d{10}-[A-Za-z])|(\d{6,8}-C\d{10}-[A-Za-z])'
    return bool(re.match(pattern, code))
    