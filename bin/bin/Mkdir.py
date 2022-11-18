import os, json
from utils.Colors import TerminalColors as col
from utils.Fancyprint import Fancyprint as pc
import utils.Fancyprint

class Mkdir():
    def __init__(self, data, res, srcfolder, dirpath):
        
        utils.Fancyprint.data = data
            
        def make(d):
            
            route = os.path.join(
                os.path.dirname(os.path.abspath(__file__)
                ), '..', srcfolder, "metadata.json")
            
            with open(route) as f:
                data = json.load(f)
            
            fJunction = os.path.abspath(os.path.join(dirpath, data['dirpath'][1:], d))
            if fJunction.startswith(dirpath):
                if os.path.exists(fJunction):
                    pc()
                    print(f'{col.WARNING}Directory exists{col.ENDC}')
                else:
                    os.makedirs(fJunction, exist_ok=True)
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
                    keyboard.unregister_hotkey('ctrl+shift+q')
                    keyboard.press('enter')
                except Exception: pass
                
            keyboard.add_hotkey('ctrl+shift+q', lambda: quitKH())
            
            pc()
            d = input('Now, type you folder\'s name: ')
            
            if not exitHK:
                make(d)
            
        elif len(res) == 2:
            make(res[1])
            
        else:
            pc()
            print(f'{col.WARNING}Mkdir must contain 1 or none arguments{col.ENDC}')