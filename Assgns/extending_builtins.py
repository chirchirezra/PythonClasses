import os

from config_error import ConfigError
class ConfigDict(dict):
    def __init__(self,filename):
        self._filename = filename
        if os.path.isfile(self._filename):
            try:
                with open(self._filename) as fh:
                    for line in fh:
                        line = line.rstrip()
                        key,value = line.split('=',1)
                        dict.__setitem__(self,key,value)
            except IOError:
                raise IOError('The file path is invalid')

    def __setitem__(self,key,value):
        dict.__setitem__(self,key,value)
        with open(self._filename,'w') as fw:
            for key,value in self.items():
                fw.write(f'{key}={value}\n')

    def __getitem__(self,key): 
        if not key in self.keys():
            raise ConfigError(self,key)
        else:
            return dict.__getitem__(self,key)
        

        
        

        
                


config = ConfigDict('conf.txt')
config.__setitem__('Name','Chirchir Ezra')
config.__setitem__('Age',24)
print(config.__getitem__('Age'))