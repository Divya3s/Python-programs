# def _sum(arr):
#     sum = 0
#     for i in arr:
#         sum = sum + i
        
#     return(sum)


# if __name__ == "__main__":
#     arr = [12, 4, 6, 15]
    
#     n = len(arr)
    
#     ans = _sum(arr)
    
#     print('Sum of the array is', ans)



# ------------------------------------------------------------
# m=None
# print(type(m))


# ---------------------find largest number in an array---------------------------------------
# def largest(arr, n):
#     max = arr[0]

#     for i in range(1,n):
#         if arr[i] > max:
#             max = arr[i]
#     return max

# arr = [10, 22, 34, 11, 76,109, 3, 6]
# n=len(arr)

# print("largest number=", largest(arr, n))

# ------------------------------------------------------------
# list = [4,55,6,87,34,22,105,223,65,3]

# max = list[0]
# n = len(list)

# for i in range(1,n):
#   if list[i]>max:
#     max = list[i]

# print(max)
# -------------------sunm of elements of a list-----------------------------------------
# list1 = [56,7,88,45,6,34,89,44]

# sum = 0

# for i in list1:
#     sum=sum+i

# print(sum)
# ------------------------------------------------------------
# arr = [1,2,3,4,5,6,7,8,9,0]
# arrr = []
# n = len(arr)
# for i in range(n):
#     arrr.append(arr[-i-1])
# print(arrr)

# ------------1. ------------------------------------------------
# import array
# a = array.array('i',[5, 6, -7, 8])
# print('the array elements are:')
# for el in a:
#     print(el)
# ------2------------------------------------------------------
# from array import *
# a = array('i',[5, 6, -7, 8])
# for el in a:
#     print(el)
# -----3-------------------------------------------------------
# from array import *
# c = array('u', ['a','b','c','d','e'])
# for ch in c:
#     print(ch)
# ----4--------------------------------------------------------
# from array import *
# arr1 = array('d',[1.5, 3.4, 5.2, 5.0,3])
# arr2 = array(arr1.typecode, [a*3 for a in arr1])
# for i in arr2:
#     print(i)
# -------5-----------------------------------------------------
# from array import *
# x = array('i',[10, 20, 30, 40, 50, 60])
# n = len(x)

# for i in range(n):
#     print(x[i], end=' ')
# ------6------------------------------------------------------
# from array import *
# x = array('i',[10, 20, 30, 40, 50, 60])
# n = len(x)
# i = 0
# while i<n:
#     print(x[i], end=' ')
#     i+=1
# -7-----------------------------------------------------------
# from array import *
# x = array('i',[10, 20, 30, 40, 50, 60, 70])
# y = x[1:4]
# print(y)

# y = x[0:]
# print(y)

# y = x[:4]
# print(y)

# y = x[-4:]
# print(y)

# y = x[-4:-1]
# print(y)

# y = x[0:7:2]
# print(y)

# -------8-----------------------------------------------------
# from array import *
# x = array('i',[10, 20, 30, 40, 50, 60, 70])
# for i in x[2:5]:
#     print(i)
# ---9 methods of arrays---------------------------------------------------------
# from array import *
# x = array('i',[10, 20, 30, 40, 50, 60, 70])
# print(x)
# x.append(80)
# print(x)
# x.insert(0, 5)
# print(x)
# x.remove(20)
# print(x)
# x.pop()
# print(x)
# print(x.index(30))
# print(x)

# ----10--------------------------------------------------------
# from array import *
# lst = [int(i) for i in input('Enter marks').split(',')]
# marks = array('i', lst)
# sum = 0
# for x in marks:
#     print(x)
#     sum+=x
# print('total marks= ', sum)
# n = len(marks)
# percent = sum/n
# print('percent= ', percent)
# -------------swap values-----------------------------------------------
# a = 50
# b = 100

# t = 0

# print(a,b)

# t = a
# a = b
# b = t

# print(a, b)
# ----11--------------------------------------------------------

# ------12------------------------------------------------------

# ------13------------------------------------------------------

# ------14------------------------------------------------------
# import numpy
# arr = numpy.array([10, 20, 30, 40, 50, 60])
# print(arr)

# ------15------------------------------------------------------
# import numpy as np
# arr = np.array([10, 20, 30, 40, 50, 60])
# print(arr)
# ---16--------------------------------------------------------
# from numpy import *
# arr = array([10, 20, 30, 40, 50, 60])
# print(arr)
# ----17----18-----19-----------------------------------------------
# from numpy import *
# arr1 = array(['a','b','c','d','e'])
# print(arr1)
# arr2 = array(['apple','ball','cow','dog','elephant'])
# print(arr2)

# arr3 = array(arr2)
# arr4 = arr1

# print(arr3)
# print(arr4)
# -----20-------------------------------------------------------
# from numpy import *
# a = linspace(0, 10, 5) #divide 0 to 10 into 5 parts
# print(a)
# --------21----------------------------------------------------
# from numpy import *
# b = logspace(1, 4, 5)
# print(b)
# n = len(b)
# print(n)

# for i in range(n):
#     print('%.1f' %b[i], end=' ')
# ----22--------------------------------------------------------

# ------------------------------------------------------------

# ------------------------------------------------------------

# ------------------------------------------------------------

# ------------------------------------------------------------

# ------------------------------------------------------------

# ------------------------------------------------------------

# ------------------------------------------------------------

# ------------------------------------------------------------

# ------------------------------------------------------------

# ------------------------------------------------------------

# ------------------------------------------------------------

# ------------------------------------------------------------

# ------------------------------------------------------------

# ------------------------------------------------------------

# ------------------------------------------------------------

# ------------------------------------------------------------

# ------------------------------------------------------------

# ------------------------------------------------------------

# ------------------------------------------------------------

# ------------------------------------------------------------

# ------------------------------------------------------------

# ------------------------------------------------------------

# ------------------------------------------------------------

# ------------------------------------------------------------