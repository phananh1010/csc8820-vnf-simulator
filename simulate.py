import relay
import os
import header
import mylog

class Simulator:
    _meta_IP = None#'127.0.0.1', 6789
    _meta_port = None
    _port = None #4567
    _meta_file = header.FILENAME_METADATA   
    
    def __init__(self, meta_IP, meta_port, local_port):
        self._meta_IP = meta_IP
        self._meta_port = meta_port
        self._port = local_port
    
    def parse_metadata(self, text):
        for s in text.split('\n')[1:]:
            hostname, port, chain, role, nb_ip, nb_port = s.split(' ')
            #mylog.log((hostname, port, chain, role, self._port))
            if int(port) == self._port:
                mylog.log('MATCHED! metadata port: {}, local port: {}, role: {}, chain: {}'.format(port, self._port, role, chain))
                return hostname, port, chain, role, nb_ip, nb_port
        return None
    
    def get_hostname(self):
        #get hostname of itself, attempt to get IP of itself
        #this information is used to determine the role of the given progran
        #MUST have internet connection to get ip
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        
        IP, hostname = s.getsockname()[0], os.uname()[1]
        s.close()
        return IP, hostname

        
    def get_metainfo(self):
        #retrieve the meta infor from master server
        os.system('wget {}:{}/{}'.format(self._meta_IP, self._meta_port, self._meta_file))
        dat = open('./{}'.format(self._meta_file)).read()
        hostname, port, chain, role, nb_ip, nb_port = self.parse_metadata(dat)
        nbs_port = int(nb_port)
        port = int(port)
        return hostname, port, chain, role, nb_ip, nb_port    
        
    def run():
        LOCAL_PORT = 4567
        
        hostname, port, chain, role, nb_ip, nb_port = rl.get_metainfo()
        mylog.log('GATHER META DATA SUCCESS, Role: {}, Chain: {}, Neighbor: {}'.format(role, chain, (nb_ip, nb_port)))
        #if role == source, create source object
        #if role == sink, create sink object
        #if role == relay, create relayer
        #rl = relay.Relayer(LOCAL_PORT)
        #then, execute the 