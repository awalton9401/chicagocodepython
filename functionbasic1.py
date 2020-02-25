# # -*- coding: utf-8 -*-

# 1
def a():
    return 5
print(a())

# # prediction 5

# #2
# def a():
#     return 5
# print(a()+a())

# # prediction 10

# #3
# def a():
#     return 5
#     return 10
# print(a())

# # prediction 5, 10 // answer is 5. only can have one return statement. code will exucute first return statement.

# #4
# def a():
#     return 5
#     print(10)
# print(a())

# # prediction 5, 10 // answer is 5. only one print() is allowed inside of a function. 

# #5
# def a():
#     print(5)
# x = a()
# print(x)

# # prediction 5. // uses the print(5) function at line 33.

# #6
# def a(b,c):
#     print(b+c)
# print(a(1,2) + a(2,3))

# doesnt have a return statement

# 7
# def a(b,c):
#     return str(b)+str(c)
# print(a(2,5))

# prediction 25. str coverts numbers into a string.

# 8
# def a():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
#         return 10
#     return 7
# print(a())

# prediction 100, 10


# 9
# def a(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(a(2,3))
# print(a(5,3))
# print(a(2,3) + a(5,3))

# prediction 7, 14, 21

# 10
# def a(b,c):
#     return b+c
#     return 10
# print(a(3,5))

# prediction 8

# 11

# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
# print(b)
# a()
# print(b)

# prediction: 500, 500, 300, 500

# #12
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# a()
# print(b)

# #prediction 500, 500, 300, 500

# #13
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# b=a()
# print(b)

# 500, 500, 300, 300


# #14
# def a():
#     print(1)
#     b() 
#     print(2)        
# def b():
#     print(3)
# a()


# 1, 3, 2

# 15
# def a():
#     print(1)
#     x = b()
#     print(x)
#     return 10
# def b():
#     print(3)
#     return 5
# y = a()
# print(y)


# def countdown(num):
#     newList = []
#     for i in range(num, 0, -1):
#         newList.append(i)
#     print(newList)
#     return newList

#     countdown(10)


#     while number >= 0:
#         newList.append(number)
#         number = number - 1









