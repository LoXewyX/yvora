import os, json
from utils.Colors import TerminalColors as col
from utils.Fancyprint import Fancyprint as pc
import utils.Fancyprint

class Cd():
    def __init__(self, data, res, srcfolder, dirpath):
        
        utils.Fancyprint.data = data
        
        if len(res) == 2:
            
            route = os.path.join(
                os.path.dirname(os.path.abspath(__file__)
                ), '..', srcfolder, "metadata.json")
            
            with open(route) as f:
                data = json.load(f)
            
            osfolders = res[1][1:] if res[1].startswith('/') or res[1].startswith('\\') else res[1]
            
            if res[1].startswith('/') or res[1].startswith('\\'):
                relpath = os.path.abspath(os.path.join(dirpath, osfolders))
            else:
                relpath = os.path.abspath(os.path.join(dirpath, data['dirpath'][1:], osfolders))
            
            if os.path.exists(relpath) and relpath.startswith(dirpath):
                try:
                    
                    if relpath == dirpath: data['dirpath'] = '/'
                    else: data['dirpath'] = relpath.replace(dirpath, "").replace(os.sep, '/')
                        
                    with open(route, 'w') as f:
                        json.dump(data, f, indent=4)
                except:
                    pc()
                    print(f'{col.WARNING}Not accessible{col.ENDC}')
            else:
                pc()
                print(f'{col.WARNING}Not accessible{col.ENDC}')
            
        else:
            pc()
            print(f'{col.WARNING}cd must contain 1 argument{col.ENDC}')