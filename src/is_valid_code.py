import re

def is_valid_code(code):
    pattern = r'([0-9]{8}[-][0-9]{8}[-][C][0-9]{10}[-][A-Z])|([0-9]{8}[-][C][0-9]{10})|([A-Z]{2}[-][A-Z][-][0-9][A-Z][0-9]{2}[-][0-9])'
    match = re.search(pattern, code)
    
    
    if match:
        new_code = match.group()
        return new_code

      

