class User:
    def __init__(self,id,name):
        self.user_id=id
        self.user_name=name
        self.follower=0
        self.following=0
    def follow(self,user):
        user.follower+=1
        self.following+=1

user_1=User("001","Harshit")
print(user_1.user_id,user_1.user_name)
user_2=User("002","Divyani")
print(user_2.user_id,user_2.user_name)
user_1.follow(user_2)
print(user_1.follower)
print(user_1.following)
print(user_2.follower)
print(user_2.following)
