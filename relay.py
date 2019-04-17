import os
import sys
import socket

class Relayer(object):
    _buff = None
    _meta_IP = '10.250.21.252'
    _meta_port= '1234'
    _meta_file = 'note.txt'
    
    def __init__(self, master_ip, master_port):
        self._buff = []
        
    def get_hostname(self):
        #get hostname of itself, attempt to get IP of itself
        #this information is used to determine the role of the given progran
        #MUST have internet connection to get ip
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return(s.getsockname()[0])
        s.close()
        
        
    def get_metainfo(self):
        os.system('wget {}:{}/{}'.format(self._meta_IP, self._meta_port, self._meta_file))
        print open('./{}'.format(self._meta_file)).read()