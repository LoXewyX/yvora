import os
from utils.Colors import TerminalColors as col
from utils.Fancyprint import Fancyprint as pc
import utils.Fancyprint

class Run():
    def __init__(self, data, res):
        
        utils.Fancyprint.data = data
        
        pc(4)
        pc(5)
        print(f'{col.WARNING}Disclaimer{col.ENDC}')
        pc(6)
        print('All commands are provided from your OS')
        os.system(' '.join(res[1:]))