import socket
import relay
import mylog

class Source(relay.Relayer):
    _sock_send = None
    def __init__(self, ip, port, nb_ip, nb_port):
        self._ip = ip
        self._port = port
        self._nb_ip, self._nb_port = nb_ip, nb_port
        self._sock_send = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    def send_packet(self):
        mylog.log('SENDING message to {} - {}'.format(self._nb_ip, self._nb_port))
        MESSAGE = "hello"
        self._sock_send.sendto(MESSAGE, (self._nb_ip, self._nb_port))
        return
    
    def release(self):
        self._sock_send.close()