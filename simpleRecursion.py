

def sumRecursion(x):

    # defining the base case like where to stop
    if x==0:
        return 0

    ''' Here on first iterate n=5 
    n=5+numRecursion(5-1)
    Every iterate problem can be solved by recursion & vice-a-versa
    '''
    return x+sumRecursion(x-1)

print(sumRecursion(5))