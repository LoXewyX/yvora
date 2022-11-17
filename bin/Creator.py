from utils.Colors import TerminalColors as col
from utils.Fancyprint import Fancyprint as pc
import utils.Fancyprint

class Creator:
    def __init__(self, data, apps, res):
        
        utils.Fancyprint.data = data
        
        if len(res) == 2:
            if res[1] in apps:
                name = apps.get(res[1])['creator']
                pc()
                print('%s by %s' % (res[1], name if name != '' else 'unknown'))
            else:
                pc()
                print(f'{col.WARNING}I couldn\'t find program {col.ENDC}{res[1]}')
        else:
            pc()
            print(f'{col.WARNING}Creator requires only 1 argument{col.ENDC}')