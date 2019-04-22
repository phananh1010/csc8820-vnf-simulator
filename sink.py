import mylog
import relay
import socket
import header

class Sink(relay.Relayer):
    _sock_recv = None
    def __init__(self, ip, port):
        self._ip = ip
        self._port = port
        #self._nb_ip, self._nb_port = nb_ip, nb_port #no neighbor
        self._sock_recv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._sock_recv.bind((self._ip, self._port))
        
    def recv(self):
        mylog.log("LISTENING AT {} - {}".format(self._nb_ip, self._nb_port))  
        with open('sink.txt', 'w') as f:
            while True:
                data, addr = self._sock_recv.recvfrom(1024) # buffer size is 1024 bytes
                logdat = "AT {} RECEIVED - {} FROM - {}".format(mylog.mtime(), data, addr)
                mylog.log(logdat)
                print >> f, 'RECEIVE {} {}'.format(mylog.mtime(), data)     # Python 2.x
                f.flush()
            
    def release(self):
        self._sock_recv.close()