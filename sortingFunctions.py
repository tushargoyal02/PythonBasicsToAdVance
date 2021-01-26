
# sort the data structure in python
nums = [1,0,-1,23,445]

#using sorted function to sort the values  - Return a list
output =sorted(nums)
print(output)

#sorting result in reverse order
output =sorted(nums, reverse=True)
print(output)

#sorting the data as per the length of the string
#-- HERE WE HAVE KEY PARAMETER , where we can define our logic

def lengthSorting(x):
    return len(x)

data = ['a','fdsafas','tushar']

finalOut = sorted(data , key=lengthSorting)
print(finalOut)

