import json, os
from utils.Colors import TerminalColors as col
from utils.Fancyprint import Fancyprint as pc
import utils.Fancyprint
from utils.RelpathSolver import get_route

class New():
    def __init__(self, data, res, srcfolder, binfolder, dirpath):
        
        utils.Fancyprint.data = data
            
        def new(proj, creator, guide, version, arguments):
            
            route = get_route(dirpath, srcfolder, 'apps.json')
            with open(route) as f:
                appdata = json.load(f)
                
            empty_args = len(arguments) == 1 and arguments[0] == ''
            
            appdata.update({proj.lower(): {
                'help': guide,
                'creator': creator,
                'version': version,
                'args': [] if empty_args else arguments
            }})
            
            with open(route, 'w') as f:
                json.dump(appdata, f, indent=4, sort_keys=True)
            
            if empty_args:
                arguments = 'self'
            else:
                arguments.insert(0, 'self')
                arguments = ', '.join(arguments)
            
            binpath = os.path.join(dirpath, '..', binfolder, '{}.py'.format(proj.capitalize()))
            with open(binpath, 'w') as f:
                f.write (
                'class {}():\n'.format(proj.capitalize()) +
                f'\tdef __init__({arguments}):\n' +
                f'\t\tprint(\'{proj} works!\') # your code goes here'
                )
            
            pc()
            print(proj.capitalize() + ' was created')
        
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
            
            proj = ''
            while proj == '':
                pc()
                proj = input(f'Type your project\'s name{col.RED}*{col.ENDC}: ')
            
            creator = ''
            while not exitHK and creator == '':
                pc()
                creator = input(f'creator{col.RED}*{col.ENDC}: ')
            
            if not exitHK:
                pc()
                guide = input('brief guide (help): ')
            
            version = ''
            while not exitHK and version == '':
                pc()
                version = input(f'version [N.N.N]{col.RED}*{col.ENDC}: ')
            
            if not exitHK:
                pc()
                arguments = [x.strip() for x in input('arguments [separated by comma]: ').split(',')]
            
            if not exitHK:
                new(proj, creator, guide, version, arguments)
            
        else:
            pc()
            print(f'{col.WARNING}new has too much arguments!{col.ENDC}')
