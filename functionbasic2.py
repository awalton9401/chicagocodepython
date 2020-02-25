num = 10

def countdown(num):
    newList = []
    for i in range(num, 0, -1):
        newList.append(i)
    print(newList)
countdown(num)

def print_and_return(lst):
    print(lst[0])
    return lst[1]
print(print_and_return([5, 10]))

lst = [1, 2, 3, 4, 5]

def first_plus_length(lst):
    sum = lst[0] + len(lst)
    return sum
print(first_plus_length(lst))

lst = [5 , 10, 15, 20, 25]

def values_greater_than_second(lst):
    newLst = []
    for i in range(0, len(lst), 1):
        if lst[i] > lst[1]:
            newLst.append(lst[i])
    return newLst
print(values_greater_than_second([5 , 10, 15, 20, 25]))

def this_length_that_value(size, value):
    newlst = []
    for i in range(0, size, 1):
        newlst.append(value)
    return newlst
print(this_length_that_value(10, 5))


def this_length_that_value(size, value):
    newlst = []
    for i in range(0, size, 1):
        newlst.append(value)
    return newlst
print(this_length_that_value(10, 5))



