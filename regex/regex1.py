import re

def check(str, pattern):
    if re.search(pattern, str):
        print("valid String")
    else:
        print("Invalid string")
        
pattern = re.compile('^[1234]+$')

check('2134', pattern)
check('349', pattern)