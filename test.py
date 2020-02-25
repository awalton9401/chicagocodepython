# students = [
#          {'first_name':  'Michael', 'last_name' : 'Jordan'},
#          {'first_name' : 'John', 'last_name' : 'Rosales'},
#          {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#          {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]

# def iterateDictionary(some_list):
#     for i in range(len(some_list)):
#         for item in some_list[i]:
#             print(item, some_list[i][item])
#     return some_list
# iterateDictionary(students)


# dojo = {
#    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }


# def printInfo(some_dict):
#     for i in(some_dict):
#         print(len(some_dict[i]),i)
#         for item in range(len(some_dict[i])):
#             print(some_dict[i][item])       
#     return some_dict
# printInfo(dojo)


def extractDigit(num, ind):
   str_num =str(num)
   list = []
   for char in reversed(str_num):
      list.append(char)
      print(list)
   if(ind < len(list)):
      return list[ind]
   else: return 0

print(extractDigit(5678, 2))















class Animal:
    def __init__(self, animal_name, age):
        self.animal_name = animal_name
        self.age = age
        self.health_level = 0
        self.happiness_level = 0

    def feed(self):
        raise NotImplementedError

    def display_info(self):
        print(self.animal_name, self.age, self.health_level, self.happiness_level)


class Lion(Animal):
    def __init__(self, animal_name, age):
        super().__init__(animal_name, age)
        self.has_mane = True
        self.health_level = 2
        self.happiness_level = 3
    
    def feed(self):
        self.health_level += 5
        self.happiness_level += 4




class zoo: 












lion=Lion("Leo", 33)

lion.display_info()
    
    