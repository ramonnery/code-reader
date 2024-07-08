from datetime import datetime

def to_name(code):
    today = datetime.now().strftime('%Y%m%d')
    seconds = datetime.now().time().strftime("%S")
    new_code = f'{code}-{today}-100{seconds}'
    
    return new_code

