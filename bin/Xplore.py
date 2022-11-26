import webbrowser
from utils.Colors import TerminalColors as col
from utils.Fancyprint import Fancyprint as pc
import utils.Fancyprint

class Xplore():
    def __init__(self, data, res):
        
        def redirect(txt):
            URL = txt if 'www' in txt else f'www.{txt}'
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
                    print(f'\n{col.RED}escaped{col.ENDC}')
                except Exception: pass
            keyboard.add_hotkey('ctrl+x', lambda: quitKH())
            
            pc()
            d = input('Now, type your URL: ')
            
            if not exitHK:
                redirect(d)
        
        elif len(res) == 2:
            redirect(res[1])
            
        else:
            pc()
            print(f'{col.WARNING}cd must contain 1 argument{col.ENDC}')
