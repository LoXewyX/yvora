import os, json
from utils.Fancyprint import Fancyprint as pc
import utils.Fancyprint

class Pwd():
    def __init__(self, data, srcfolder, root):
        
        utils.Fancyprint.data = data
        
        route = os.path.join(
            os.path.dirname(os.path.abspath(__file__)
        ), '..', srcfolder, "metadata.json")
        
        with open(route) as f:
            data = json.load(f)
        
        pc()
        print(data['rootpath'] if root else '/%s%s' % (data['user'], data['dirpath']))