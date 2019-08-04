#!/usr/bin/env python3

class UserDate(object):
    def __init__(self,ID,Name):
        self.ID = ID
        self.Name = Name

    def __repr__(self):
        return 'ID:{} Name:{}'.format(self.ID, self.Name)

class NewUser(UserDate):
    def __init__(self,ID):
        super()._inti_(ID)


    def __inti__(self,Name):
        set_name = Name



if __name__=="__main__":
    user1 = NewUser(101,'Jack')
    user1.set_name('Jackie')
    user2 = NewUser(102,'Louplus')
    print(user1)
    print(user2)

