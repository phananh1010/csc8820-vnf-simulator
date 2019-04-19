import os
import sys
import socket
import header
import mylog

class Relayer(object):
    _buff = None
    _sock = None
    
    _port = None
    _nb_ip = None
    _nb_port = None

    
    def __init__(self, port, nb_ip, nb_port):
        self._buff = []
        self._port = port
        self._nb_ip, self._nb_port = nb_ip, nb_port


    
    def start_server(self):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        self._sock.bind((UDP_IP, UDP_PORT))
        
    def relay(self):
        
        return