import time
from threading import Thread
from .classes import Volume, PortMapping

# stop_event= threading.Event()
# p = Thread(target=producer, args=(msg_queue, stop_event))
# p.start()

daemonThreads: list[Thread] = []

def updateContainerState():
    pass

def checkHealth():
    pass

def spawnContainer(name: str="Name of container", image: str="Docker image", cmd: str = '', volumes: list[Volume]=[], portMappings: list[PortMapping]=[]):
    cmd = f'docker run -d {' '.join(list(map(lambda x: f'-v {x.hostPath}:{x.containerPath}', volumes)))} {' '.join(list(map(lambda x: f'-p {x.hostPort}:{x.containerPort}', portMappings)))} --name {name} {image} {cmd}'
    # Execute the cmd
    