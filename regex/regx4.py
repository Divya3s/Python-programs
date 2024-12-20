import re

""" reg = r'm\w\w'
nor = 'm\\w\\w'
print(reg)
print(nor)

str = 'this is normal \nstring'
print(str)

rstr = r'this is raw \nstring'
print(rstr)
 """
# ------------------------------------------
""" prog = re.compile(r'm\w\w')
str = 'cat mat bat rat'
result = prog.search(str)
print(result.group()) """

# ------------------------------------------

""" str = 'cat mat bat rat'
res = re.search(r'm\w\w', str)
print(res.group()) """

# ------------------------------------------

""" str = 'man sun mop run'
result = re.search(r'm\w\w',str)
if result is not None:
    print(result.group()) """
# ------------------------------------------
""" str = 'man sun mop run'
result = re.findall(r'm\w\w',str)
if result is not None:
    print(result) """
# ------------------------------------------
""" str = 'man sun mop run'
result = re.findall(r'm\w\w',str)
if result is not None:
    for s in result:
        print(s) """
# ------------------------------------------
""" str = 'man sun mop run'
result = re.match(r'm\w\w',str)
print(result.group()) """
# ------------------------------------------
""" str = 'sun man mop run'
result = re.match(r'm\w\w',str)
print(result) """
# ------------split------------------------------
""" str = 'this is a string'
print(re.split(r'\W+',str)) """
# ---------replace string---------------------------------
""" str = 'this iz a string'
print(re.sub(r'z','s',str)) """
# ------retrieve all words starting with a------------------------------------
""" str = 'an apple a day keeps doctors away'
result = re.findall(r'\ba[\w]*\b', str)
for word in result:
    print(word) """
# ------------------------------------------

# ------------------------------------------

# ------------------------------------------

# ------------------------------------------

# ------------------------------------------

# ------------------------------------------

# ------------------------------------------

# ------------------------------------------

# ------------------------------------------

# ------------------------------------------

# ------------------------------------------

# ------------------------------------------

# ------------------------------------------

# ------------------------------------------

# ------------------------------------------

# ------------------------------------------

# ------------------------------------------

# ------------------------------------------

# ------------------------------------------

