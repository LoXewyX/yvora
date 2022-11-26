import os, json
from utils.Colors import TerminalColors as col
from utils.Fancyprint import Fancyprint as pc
import utils.Fancyprint
from utils.RelpathSolver import get_relpath, get_userpath, get_route

class Cd():
    def __init__(self, data, res, srcfolder, dirpath, root):
        
        utils.Fancyprint.data = data
        
        if len(res) == 2:
            
            relpath = get_relpath(res, dirpath, srcfolder, root)
            userpath = get_userpath(dirpath, data, root)
            route = get_route(dirpath, srcfolder, 'metadata.json')
            
            if os.path.exists(relpath) and relpath.startswith(userpath) and os.path.isdir(relpath):
                try:
                    
                    if relpath == userpath: data['rootpath' if root else 'dirpath'] = '/'
                    else: data['rootpath' if root else 'dirpath'] = relpath.replace(userpath, "").replace(os.sep, '/')
                        
                    with open(route, 'w') as f:
                        json.dump(data, f, indent=4, sort_keys=True)
                except:
                    pc()
                    print(f'{col.WARNING}Not accessible{col.ENDC}')
            else:
                pc()
                print(f'{col.WARNING}Not accessible{col.ENDC}')
            
        else:
            pc()
            print(f'{col.WARNING}cd must contain 1 argument{col.ENDC}')