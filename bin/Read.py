import os, json
from utils.Colors import TerminalColors as col
from utils.Fancyprint import Fancyprint as pc
import utils.Fancyprint
from utils.RelpathSolver import get_userpath

class Read():
    def __init__(self, data, res, dirpath, root):
        
        utils.Fancyprint.data = data
            
        def read(n=None, m=None, o=False):
            
            junction = res[1][1:] if res[1].startswith('/') or res[1].startswith('\\') else res[1]
            userpath = get_userpath(dirpath, data, root)
            
            if res[1].startswith('/') or res[1].startswith('\\'):
                relpath = os.path.abspath(os.path.join(userpath, junction))
            else:
                relpath = os.path.abspath(os.path.join(userpath, data['rootpath' if root else 'dirpath'][1:], junction))
            
            if os.path.exists(relpath) and relpath.startswith(userpath):
                try:
                    pc()
                    print('%s%s - %i lines%s' % (col.CYAN, relpath.split(os.sep)[-1], len(open(relpath, 'r').readlines()), col.ENDC))
                    if isinstance(n, str): n = int(n)
                    if isinstance(m, str): m = int(m) + 1
                    str_ar = open(relpath, 'r').read().split('\n')[n:m]
                    if n == None: n = 0
                    for i in range(len(str_ar)):
                        print('%s %s' % (str(i+n).zfill( len(str(len(str_ar))) ) if o else '', str_ar[i]))
                    
                except:
                    print(f'{col.WARNING}Not accessible{col.ENDC}')
            else:
                pc()
                print(f'{col.WARNING}Not accessible{col.ENDC}')
                
        def error(types):
            print(f'{col.WARNING}Invalid arguments!{col.ENDC} Valids:')
            print(json.dumps(types, indent = 4))
            print('--min or --max requires an extra number argument')
        
        if len(res) == 1:
            print(f'{col.WARNING}read must contain at least 1 argument{col.ENDC}')
            
        elif len(res) == 2:
            read()
            
        else:
            types = {
                '-n': '--min',
                '-m': '--max',
                '-o': '--num'
            }
            
            i = 2
            nxt = False
            skip = False
            
            n = None
            m = None
            o = False
            
            try:
                for x in res[i:]:
                    if not nxt:
                        if x == list(types.keys())[0] or x == types[list(types.keys())[0]]:
                            n = res[i+1]
                            nxt = True
                            
                        elif x == list(types.keys())[1] or x == types[list(types.keys())[1]]:
                            m = res[i+1]
                            nxt = True
                            
                        elif x == list(types.keys())[2] or x == types[list(types.keys())[2]]:
                            o = True
                            
                        else:
                            error(types)
                            skip = True
                            break
                        
                    else: nxt = False
                    i += 1
                
                if not skip:
                    read(n, m, o)
            except:
                error(types)