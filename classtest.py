#!/usr/bin/env python3

class UserDate:
    def __init__(self,ID,name):
        self.ID = ID
        self._name = name

    def __repr__(self):
        return 'ID:{} name:{}'.format(self.ID, self._name)


class NewUser(UserDate):
    def get_name(self):
        return self._name
    def set_name(self,value):
        self._name = value

if __name__=="__main__":
    user1 = NewUser(101,'Jack')
    user1.set_name('Jackie')
    user2 = NewUser(102,'Louplus')
    print(user1)
    print(user2)

