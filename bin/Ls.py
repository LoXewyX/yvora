import os
from utils.Colors import TerminalColors as col
from utils.Fancyprint import Fancyprint as pc
import utils.Fancyprint

class Ls():
    def __init__(self, data, res, dirpath, root):
        
        utils.Fancyprint.data = data
        
        def pdirs(relpath):
            dirs = os.listdir(relpath)
            try:
                if len(dirs) > 1:
                    for x in dirs[:-1]:
                        print('├─', f'{col.CYAN}{x}{col.ENDC}' if os.path.isdir(os.path.join(relpath, x)) else x)
                if len(dirs) != 0:
                    print('└─', '{0}{1}{2}'.format(col.CYAN, dirs[-1], col.ENDC) if os.path.isdir(os.path.join(relpath, x)) else dirs[-1])
                else: print('└─', f'{col.WARNING}Empty dir{col.ENDC}')
            except: print(f'{col.WARNING}Not valid{col.ENDC}')
        
        if len(res) == 1:
            pc(4)
            relpath = os.path.join(dirpath, '' if root else data['user'], data['rootpath' if root else 'dirpath'][1:])
            pdirs(relpath)
            
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
                pdirs(relpath)
            else:
                pc(3)
                print(f'{col.WARNING}Not accessible{col.ENDC}')
            
        else:
            pc()
            print(f'{col.WARNING}ls must contain between 1 - 2 arguments{col.ENDC}')
