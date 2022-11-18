from utils.Fancyprint import Fancyprint as pc
import utils.Fancyprint

class Supersede:
    def __init__(self, data):
        
        utils.Fancyprint.data = data
        
        pc()
        print('Supersede works!')