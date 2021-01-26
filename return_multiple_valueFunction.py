

def returnFunction(a):
    if a%2 ==0:
        return True, 1

    return False, -1

# Taking the return in the OUTPUT VARIABLe here
output = returnFunction(10)
#printing the type of value:  ----> RETURNS (TUPLE)   <----
print(type(output))

firstVal, secondVal = returnFunction(10)

print("First Value :",firstVal, "Second Value",secondVal)