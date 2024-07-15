import re

def is_valid_code(code):

    if 'O' in code or 'o' in code:
        code_upper = code.upper()
        code = code_upper.replace('O', '0')

    pattern = r'([0-9]{8}[-][0-9]{8}[-][C][0-9]{10}[-][A-Z])|([0-9]{8}[-][C][0-9]{10})|([A-Z]{2}[-][A-Z][-][0-9][A-Z][0-9]{2}[-][0-9])'
    match = re.search(pattern, code)
    
    if match:
        new_code = match.group()
        return new_code

      

