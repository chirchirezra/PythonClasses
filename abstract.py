import abc

class GetterSetter(object):
    __metaclass__= abc.ABCMeta

    @abc.abstractmethod
    def set_val(self,input):
        '''Implemet the setter method here'''
        return

    @abc.abstractmethod
    def get_val(self):
        '''Implement the getter method here'''
        return 

class SetGet(GetterSetter):

    def set_val(self,val):
        self.val = val

    def get_val(self):
        return self.val


x = SetGet()
x.set_val(4)
print(x.get_val())