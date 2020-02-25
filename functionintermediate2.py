x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)

students[0]['last_name'] = 'Bryant'
print(students[0])

sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'])

z[0]['y'] = 30
print(z)

studentsList = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


def iterateDictionary(some_list):
    for i in range(len(some_list)):
        for key in some_list[i]:
            print(key, some_list[i][key])
    return some_list
iterateDictionary(studentsList)

def iterDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        print(some_list[i][key_name])
    return some_list
iterDictionary2('first_name', studentsList)
iterDictionary2('last_name', studentsList)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for item in some_dict:        
        print(item, len(some_dict[item]))
        for i in range(len(some_dict[item])):
            print(some_dict[item][i])
    return some_dict
printInfo(dojo)

