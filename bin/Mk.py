import os, json
from utils.Colors import TerminalColors as col
from utils.Fancyprint import Fancyprint as pc
import utils.Fancyprint

class Mk():
    def __init__(self, data, res, srcfolder, dirpath):
        
        utils.Fancyprint.data = data
        
        route = os.path.join(
            os.path.dirname(os.path.abspath(__file__)
            ), '..', srcfolder, "metadata.json")
        
        with open(route) as f:
            data = json.load(f)
            
        def mk(name, txt='', b=''):
            osfolders = name[1:] if name.startswith('/') or name.startswith('\\') else name
            
            if name.startswith('/') or name.startswith('\\'):
                relpath = os.path.abspath(os.path.join(dirpath, osfolders))
            else:
                relpath = os.path.abspath(os.path.join(dirpath, data['dirpath'][1:], osfolders))
            
            if relpath.startswith(dirpath):
                try:
                    with open(relpath, 'wb' if b else 'w') as f:
                        f.write(txt.encode('UTF-8') if b else txt)
                    
                except:
                    print(f'{col.WARNING}Not valid{col.ENDC}')
            else:
                pc()
                print(f'{col.WARNING}Not accessible{col.ENDC}')
                
        def error(types):
            print(f'{col.WARNING}Invalid arguments!{col.ENDC} Valids:')
            print(json.dumps(types, indent = 4))
        
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
            types = {
                '-b': '--bin'
            }
            
            #supervsion
            
            i = 3
            nxt = False
            skip = False
            
            b = False
            
            try:
                for x in res[i:]:
                    if not nxt:
                        if x == list(types.keys())[0] or x == types[list(types.keys())[0]]:
                            b = True
                            
                        else:
                            error(types)
                            skip = True
                            break
                        
                    else: nxt = False
                    i += 1
                
                if not skip:
                    mk(res[1], res[2], b)
            except:
                error(types)