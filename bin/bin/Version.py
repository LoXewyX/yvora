from utils.Colors import TerminalColors as col
from utils.Fancyprint import Fancyprint as pc
import utils.Fancyprint

class Version:
    def __init__(self, data, apps, res):
        
        utils.Fancyprint.data = data
        
        if len(res) == 2:
            if res[1] in apps:
                name = apps.get(res[1])['version']
                pc()
                print('%s → %s' % (res[1], name if name != '' else 'unknown'))
            else:
                pc()
                print('I couldn\'t find program \'%s\'' % res[1])
        else:
            pc()
            print('Version requires only 1 argument')