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
            
            appdata.update({proj.lower(): {
                'help': guide,
                'creator': creator,
                'version': version,
                'args': arguments
            }})
            
            with open(route, 'w') as f:
                json.dump(appdata, f, indent=4, sort_keys=True)
            
            arguments.insert(0, 'self')
            
            binpath = os.path.join(dirpath, '..', binfolder, f'{proj.capitalize()}.py')
            with open(binpath, 'w') as f:
                f.write (
                f'class {proj.capitalize()}():\n' +
                '\tdef __init__(%s):\n' % ', '.join(arguments) +
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
                except Exception: pass
                
            keyboard.add_hotkey('ctrl+x', lambda: quitKH())
            pc()
            proj = input('Type your project\'s name: ')
            
            if not exitHK:
                pc()
                creator = input('creator: ')
            
            if not exitHK:
                pc()
                guide = input('brief guide (help): ')
                
            if not exitHK:
                pc()
                version = input('version [N.N.N]: ')
                
            if not exitHK:
                pc()
                arguments = [x.strip() for x in input('arguments [separated by comma]: ').split(',')]
            
            if not exitHK:
                new(proj, creator, guide, version, arguments)
            
        else:
            pc()
            print(f'{col.WARNING}new has too much arguments!{col.ENDC}')
