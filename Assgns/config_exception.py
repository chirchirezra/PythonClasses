class ConfigError(Exception):

    def __init__(self,*args):
        if args:
            self.message = args[0]
        else:
            self.message = ''

    def __str__(self):
        if self.message:
            return f'{self.message}'
        else:
            return 'Configuration Error'