import os
import importlib
import subprocess
import sys
import interface as iface
import pkg_resources as respkg

setpkg = ['%s' % i.key for i in respkg.working_set]

usepkgs = [
    'keyboard',
    'cryptography',
    'pick'
]

for pkg in usepkgs:
    if not pkg in setpkg:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', pkg, '-q'])
        print(f'\'{pkg}\' was installed')

os.system('cls' if os.name == 'nt' else 'clear')

def load():
    iface.Interface()
    
    while iface.restart:
        rootPrivs = iface.root
        importlib.reload(iface)
        iface.root = rootPrivs
        load()

if __name__ == '__main__':
    load()