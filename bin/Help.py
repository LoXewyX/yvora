from utils.Colors import TerminalColors as col
from utils.Fancyprint import Fancyprint as pc
import utils.Fancyprint

class Help():
    def __init__(self, data, apps, res):
        
        utils.Fancyprint.data = data
        
        if len(res) == 1:
            pc(1)
            pc(2)
            print('Try typing \'help [program]\' or type \'help (--all or -a)\'')
            pc(3)
            print(f'{col.CYAN}REMEMBER!{col.ENDC} [ctrl + x] to escape on input functions')
        elif res[1] == '--all' or res[1] == '-a':
            pc(1)
            if len(apps) > 1:
                for i in list(apps.keys())[:-1]:
                    print('├─ %s → %s' % (i, apps.get(i)['help']))
            print('└─ %s → %s' % (list(apps.keys())[-1], apps.get(list(apps.keys())[-1])['help']))
                
        elif res[1] in apps:
            pc()
            print('%s → %s' % (res[1], apps.get(res[1])['help']))
        else:
            pc()
            print(f'{col.WARNING}I couldn\'t find {col.ENDC}{res[1]}')