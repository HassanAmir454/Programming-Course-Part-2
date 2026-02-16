'''
use class_level attributes (root of the class) only for values that are the same for every object
Examples:
-Number of wheels on a car
-Pi constatnt
-configuration shared by all instances 
-Version numbers...
'''

class Car:
    wheels = 4  #same for all cars as a default
'''these attributes live on the class, not the object
Use construction (__init__) for instance specific data. They are unique per object.

Examples:
-Car color
-max sped
-current color
-registration number
'''

class Car:
    wheeels = 4
    def __init__(self, color, max_speed):
        self.color = color
        self.max_speed = max_speed
        self.current_speed = 0

'''everytime you create a new object, constructer __init__() runs and give the specific object it own attributes.
why not put specific object attributtes in the root? Because attributes in the root are shared unless unwritten


for example:
'''
class Person:
    hobbies = []

p1 = Person()
p2 = Person()

p1.hobbies.append("Football")
p1.hobbies.append("Reading")
p2.hobbies.append("Making music")

print(p2.hobbies) #output ['Football', 'Reading', 'Making music']

'''
if the list was inside __init__, each would get its own list
 '''

class Student:
    hobbies: list[str]
    def __init__(self, hobbies):
        self.hobbies = hobbies

s1 = Student("Football, Reading")

s2 = Student("Making music")

print(s1.hobbies)
print(s2.hobbies)

#Miras version 

class Student2:
    def __init__(self):
        self.hobbies = []

ss1 = Student2()
ss2 = Student2()

ss1.hobbies.append("Football")
ss1.hobbies.append("Reading")
ss2.hobbies.append("Making music")

print(ss1.hobbies)
print(ss2.hobbies)
#output ['Football', 'Reading']
#['Making music']



