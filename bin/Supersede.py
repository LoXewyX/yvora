import os, json
from utils.Colors import TerminalColors as col
from utils.Fancyprint import Fancyprint as pc
import utils.Fancyprint

class Supersede():
    def __init__(self, data, res, srcfolder, dirpath):
        
        utils.Fancyprint.data = data
            
        def make(d, r):
            
            route = os.path.join(
                os.path.dirname(os.path.abspath(__file__)
                ), '..', srcfolder, "metadata.json")
            
            with open(route) as f:
                data = json.load(f)
            
            fenter = os.path.abspath(os.path.join(dirpath, data['dirpath'][1:], d))
            fexit = os.path.abspath(os.path.join(dirpath, data['dirpath'][1:], r))
            
            if fenter.startswith(dirpath) and fexit.startswith(dirpath):
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
                    keyboard.unregister_hotkey('ctrl+shift+q')
                    keyboard.press('enter')
                except Exception: pass
                
            keyboard.add_hotkey('ctrl+shift+q', lambda: quitKH())
            
            pc()
            d = input('Type your entrance: ')
            
            if not exitHK:
                r = input('Now, type your exit: ')
            
            if not exitHK:
                make(d, r)
            
        elif len(res) == 3:
            make(res[1], res[2])
            
        else:
            pc()
            print(f'{col.WARNING}Supersede must contain 2 or none arguments{col.ENDC}')