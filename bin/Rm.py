import os, json
from utils.Colors import TerminalColors as col
from utils.Fancyprint import Fancyprint as pc
import utils.Fancyprint
from utils.RelpathSolver import get_userpath

class Rm():
    def __init__(self, data, res, dirpath, root):
        
        utils.Fancyprint.data = data
            
        def rm(d, rec=False):
                
            userpath = get_userpath(dirpath, data, root)
            relpath = os.path.abspath(os.path.join(userpath, data['rootpath' if root else 'dirpath'][1:], d))
            
            if relpath.startswith(userpath) and os.path.exists(relpath):
                if os.path.isfile(relpath):
                    os.remove(relpath)
                else:
                    if rec:
                        import shutil
                        shutil.rmtree(relpath)

                    else:
                        try:
                            os.rmdir(relpath)
                        except:
                            pc()
                            print(f'{col.WARNING}This directory contains files{col.ENDC}')
                
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
            d = input('Type your directory / file you want to remove: ')
            
            if not exitHK: rm(d)
            
        elif len(res) == 2: rm(res[1])
        
        else:
            types = {
                '-r': '--recursive',
            }
            
            rec = False
            
            ignore = False
            
            try:
                for x in res[2:]:
                    if x == list(types.keys())[0] or x == types[list(types.keys())[0]]:
                        rec = True
                    
                    else:
                        print('x')
                        error(types)
                        ignore = True
                        break
                
                if not ignore: rm(res[1], rec)
            except Exception as e:
                print(e)
                error(types)