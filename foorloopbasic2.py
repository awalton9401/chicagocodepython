lst = [-5, 0, 5, 10, 15, 20, 20, 25]

def biggie_size(lst):
    for i in range(len(lst)):
        if lst[i] > 0:
            lst[i] = "big"
    return lst
print(biggie_size(lst))

def count_positives(lst):
    count = 0
    for i in range(0, len(lst), 1):
        if lst[i] > 0:
            count = count + 1
            lst[-1] = count    
    return lst
print(count_positives(lst))

def sum_total(lst):
    sum = 0
    for i in range(len(lst)):
        sum = sum + lst[i]
    return sum
print(sum_total(lst))

def avg(lst):
    avg = 0.0
    avg = float(sum_total(lst)) / float(len(lst))
    return avg
print(avg(lst))

def length(lst):
        return len(lst)
print(length(lst))

def max(lst):
    max = 0
    for i in range(len(lst)):
        if lst[i] > max:
            max = lst[i]
    return max
print(max(lst))

def min(lst):
    min = 0
    for i in range(len(lst)):
        if lst[i] < min:
            min = lst[i]
    return min
print(min(lst))

def ultanalysis(list):
    newobject = {
        "sumtotal":sum_total(lst),
        "average": avg(lst),
        "max": max(lst),
        "min": min(list),
        "length": len(lst)
    }
    return newobject
print(ultanalysis(lst))

def reverse(lst):
    for i in range(len(lst) / 2):
        temp = lst[i]
        lst[i] = lst[len(lst) - i - 1]
        lst[len(lst) - i - 1] = temp
    return lst
print(reverse(lst))










    

    




