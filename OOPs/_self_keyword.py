
class Person:
    def __init__(self,name):
        self.name = name
    
    #it is used to change the type of Object created
    def __str__(self):
        return("hello")


obj = Person('tushar')

# now you will see it doesn't show up the memory address now shows only the string data
print(obj)

#__Str__ is used to return and add any object with string data