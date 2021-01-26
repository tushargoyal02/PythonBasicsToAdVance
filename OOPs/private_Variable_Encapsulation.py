class vehcile:
    
    # It is always said that it creates private variable
    _name = "Tata Motors"

    # now I have used two (double underscore) <- It will do Name Mangaling
    __newName = "New Tata Motors"

obj = vehcile()
print(obj._name)   # we are still able to access this data


# print(obj.__newName)          #this will give error
#print(dir(obj))                # it gives everything 
''' Above your will find the change the name of variable {__newName} to
{_vehcile__newName}  -> className.variableName
That is how we acheive private variables '''

# to access the same data
print(obj._vehcile__newName)