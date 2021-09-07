#Collections are groups of items. Python supports several types of collections. Three of the most common are dictionaries, lists and arrays.
#Lists are a collection of items. Lists can be expanded or contracted as needed, and can contain any data type. 
#Lists are most commonly used to store a single column collection of information, however it is possible to nest lists


#Search for; 
#Tuple, Sets(), 

from collections import counter 

Country = {}
Country['first'] = 'Nepal,'
City ['last']= 'Colorado'
Kenya = {}
 City ['first'] = 'Nairobi'
 Arthur['last'] = 'Joe'

 Citizenship = []
 Citizenship.append(Country)
 Citizenship.append(Mark)
 Citizenship.append({
     'first': 'Dennis', 'last': 'Ngethe'
 })
 print(Citizenship)
 people = ['Luke', 'Nathan']
 

a = 'The counter is used to select different types of items depending on the attributes of which have been input. E.g. keys, items, values.'
my_counter = Counter(a)
print(my_counter)
#print(my_counter.keys())
#print(my_counter.items())
#print(my_counter.values())


from array import array
scores = array('d')
scores.append(97)
scores.append(98)
print(scores)

#Arrays are similar to lists, however are designed to store a uniform basic data type, such as integers or floating point numbers.

names = ['Dennis', 'Micheal']
print(len(names)) # Get the number of items
names.insert(0, 'Jonathan') # Insert before index
print(names)

person = {'first': 'Dennis'}
person['last'] = 'Nancy'
print(person)
print(person['first'])

names = ['Dennis', 'Lissa']
scores = []
scores.append(98)
scores.append(99)
print(names)
print(scores)

names = ['Samuel', 'Oscar', 'Bill']
presenters = names[0:2] # Get the first two items
# Starting index and number of items to retrieve
print(names)
print(presenters)


