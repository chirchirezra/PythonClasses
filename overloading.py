import abc

class SetGetParent(object):
    '''implement the abstract class SetGetParent'''
    __metaclass__=abc.ABCMeta

    def __init__(self,val):
        self.val = val

    def set_val(self,value):
        self.val=value

    def get_val(self):
        return self.val

    @abc.abstractmethod
    def show_doc(self):
        return

class GetSetInt(SetGetParent):

    def set_val(self,val):
        if not isinstance(val,int):
            return 0
        super(GetSetInt,self).set_val(val)

    def show_doc(self):
        print(f'The value of val is {self.val}')


class GetSetList(SetGetParent):
    
    def __init__(self,value):
        self.value_list = [value]
    def set_val(self,value):
        self.value_list.append(value)

    def get_val(self):
        return self.value_list[-1]

    def get_values(self):
        return self.value_list

    def show_doc(self):
        print(f'The length of the list is {len(self.value_list)} ')


instance = GetSetList(6)
instance.set_val(34)
instance.set_val(40)
instance.set_val(38)

print(instance.get_val())
print(instance.get_values())
instance.show_doc()
