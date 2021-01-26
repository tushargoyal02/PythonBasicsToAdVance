
# RETURN KEYWORD HERE
def produce():

    for i in range(0,10):
        # checking for even number
        if i%2 ==0:
            return i

print(produce())   # it returns only 0 as it only 1st condition is matched

# -------------
''' Yield keyword will resume iteration'''
def produce1():

    for i in range(0,10):
        # checking for even number
        if i%2 ==0:
            yield i
# it retuns some generator so access value over a loop
print(produce1())     

for i in produce1():
    print(i)