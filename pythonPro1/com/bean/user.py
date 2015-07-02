__author__ = 'adminweke'
class user:
    def __init__(self, name):
        self.name = name

    def myname(self):
        print('my name is %s' % self.name)

u = user('Liu')
u.myname()