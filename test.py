import source
import sink
import relay
import simulate
import header

reload(relay)
reload(header)
reload(simulate)
reload(sink)
reload(source)

import time

def create_service(PORT):
    sim = simulate.Simulator('131.96.155.202', 6789, PORT)
    return sim

def start_service(step=100):
    service = sim.run(step=step)

def release_service(sim):
    sim.release_service()
    
sim = create_service(5555)
start_service()
release_service(sim)