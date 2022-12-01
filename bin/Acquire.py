import os, json, keyboard
import urllib.request
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
                keyboard.unregister_hotkey('ctrl+x')
                keyboard.press('enter')
            except Exception: pass
        keyboard.add_hotkey('ctrl+x', lambda: quitKH())
        
        def give(f=False):
            if res[1] in remoteApps:
                if f or not res[1] in apps:
                    write()
                else:
                    global exitHK
                    if not exitHK:
                        pc(4)
                        pc(2)
                        print(f'{col.WARNING}App {res[1]} is already indexed{col.ENDC}')
                        pc(3)
                        i = input('Do you wish to reinstall it [Y/n]? ')
                        if not exitHK and (i == '' or i == 'n' or i == 'y'):
                            write() if i == 'y' or i == '' else desist()
                                
            elif not exitHK:
                pc()
                print(f'{col.WARNING}App {res[1]} is not indexed on my cloud{col.ENDC}')
            
        def write():
            with urllib.request.urlopen('https://raw.githubusercontent.com/LoXewyX/yvora_cloud/main/acquire/%s.py' % res[1].capitalize()) as url:
                with open('%s.py' % os.path.join(path, binfolder, res[1].capitalize()), 'w', encoding='utf-8') as f:
                    f.write(url.read().decode('utf-8').replace('\n', ''))
            pc()
            print('{}.py was created'.format(res[1].capitalize()))
            
            apps.update({res[1]: remoteApps[res[1]]})
            
            with open(os.path.join(path, srcfolder, 'apps.json'), 'w') as f:
                json.dump(apps, f, indent=4, sort_keys=True)
            pc()
            print('apps.json was updated')
        
        global remoteApps, exitHK
        exitHK = False
        pc()
        with urllib.request.urlopen('https://raw.githubusercontent.com/LoXewyX/yvora_cloud/main/apps.json') as url:
            remoteApps = json.load(url)
        
        if len(res) > 2:
            types = {
                '-f': '--force',
                '-y': '--yes'
            }
            
            f = False
            y = False
            
            for x in res[2:]:
                if x == list(types.keys())[0] or x == types[list(types.keys())[0]]:
                    f = True
                elif x == list(types.keys())[1] or x == types[list(types.keys())[1]]:
                    y = True
                else:
                    pc()
                    print(f'{col.WARNING}Invalid argument! Types:{col.ENDC}')
                    break
                
            give(f) if y or ask() else desist()
        
        elif len(res) == 2:
            give() if ask() else desist()
            
        elif len(res) == 1:
            pc()
            res.append(input('Introduce your package you wish to install: '))
            if not exitHK:
                pc()
                give() if ask() else desist()
