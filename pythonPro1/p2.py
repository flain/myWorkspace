__author__ = 'adminweke'
a = 1
b = 2
print a + b

class animal:
    def __init__(self):
        print 'in animal init'
    def run(self):
        print 'animal run'
a=animal()
a.run()
class dog(animal):
    pass
d=dog()
d.run()