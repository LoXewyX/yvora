from utils.Colors import TerminalColors as col
from utils.Fancyprint import Fancyprint as pc
import utils.Fancyprint

class X:
    def __init__(self, data):
        
        utils.Fancyprint.data = data
        
        pc()
        print('X works!')