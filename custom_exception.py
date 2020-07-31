class MyCustomError(Exception):
    
    def __init__(self,*args):
        if args:
            self.message = args[0]
        else:
            self.message=''

    def __str__(self):
        if self.message:
            return f'Here is the Exception with the error {self.message}'
        else:
            return f'This is an exception without error message'

raise MyCustomError('Hello')