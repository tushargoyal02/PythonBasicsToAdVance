'''Construct a class Car with the following features:
    create a class variable called color with value black
    create 2 instance variables: brand and year
    the instance variables are injected from outside - via a constructor
    generate functions with which we can acquire the instance variables - these are called getters
'''

class car:

    #class variable
    color = 'black'

    def __init__(self, brand,year):
        self.brand = brand
        self.year = year

    def data(self):
        print(self.brand, self.year)


obj = car('Buckati',2004)
obj.data()