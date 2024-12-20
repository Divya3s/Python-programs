li = [1,44, 5, 66, 98,43, 22, 109,7, 88]

def maximum(*args):
    max = li[0]
    for i in li:
        if i > max:
            max = i
    return max

ml = maximum(li)
print(ml)

def minimum(*args):
    min = li[0]
    for i in li:
        if i<min:
            min = i
    return min
mn = minimum(li)
print(mn)

def addall(*args):
    sum = 0
    for i in li:
        sum = sum+i
    return sum

print(addall(li))

def average(*args):
    add = 0
    for i in li:
        add = add+i
    avg = add/len(li)
    return avg

print(average(li))