#--1--------------------------------------------------------------------------
# dict={'name':'chandra','id':200, 'salary':9080 }
# print('name of emloyee: ', dict['name'])
# print('id number: ', dict['id'])
# print('salary: ', dict['salary'])
#----2------------------------------------------------------------------------
# dict={'name':'chandra','id':200, 'salary':9080 }
# print(dict)
# print('keys in dict = ', dict.keys())
# print('values in dict = ', dict.values())
# print('values in dict = ', dict.items())
#---3-------------------------------------------------------------------------
# # dict = eval(input("Enter elements in {}: "))
# dict={'value':555,'id':200, 'salary':9080 }
# s = sum(dict.values())
# print('Sum of values in the dictionary: ', s)

#---4-------------------------------------------------------------------------
# x = {}
# print('How many elements? ', end=' ')
# n=int(input())
# for i in range(n):
#     print('Enter key:', end=' ')
#     k = input()
#     print('Enter its value: ', end=' ')
#     v = int(input())
#     x.update({k:v})
# print('The Dictionary is: ', x)
#-----5-----------------------------------------------------------------------
# x = {}
# print('How many players?', end=' ')
# n = int(input())

# for i in range(n):
#     print('enter player name:', end=' ')
#     k=input()
#     print('enter runs: ', end=' ')
#     v = int(input())
#     x.update({k:v})

# print('players in this match: ', )
# for pname in x.keys():
#     print(pname)

# print('enter player name:', end=' ')
# name=input()
# runs=x.get(name, -1)
# if (runs==-1):
#     print('player not found.')

# else:
#     print('{} made {} runs.'.format(name, runs))
#---6----for loop with dictionary---------------------------------------------------------------------
# colours={'r':"red", 'y':"yellow",'g':"green",'b':"blue"}

# for k in colours:
#     print(k)

# for k in colours:
#     print(colours[k])

# for k, v in colours.items():
#     print('key={} value={}'.format(k, v))
#----7 find number of occurence of each letter in a string using dictionary--------------------------
# str = "find number of occurence of each letter in a string using dictionary"
# dict={}
# for x in str:
#     dict[x]=dict.get(x, 0)+1

# for k, v in dict.items():
#     print('key = {}\t its occurance = {}'.format(k, v))
#------8 sort elements of the dictionary----------------------------------------------------------------------
# colours = {10:'red', 35:'green', 15:'blue', 25:'white'}
# c1 = sorted(colours.items(), key=lambda t:t[0])
# print(c1)

# c2 = sorted(colours.items(), key=lambda t: t[1])
# print(c2)
#----9 two lists into a key value dictionary------------------------------------------------------------------------
# l1 = ['1', '2', '3', '4', '5']
# l2 = ['a', 'b', 'c', 'd', 'e']
# z = zip(l1, l2)
# d = dict(z)

# print('{:1s} -- {:1s}'.format('l1', 'l2'))

# for k in d:
#     print('{:1s} -- {:1s}'.format(k, d[k]))

#----10------------------------------------------------------------------------
str = "vijay=23, ganesh=20, lakshmi=19, nikhil=22"

lst=[]
for x in str.split(','):
    y=x.split('=')
    lst.append(y)

d=dict(lst)
d1={}
for k, v in d.items():
    d1[k]=int(v)

print(d1)
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

