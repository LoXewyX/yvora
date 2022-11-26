from utils.Colors import TerminalColors as col
from utils.Fancyprint import Fancyprint as pc
import utils.Fancyprint
import getpass
import os
from cryptography.fernet import Fernet
import keyboard
from pick import pick
import hashlib

import interface

class Cypher():
    def __init__(self, data, res, dirpath, root):
        
        utils.Fancyprint.data = data
        
        global keypath
        keypath = os.path.join(dirpath, 'etc', 'cypher', '.key')
        
        def encrypt():
            global keypath, abspath
            files = []

            for f in os.listdir(abspath):
                f = os.path.join(abspath, f)
                if os.path.isfile(f):
                    files.append(f)
            print(files)

            key = Fernet.generate_key()

            with open(keypath, 'wb') as k:
                k.write(key)

            for f in files:
                with open(f, 'rb') as k:
                    c = k.read()
                e = Fernet(key).encrypt(c)
                with open(f, 'wb') as k:
                    k.write(e)
            print('Encripted')
        
        def decrypt():
            global keypath, abspath
            files = []

            for f in os.listdir(abspath):
                f = os.path.join(abspath, f)
                if os.path.isfile(f):
                    files.append(f)
            print(files)

            with open(keypath, 'rb') as key:
                sk = key.read()

                for f in files:
                    with open(f, 'rb') as k:
                        c = k.read()
                    d = Fernet(sk).decrypt(c)
                    with open(f, 'wb') as k:
                        k.write(d)
            print('Decripted')
        
        # --------------------------------
        
        def auth():
            MAXATTEMPTS = interface.MAXATTEMPTS
            attempts = interface.attempts
            global exitHK
            
            # Main loop
            while not exitHK:
                if attempts > 0:
                    if not exitHK:
                        def pwd():
                            if data['password'] == False: return True
                            pc(1)
                            msgpw = '└┤ Secret password [%i / %i attempts]: ' % (attempts, MAXATTEMPTS)
                            i = getpass.getpass(msgpw)
                            return hashlib.sha512(i.encode()).hexdigest() == data['password']
                        
                        if root or pwd(): return True
                        elif not exitHK:
                            attempts -= 1
                            interface.attempts = attempts
                            pc()
                            print(f'{col.WARNING}This password is not valid for me {col.ENDC}')
                else:
                    pc()
                    print('I think you are acting very suspicious, so I\'m afraid you can no longer enter the password')
                    exitHK = True
        
        def checkpath(path):
            global abspath
            userpath = dirpath if root else os.path.join(dirpath, data['user'])
            osfolders = path[1:] if path.startswith('/') or path.startswith('\\') else path
            
            if path.startswith('/') or path.startswith('\\'):
                relpath = os.path.abspath(
                    os.path.join(userpath, osfolders)
                )
            else:
                relpath = os.path.abspath(os.path.join(userpath, data['rootpath' if root else 'dirpath'][1:], osfolders))
            abspath = relpath
            return os.path.exists(relpath) and relpath.startswith(userpath)
        
        if len(res) == 1:
            global exitHK
            exitHK = False
            
            def quitKH():
                try:
                    global exitHK
                    exitHK = True
                    keyboard.unregister_hotkey('ctrl+x')
                    keyboard.press('enter')
                    print(f'\n{col.RED}escaped{col.ENDC}', end='')
                except Exception: pass
            keyboard.add_hotkey('ctrl+x', lambda: quitKH())
            
            def path():
                cypherpath = ''
                if not exitHK:
                    pc()
                    cypherpath = input(f'Type your path you wish to cypher{col.RED}*{col.ENDC}: ')
                    global valid
                if not exitHK and (cypherpath == '' or not checkpath(cypherpath)):
                    pc()
                    print(f'{col.WARNING}Invalid route{col.ENDC}')
                    path()
                else: return cypherpath
                
            def ask(opt):
                global abspath
                i = input (
                    f'Are you sure you want to {opt} your files on path?\n' +
                    f'{col.CYAN}Absolute path:{col.ENDC}\t\'{abspath}\'\n' +
                    f'{col.CYAN}Key path:{col.ENDC}\t\'{keypath}\'\n'
                    'Choose [y/N]: '
                )
                if i == 'y':
                    return True
                elif i == '' or i == 'n':
                    return False
                else:
                    ask(opt, path)
            
            if not exitHK:
                if not exitHK:
                    path = path()
                if not exitHK:
                    option = pick(['Encrypt', 'Decrypt', 'Exit'], 'Cypher menu', indicator='>', default_index=0)[0]
                    if option == 'Exit': exitHK = True
                    
                if auth() and ask(option.lower()):
                    locals()[option.lower()]()
                        
            # Encrypt
            
            

            # # Decrypt

            
            
        else:
            pc()
            print(f'{col.WARNING}cypher must contain no arguments{col.ENDC}')


