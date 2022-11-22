import keyboard
import json
import os.path
from os import remove as rm
from utils.Colors import TerminalColors as col
from utils.Fancyprint import Fancyprint as pc
import utils.Fancyprint

class Purge():
    def __init__(self, data, apps, res, path, binfolder, srcfolder):
        
        utils.Fancyprint.data = data
        
        def ask():
            i = 'foo'
            while not (i == 'y' or i == 'n' or i == ''):
                pc()
                i = input('Are you sure you want to purge package %s [Y/n]: ' % res[1])
            return True if i == 'y' or i == '' else False
        
        def desist():
            pc()
            print('Understood...')
        
        def invalid(types):
            pc(1)
            pc(5)
            print(f'{col.WARNING}Invalid argument!{col.ENDC}')
            pc(5)
            print(f'{col.WARNING}Types are:{col.ENDC}')
            index = 0
            pc(7)
            if len(types) > 1:
                for k in list(types.keys())[:-1]:
                    pc(5)
                    print(f'{k} / {types[k]}{col.ENDC}')
                    index += 1
            if len(types) >= 1:
                pc(6)
                print(f'{list(types.keys())[-1]} / {types[list(types.keys())[-1]]}{col.ENDC}')
            else:
                pc(6)
                print('None')
        
        def quitKH():
            global exitHK
            exitHK = True
            try:
                keyboard.unregister_hotkey('ctrl+x')
                keyboard.press('enter')
            except Exception: pass
        
        def erase():
            global force
            if res[1] in apps or force:
                filepath = os.path.join(path, binfolder, '%s.py' % res[1].capitalize())
                appspath = os.path.join(path, srcfolder, 'apps.json')
                try:
                    d_temp = apps
                    del d_temp[res[1]]
                    with open(appspath, 'w') as f: 
                        json.dump(d_temp, f, indent=4)
                    pc()
                    print('apps.json was updated')
                except:
                    if not force:
                        pc()
                        print(f'{res[1]} {col.WARNING}is not indexed on apps.json{col.ENDC}')
                    
                if os.path.exists(filepath):
                    rm(filepath)
                    pc()
                    print('App %s was removed' % res[1])
                else:
                    pc()
                    print('{0}App {2}{1}{0} does not exist{2}'.format(col.WARNING, res[1], col.ENDC))
                    
            else:
                pc(1)
                pc(5)
                print('{0}App {2}{1}{0} is not indexed{2}'.format(col.WARNING, res[1], col.ENDC))
                pc(6)
                print('{0}Add parameter {1}-f or --force{0} to force it\'s uninstallation{1}'.format(col.WARNING, col.ENDC))
        
        global force, exitHK
        force = False
        exitHK = False
        noAsk = False
        
        keyboard.add_hotkey('ctrl+x', lambda: quitKH())
        
        if len(res) >= 3:
            types = {
                '-f': '--force',
                '-y': '--yes'
            }
            
            def compareList(l1, l2):
                try:
                    for i in l1:
                        l2.remove(i)
                        return True
                except:
                    return False
            
            if compareList(res[2:], list(types.keys())) or compareList(res[2:], list(types.values())):
                for x in res[2:]:
                    if x == list(types.keys())[0] or x == types[list(types.keys())[0]]:
                        force = True                
                    if x == list(types.keys())[1] or x == types[list(types.keys())[1]]:
                        noAsk = True
                erase() if noAsk else (erase() if ask() else desist())
            else: invalid(types) 
            
        elif len(res) == 2:
            erase() if ask() else desist()
        elif len(res) == 1:
            pc()
            res.append(input('Introduce your package you wish to purge: '))
            if not exitHK:
                pc()
                erase() if ask() else desist()
            