class A:
    def __init__(self):
        self.name = 'xiaoming'
    def testA(self):
        print('----testA----')

class B:
    def __init__(self):
        self.age = 8
    def testB(self):
        print('----testB----')

class Person (A,B):
    def __init__(self):
        A.__init__(self)
        B.__inti__(self)
    def testPerson(self):
        print('----testPerson----')

person = Person()
print(person.name)
print(Person.name)
print(Person.age)
person.testA()
person.testB()
person.testPerson()

