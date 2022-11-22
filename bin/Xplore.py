import webbrowser
from utils.Colors import TerminalColors as col
from utils.Fancyprint import Fancyprint as pc
import utils.Fancyprint

class Xplore():
    def __init__(self, data, res):
        
        def redirect(res):
            URL = res[1] if 'www' in res[1] else 'www.%s' % res[1]
            webbrowser.get().open(URL)
        
        utils.Fancyprint.data = data
        
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
            d = input('Now, type your URL: ')
            
            if not exitHK:
                redirect(d)
        
        elif len(res) == 2:
            redirect(res)
            
        else:
            pc()
            print(f'{col.WARNING}cd must contain 1 argument{col.ENDC}')