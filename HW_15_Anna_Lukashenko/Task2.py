'''2) Write a Python program to create two empty classes, Student and Marks. Now create some instances and check whether they are instances of the said classes or not. Also, check whether the said classes are subclasses of the built-in object class or not.'''

#create two empty classes, Student and Marks.
class Students:
    pass

class Marks:
    pass

# create  instances
anna = Students()
andrew = Students()
very_good = Marks()

# check whether created instances are instances of the said classes or not.
print(type(anna))
print(type(andrew))
print(type(very_good))

# check whether the said classes are subclasses of the built-in object class or not
print(issubclass(Students,object))
print(issubclass(Marks,object))