import datetime
import os
import abc
class Writter(object):
    __metaclass__ = abc.ABCMeta
    def __init__(self,file_name):
        if os.path.exists(file_name):
            self.file = open(file_name,'a')
        else:
            self.file=open(file_name,'w')
    @abc.abstractmethod
    def write_stuff(self):
        return
    def close(self):
        self.file.close()
class WriteLog(Writter):
    def write_stuff(self,text_to_write):
        self.string = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+' ------ '+text_to_write+'\n'
        self.file.write(self.string)

class WriteCsv(Writter):
    def write_stuff(self,delimiter,list_of_values = []):
        self.stringtowrite = ''
        for string in list_of_values:
            if string !=list_of_values[-1]:
                self.stringtowrite +=' '+string+delimiter
            else:
                self.stringtowrite+=' '+string
            
        self.file.write(self.stringtowrite) 


log = WriteLog('logs.txt')
log.write_stuff('Requests from the ip 192.168.1.0')
log.write_stuff('Response to the ip 192.168.1.0')
log.close()

csv = WriteCsv('alphabets.csv')
csv.write_stuff(',',['a','b','c','d'])
csv.write_stuff(',',['e','f','g','h'])
csv.close()