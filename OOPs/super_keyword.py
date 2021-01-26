class UserDetail:

    def __init__(self, name, age):
        self.name=name
        self.age=age

    def information(self):
        print("name :",self.name,"Age :", self.age)


#inherit class (child)
class SocialMediaUser(UserDetail):

    #calling the super keyword & calling parent class constructor
    def __init__(self, name, age):
        super().__init__(name, age)


# object of inherit class
Socialuser = SocialMediaUser('tushar',30)

#calling PARENT class function to show user details
Socialuser.information()
