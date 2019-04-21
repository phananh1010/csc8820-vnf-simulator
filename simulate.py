import relay
import source
import sink
import os
import header
import mylog


class Simulator:
    _meta_IP = None#'127.0.0.1', 6789
    _meta_port = None
    _port = None #4567
    _meta_file = header.FILENAME_METADATA  
    _service = None
    
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
        #os.system('wget {}:{}/{}'.format(self._meta_IP, self._meta_port, self._meta_file))
        dat = open('./{}'.format(self._meta_file)).read()
        hostname, port, chain, role, nb_ip, nb_port = self.parse_metadata(dat)
        nb_port = int(nb_port)
        port = int(port)
        try:
            os.system('rm {}'.format(self._meta_file + '.*'))
        except Exception, e:
            mylog.log(e);  
        return hostname, port, chain, role, nb_ip, nb_port    
    
    def set_service(self, service):
        self._service = service
        
    def release_service(self):
        self._service.release()
        
    def run(self):
        #create the service for given port
        hostname, port, chain, role, nb_ip, nb_port = self.get_metainfo()
        if role == header.ROLE_SOURCE:
            service = source.Source(port, nb_ip, nb_port)
            self.set_service(service)
            service.send_packet()
        elif role == header.ROLE_SINK:
            service = sink.Sink(port)
            self.set_service(service)
            service.recv()
        elif role == header.ROLE_RELAYER:
            service = relay.Relayer(port, nb_ip, nb_port)
            self.set_service(service)
            service.relay()  
        else:
            mylog.log('ERROR, role not matched')
            raise

        return service