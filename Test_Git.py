import os


class Test_Git:
    '''Class used to test how Git works with TortoiseGit'''


    def __init__(self,**kwargs):
        
        self.name   =   'Test_Git'
        self.level  =   1
        self.config = {}

        for key in kwargs:
            self.config[key]     = kwargs[key]


    def print_kwargs(self,**kwargs):
        for key in kwargs:
            print("key = {0}, value = {1}".format(key, kwargs[key]))

        
class Foo:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

#door = Foo(size='180x70', color='red chestnut', material='oak')
#print(door.size) #180x70


if __name__=='__main__':
    os.chdir('C:\Users\JKaminski\OneDrive\Internship DLR\Git practice\Test_repository')


    from Test_Git import Test_Git
    obj = Test_Git(config1 = 'test', config2 = 'test2')
    obj.print_kwargs(a="two", b=1)
