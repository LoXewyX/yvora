import shutil, os, json, keyboard
from utils.Colors import TerminalColors as col
from utils.Fancyprint import Fancyprint as pc
import utils.Fancyprint

class Acquire():
    def __init__(self, data, apps, res, path, binfolder, srcfolder):
        
        utils.Fancyprint.data = data
        
        def ask():
            i = 'foo'
            while not (i == 'y' or i == 'n' or i == ''):
                i = input('Are you sure you want to install package %s [Y/n]: ' % res[1])
            return True if i == 'y' or i == '' else False
        
        def desist():
            pc()
            print('Understood...')
        
        def quitKH():
            global exitHK
            exitHK = True
            try:
                keyboard.unregister_hotkey('ctrl+shift+q')
                keyboard.press('enter')
            except Exception: pass
        
        def give():
            global force
            if res[1] in remoteApps:
                if not res[1] in apps or force:
                    extract()
                else:
                    global exitHK
                    if not exitHK:
                        pc(4)
                        pc(2)
                        print(f'{col.WARNING}App {res[1]} is already indexed{col.ENDC}')
                        pc(3)
                        i = input('Do you wish to reinstall it [Y/n]? ')
                        if not exitHK and (i == '' or i == 'n' or i == 'y'):
                            extract() if i == 'y' or i == '' else desist()
                                
            elif not exitHK:
                pc()
                print(f'{col.WARNING}App {res[1]} is not indexed on my cloud{col.ENDC}')
            
        def extract():
            shutil.copy2(os.path.join(cloudRoute, 'acquire', '%s.py' % res[1].capitalize()), os.path.join(path, binfolder))
            
            w = apps
            w.update({res[1]: remoteApps[res[1]]})
            
            with open(os.path.join(path, srcfolder, 'apps.json'), 'w') as f:
                json.dump(w, f, indent=4)
        
        global force, remoteApps, exitHK
        force = False
        exitHK = False
        cloudRoute = os.path.join(path, '..', 'yvora_cloud')
        remoteApps = json.load(open(os.path.join(cloudRoute, 'apps.json')))
        
        keyboard.add_hotkey('ctrl+shift+q', lambda: quitKH())
            
        if len(res) == 3:
            types = {
                '-f': '--force',
                '-y': '--yes'
            }
            for x in res[2:]:
                if x == list(types.keys())[0] or x == types[list(types.keys())[0]]:
                    force = True
                    ask()
                elif x == list(types.keys())[1] or x == types[list(types.keys())[1]]:
                    give()
                else:
                    pc()
                    print(f'{col.WARNING}Invalid argument! Types:{col.ENDC}')
                    break
        elif len(res) == 2:
            give() if ask() else desist()
        elif len(res) == 1:
            pc()
            res.append(input('Introduce your package you wish to install: '))
            if not exitHK:
                pc()
                give() if ask() else desist()