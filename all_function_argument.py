'''  postional argument basically mean the order in which
    parameter is defined , the concreate value of argument should be
    passed in same order,.

'''
# multi-argument -
def multi(*names):
    print(names[0])
    print("Second argument from tuple : "+ names[1])

multi("tushar","goyal")

# default argument
def defaultFunc(name="Tushar"):
    print("Your name is : "+name,"\n")

defaultFunc()


#keyword argument - because the order doesn't matter for us now
def keywordFunc(name, age):
    print("Name is :"+ name)
    print("Age is {} ".format(age))
keywordFunc(name="Tushar", age=28)



# If we don't know how many keywords argument are there
def keywordArgument(**names):
    print(type(names))
    print(names["age"])
    print("The name of person is "+names["name"], "Age is", names["age"])
   
keywordArgument(name="Tushar",age=28)