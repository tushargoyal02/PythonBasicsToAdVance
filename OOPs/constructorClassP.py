

class person:

    # calling constructor which is a sought of initilization block
    #SELF is a reference to the instance of the person class
    
    # constructor initlizaing  {We can use any name in place of self}
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def nameShowing(self):
        print("name "+self.name,"\tAge :"+self.age)


obj = person('tushar',"20")

obj.nameShowing()