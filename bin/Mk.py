import os, json
from utils.Colors import TerminalColors as col
from utils.Fancyprint import Fancyprint as pc
import utils.Fancyprint
from utils.RelpathSolver import get_userpath

class Mk():
    def __init__(self, data, res, dirpath, root):
        
        utils.Fancyprint.data = data
            
        def mk(name, txt=''):
            
            userpath = get_userpath(dirpath, data, root)
            relpath = os.path.abspath(os.path.join(userpath, data['rootpath' if root else 'dirpath'][1:], name))
            if relpath.startswith(userpath):
                with open(relpath, 'w') as f:
                    f.write(txt)
                            
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
                    print(f'\n{col.RED}escaped{col.ENDC}')
                except Exception: pass
            keyboard.add_hotkey('ctrl+x', lambda: quitKH())
            
            pc()
            f = input('Type your file\'s name: ')
            if not exitHK:
                pc()
                c = input('Now, type your content: ')
            
            if not exitHK:
                mk(f, c)
        
        elif len(res) == 2:
            mk(res[1])
            
        elif len(res) == 3:
            mk(res[1], res[2])
            
        else:
            pc()
            print(f'{col.WARNING}mk must contain 1 or none arguments{col.ENDC}')