from utils.Colors import TerminalColors as col
from utils.Fancyprint import Fancyprint as pc
import utils.Fancyprint

class Setname():
    def __init__(self, data, res, srcfolder):
        
        utils.Fancyprint.data = data
        
        def noEmoji(txt):
            import re
            emoj = re.compile("["
                u"\U0001F600-\U0001F64F"
                u"\U0001F300-\U0001F5FF"
                u"\U0001F680-\U0001F6FF"
                u"\U0001F1E0-\U0001F1FF"
                u"\U00002500-\U00002BEF"
                u"\U00002702-\U000027B0"
                u"\U00002702-\U000027B0"
                u"\U000024C2-\U0001F251"
                u"\U0001f926-\U0001f937"
                u"\U00010000-\U0010ffff"
                u"\u2640-\u2642" 
                u"\u2600-\u2B55"
                u"\u200d"
                u"\u23cf"
                u"\u23e9"
                u"\u231a"
                u"\ufe0f"
                u"\u3030"
            "]+", re.UNICODE)
            return re.sub(emoj, '', txt)
        
        if len(res) == 3:
            res[2] = noEmoji(res[2])
            print(res[1])
            if res[1] == 'pc' or res[1] == 'user':
                import os, json
                route = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', srcfolder, "metadata.json")
                with open(route) as f:
                    data = json.load(f)
                    
                if res[1] == 'pc':
                    data['pc'] = res[2]
                    pc()
                    print('My name was changed to \'%s\'' % res[2])
                else:
                    data['user'] = res[2]
                    pc()
                    print('Your name was changed to \'%s\'' % res[2])
                
                with open(route, 'w') as f:
                    json.dump(data, f, indent=4)
            else:
                pc()
                print('{col.WARNING}The only existent users are {col.ENDC}pc {col.WARNING}and{col.ENDC} user')
        else:
            pc()
            print('{col.WARNING}Setname requires only 2 arguments{col.ENDC}')