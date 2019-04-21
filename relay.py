import os
import sys
import socket
import header
import mylog

class Relayer(object):
    _buff = None
    _sock = None
    
    _ip = None
    _port = None
    _nb_ip = None
    _nb_port = None

    
    def __init__(self, ip, port, nb_ip, nb_port):
        self._buff = []
        self._ip = ip
        self._port = port
        self._nb_ip, self._nb_port = nb_ip, nb_port
        
        self._sock_recv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._sock_recv.bind((self._ip, self._port))
        
        self._sock_send = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


    
    def relay(self):
        mylog.log("LISTENING AT {}".format(self._port))
        while True:
            data, addr = self._sock_recv.recvfrom(1024) # buffer size is 1024 bytes
            self._sock_send.sendto(data, (self._nb_ip, self._nb_port))
            mylog.log("DEBUG: RELAYED - {} FROM - {} TO - {}".format(data, addr, (self._nb_ip, self._nb_port)))
        
        
    def release(self):
        self._sock_send.close()
        self._sock_recv.close()
        return