

class person:

    # calling constructor which is a sought of initilization block
    #SELF is a reference to the instance of the person class
    
    # constructor initlizaing  {We can use any name in place of self}
    def __init__(self,name, age):
        #THIS IS A INSTANCE VARIABLE
        self.name = name
        self.age = age

    def nameShowing(self):
        print("name "+self.name,"\tAge :"+self.age)

obj = person('tushar',"210")
obj2 = person('Goyal','410')    # second instance have access to new data
obj.nameShowing()
obj2.nameShowing()