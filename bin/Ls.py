import os
from utils.Colors import TerminalColors as col
from utils.Fancyprint import Fancyprint as pc
import utils.Fancyprint

class Ls():
    def __init__(self, data, res, dirpath, root):
        
        utils.Fancyprint.data = data
            
        def pdirs(dirs):
            if len(dirs) > 1:
                for x in dirs[:-1]:
                    print('├─', x)
            if len(dirs) != 0:
                print('└─', dirs[-1])
            else: print('└─', f'{col.WARNING}Empty dir{col.ENDC}')
        
        if len(res) == 1:
            pc(4)
            relpath = os.path.join(dirpath, '' if root else data['user'], data['rootpath' if root else 'dirpath'][1:])
            pdirs(os.listdir(relpath))
            
        elif len(res) == 2:
            pc(4)
            userpath = dirpath if root else os.path.join(dirpath, data['user'])
            osfolders = res[1][1:] if res[1].startswith('/') or res[1].startswith('\\') else res[1]
            
            if res[1].startswith('/') or res[1].startswith('\\'):
                relpath = os.path.abspath(
                    os.path.join(userpath, osfolders)
                )
            else:
                relpath = os.path.abspath(os.path.join(userpath, data['rootpath' if root else 'dirpath'][1:], osfolders))
            
            if os.path.exists(relpath) and relpath.startswith(userpath):
                try:
                    dirs = os.listdir(relpath)
                    pdirs(dirs)
                    
                except:
                    pc()
                    print(f'{col.WARNING}Not accessible{col.ENDC}')
            else:
                pc(3)
                print(f'{col.WARNING}Not accessible{col.ENDC}')
            
        else:
            pc()
            print(f'{col.WARNING}ls must contain 1 argument{col.ENDC}')