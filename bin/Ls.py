import os, json
from utils.Colors import TerminalColors as col
from utils.Fancyprint import Fancyprint as pc
import utils.Fancyprint

class Ls():
    def __init__(self, data, res, srcfolder, dirpath):
        
        utils.Fancyprint.data = data
        
        route = os.path.join(
            os.path.dirname(os.path.abspath(__file__)
            ), '..', srcfolder, "metadata.json")
        
        with open(route) as f:
            data = json.load(f)
            
        def pdirs(dirs):
            if len(dirs) > 1:
                for x in dirs[:-1]:
                    print('├─', x)
            if len(dirs) != 0:
                print('└─', dirs[-1])
            else: print('└─', f'{col.WARNING}Empty dir{col.ENDC}')
        
        if len(res) == 2:
            pc(4)
            osfolders = res[1][1:] if res[1].startswith('/') or res[1].startswith('\\') else res[1]
            
            if res[1].startswith('/') or res[1].startswith('\\'):
                relpath = os.path.abspath(os.path.join(dirpath, osfolders))
            else:
                relpath = os.path.abspath(os.path.join(dirpath, data['dirpath'][1:], osfolders))
            
            if os.path.exists(relpath) and relpath.startswith(dirpath):
                try:
                    print(relpath)
                    dirs = os.listdir(relpath)
                    pdirs(dirs)
                    
                except:
                    pc()
                    print(f'{col.WARNING}Not accessible{col.ENDC}')
            else:
                pc()
                print(f'{col.WARNING}Not accessible{col.ENDC}')
        
        elif len(res) == 1:
            pc(4)
            relpath = os.path.join(dirpath, data['dirpath'][1:])
            dirs = os.listdir(relpath)
                    
            pdirs(dirs)
            
        else:
            pc()
            print(f'{col.WARNING}ls must contain 1 argument{col.ENDC}')