class InstanceCounter(object):
    count=0
    def __init__(self,number):
        self.number = self.filter_int(number)
        InstanceCounter.count+=1
    
    @staticmethod
    def filter_int(val):
        if not isinstance(val,int):
            return 0
        else:
            return val

    def get_val(self):
        return self.number


instance = InstanceCounter('hello')
print(instance.get_val())