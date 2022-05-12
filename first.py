print('Hello, world')

class TestClass(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
t = TestClass("Joe Mama", 69)
print("name = {}, age = {}".format(t.name, t.age))

def functest(fname, age):
    print('Function test')
    p = TestClass(fname, age)
    print(p.name, p.age)
    
functest('Robin','Simpson')