class ConfigError(Exception):
    def __init__(self,this,key):
        self.key = key
        self.keys = this.keys()

    def __str__(self):
        return f'The key{self.key} doesnot exist available keys are {",".join(self.keys)}'