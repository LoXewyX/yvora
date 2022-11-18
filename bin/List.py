import re
from utils.Colors import TerminalColors as col
from utils.Fancyprint import Fancyprint as pc
import utils.Fancyprint
class List():
    def __init__(self, data, apps, res):
        
        utils.Fancyprint.data = data
        
        def printList(type):
            if type == 0:
                if len(apps) > 1:
                    for x in list(apps.keys())[:-1]: print('├─ %s' % x)
                print('└─ %s' % list(apps.keys())[-1])
                
            else:
                if type == 2:
                    c = 0
                if type == 1 or type == 2:
                    store = {}
                
                ignorePrint = False
                
                for x in apps:
                    try:
                        if res[1] == '--all' or re.findall(res[1], x):
                            if type == 1:
                                c = 0
                                if res[1] == '--all':
                                    store.update({x: 'e'})
                                else:
                                    store.update({x: 'e'} if x in res[1] else {x: 'i'})
                            elif type == 2:
                                if int(res[index+1]) > c:
                                    store.update({x: 'e'} if x in res[1] else {x: 'i'})
                                    c+=1
                                else: break
                            elif type == 3 and x in res[1]:
                                print('└─ %s' % x)
                                
                    except Exception:
                        error(type)
                        ignorePrint = True
                        break
                
                if not ignorePrint and type == 1 or type == 2:
                    if len(store) > 1:
                        for x in list(store.keys())[:-1]:
                            print(('├─ %s' % x) if store[x] == 'e' else ('╞═ %s' % x))
                    if len(store) != 0:
                        print('└─' if store[list(store.keys())[-1]] == 'e' else '╘═', list(store.keys())[-1])
                    else: print('└─', f'{col.WARNING}I couldn\'t find {col.ENDC}{res[1]}')
        
        def error(type):
            if type == 1:
                print('├─', f'{col.WARNING}I can\'t understand you...{col.ENDC}')
                print('├─', f'{col.WARNING}Please use the properly regex functions{col.ENDC}')
                print('├─', f'{col.CYAN}If you want to learn how regex works:{col.ENDC}')
                print('└─', 'https://www3.ntu.edu.sg/home/ehchua/programming/howto/Regexe.html')
            elif type == 2:
                print(f'{col.WARNING}-l or --limit argument must contain an integer number next to{col.WARNING}')
                
        
        if len(res) == 1:
            pc(4)
            printList(0)
            
        elif len(res) == 2:
            pc(4)
            printList(1)
            
        else:
            types = {
                '-l': '--limit',
                '-e': '--exact',
            }
            index = 2
            ignoreArgument = False
            for x in res[2:]:
                if ignoreArgument:
                    ignoreArgument = False
                else:
                    if x == list(types.keys())[0] or x == types[list(types.keys())[0]]:
                        pc(4)
                        printList(2)
                        ignoreArgument = True
                        break
                    elif x == list(types.keys())[1] or x == types[list(types.keys())[1]]:
                        pc(4)
                        printList(3)
                        break
                    else:
                        import json
                        print('Invalid arguments! Valids:')
                        print(json.dumps(types, indent = 4))
                        
                index += 1