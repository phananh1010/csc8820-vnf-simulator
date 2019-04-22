import socket
import relay
import mylog
import time

class Source(relay.Relayer):
    _sock_send = None
    def __init__(self, ip, port, nb_ip, nb_port):
        self._ip = ip
        self._port = port
        self._nb_ip, self._nb_port = nb_ip, nb_port
        self._sock_send = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    def send_packet(self, N):
        logdat = 'AT {} SENDING message to {} - {}'.format(mylog.mtime(), self._nb_ip, self._nb_port)
        mylog.log(logdat)  
        with open('source.txt', 'a') as f:
            for i in range(N):
                MESSAGE = '{0:064000}'.format(i)
                self._sock_send.sendto(MESSAGE, (self._nb_ip, self._nb_port))
                print >> f, 'SEND {} {}'.format(mylog.mtime(), i)     # Python 2.x
                f.flush()
                time.sleep(0.01)
            
        return
    
    def release(self):
        self._sock_send.close()