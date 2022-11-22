import os
from utils.Colors import TerminalColors as col
from utils.Fancyprint import Fancyprint as pc
import utils.Fancyprint
from utils.RelpathSolver import get_userpath

class Supersede():
    def __init__(self, data, res, dirpath, root):
        
        utils.Fancyprint.data = data
            
        def make(d, r):
            userpath = get_userpath(dirpath, data, root)
            relpath = os.path.join(userpath, data['rootpath' if root else 'dirpath'][1:])
            
            fenter = os.path.abspath(os.path.join(relpath, d))
            fexit = os.path.abspath(os.path.join(relpath, r))
            
            if fenter.startswith(userpath) and fexit.startswith(userpath):
                os.rename(fenter, fexit)
                pc()
                print('%s was superseded to %s' % (fenter.split(os.sep)[-1], fexit.split(os.sep)[-1]))
            else:
                pc()
                print(f'{col.WARNING}Not accessible{col.ENDC}')
        
        if len(res) == 1:
            
            global exitHK
            exitHK = False
            
            import keyboard
            def quitKH():
                global exitHK
                exitHK = True
                try:
                    keyboard.unregister_hotkey('ctrl+x')
                    keyboard.press('enter')
                except Exception: pass
                
            keyboard.add_hotkey('ctrl+x', lambda: quitKH())
            
            pc()
            d = input('Type your file you wish to supersede: ')
            
            if not exitHK:
                pc()
                r = input('To: ')
            
            if not exitHK:
                make(d, r)
            
        elif len(res) == 3:
            make(res[1], res[2])
            
        else:
            pc()
            print(f'{col.WARNING}supersede must contain 2 or none arguments{col.ENDC}')