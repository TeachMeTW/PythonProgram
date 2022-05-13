print('Hello, world')

print(3+4)
print("Hello")
print("World")

print("My favorite number are", 3+4, "and", 3+ 10) # error without the comma after and
print("Goodbye")
print()
print("Hope to see you again")





class TestClass(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
t = TestClass("Joe Mama", 69)
print("name = {}, age = {}".format(t.name, t.age))

def functest(fname, age):
    print('Function test')
    p = TestClass(fname, age)
    print('New person name is ' + p.name + ' and age is ' +p.age + ' years old')
    
print('Enter name for person')
name = input()
print('Enter age for person')
age = input()
functest(name, age)