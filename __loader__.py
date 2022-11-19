# subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip', '-q'])
# print('\'pip\' was upgraded')

import pkg_resources as pkg
import importlib
data = pkg.working_set

def printPkgs():
    print(['%s' % i.key for i in data])

def isPkgInstalled(pkg):
    for i in data:
        if i.key == pkg:
            return True
    return False

# start
if not isPkgInstalled('keyboard'):
    import subprocess, sys
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'keyboard', '-q'])
    print('\'pynput\' was installed')
    
import interface as iface
def load():
    iface.Interface()
    
    while iface.restart:
        iface.restart = False
        importlib.reload(iface)
        load()
        
load()
