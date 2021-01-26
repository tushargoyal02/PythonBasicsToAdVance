
class smallValueException(Exception):

    def __init__(self, msg):
        #defining the instance variable
        self.msg=msg

    def showMessage(self):
        return self.msg

#defing second class exception {User Defined}
class largeValueException(Exception):
    def __init__(self,msg):
        self.msg=msg

    def showMessage(self):
        return self.msg



number = 1300

try:
    if number < 20:
        raise smallValueException("Value is small Exception")

    elif number >1200:
        raise largeValueException("Value is very large Exception")

    print("Value is withing the range 20 & 1200")

except smallValueException as se:
    print(se.showMessage())

except largeValueException as largeEx:
    print(largeEx.showMessage())