import os
from utils.Colors import TerminalColors as col
from utils.Fancyprint import Fancyprint as pc
import utils.Fancyprint
from utils.RelpathSolver import get_userpath

class Mkdir():
    def __init__(self, data, res, dirpath, root):
        
        utils.Fancyprint.data = data
            
        def make(d):
            
            userpath = get_userpath(dirpath, data, root)
            relpath = os.path.abspath(os.path.join(userpath, data['rootpath' if root else 'dirpath'][1:], d))
            
            if relpath.startswith(userpath):
                if os.path.exists(relpath):
                    pc()
                    print(f'{col.WARNING}Directory exists{col.ENDC}')
                else:
                    os.makedirs(relpath, exist_ok=True)
                    pc()
                    print('Directory created')
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
            d = input('Now, type your folder\'s name: ')
            
            if not exitHK:
                make(d)
            
        elif len(res) == 2:
            make(res[1])
            
        else:
            pc()
            print(f'{col.WARNING}mkdir must contain 1 or none arguments{col.ENDC}')