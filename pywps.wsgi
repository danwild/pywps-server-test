from pywps.app.Service import Service

import sys
sys.path.append('/usr/local/pywps-server')

print('\n\n----------PATH----------\n')
print(sys.path)

import processes
from processes.sayhello import SayHello

processes = [
   SayHello()
]

# Service accepts two parameters:
# 1 - list of process instances
# 2 - list of configuration files
application = Service(
    processes,
    ['/usr/local/pywps-server/pywps.cfg']
)
