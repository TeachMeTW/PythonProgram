class TestClass(object):
    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False
        
t = TestClass("Joe", 8.99)
print(t.price)