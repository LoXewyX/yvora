import importlib
import os
import json
import getpass
import keyboard
import socket

from utils.Colors import TerminalColors as col
from utils.Fancyprint import Fancyprint as msg
from utils.Fancyprint import graffiti as graffiti
import utils.Fancyprint

global restart, root
restart = False
root = False

class Interface():
    def __init__(self):

        # Libraries
        def getJSON(name):
            global srcfolder
            return open(
                os.path.join(
                    filepath,
                    srcfolder,
                    '%s.json' % name
                )
            )
            
        def refresh():
            global data, srcfolder, path
            
            # metadata
            data = json.load(getJSON('metadata'))
            data.update({'hostname': socket.gethostname()})
            
            with open(os.path.join(filepath, srcfolder, 'metadata.json'), 'w') as f:
                json.dump(data, f, indent=4)
            
            # unbinds
            try:
                keyboard.unregister_hotkey('ctrl+x')
            except Exception: pass
            
            # load modules
            

        def response(res_r):
            
            # Not indexed:
            # exit
            # passwd
            # reload
            # su
            
            for res_idx in range(len(res_r)):
                res = res_r[res_idx].split()
            
                if len(res) != 0:
                    global data, cliexit, apps, root
                    appCap = res[0].capitalize()
                    
                    if res[0] == 'exit':
                        if not root:
                            msg()
                            print(f'{col.CYAN}Goodbye{col.ENDC} 👋')
                            cliexit = True
                        else: root = False
                        
                    elif res[0] == 'reload':
                        if root:
                            global restart
                            restart = cliexit = True
                        else:
                            msg()
                            print(f'{col.WARNING}You are not a root user{col.ENDC}')
                        
                    elif res[0] == 'su' or res[0] == 'passwd':
                        global attempts, exitHK
                        exitHK = False
                        import hashlib
                        
                        # Main loop
                        while not exitHK:
                            if attempts > 0:
                                if not exitHK:
                                    def quitKH():
                                        global exitHK, pwdThread
                                        exitHK = True
                                        try:
                                            keyboard.unregister_hotkey('ctrl+x')
                                            keyboard.press('enter')
                                        except Exception: pass
                                    keyboard.add_hotkey('ctrl+x', lambda: quitKH())
                                    
                                    def pwd():
                                        global data
                                        if data['password'] == False: return True
                                        msg()
                                        msgpw = 'Secret password [%i / %i attempts]: ' % (
                                            attempts, MAXATTEMPTS
                                        )
                                        i = getpass.getpass(msgpw)
                                        return hashlib.sha512(i.encode()).hexdigest() == data['password']
                                    
                                    if root or pwd():
                                        if res[0] == 'su':
                                            if root:
                                                msg()
                                                print(f'{col.WARNING}You\'re already a root user{col.ENDC}')
                                            else: root = True
                                            attempts = MAXATTEMPTS
                                            exitHK = True
                                        elif res[0] == 'passwd':
                                            if not exitHK:
                                                msg()
                                                newpwd = getpass.getpass('Type me a new password: ')
                                            if not exitHK:
                                                msg()
                                                newpwdconf = getpass.getpass('Confirm it please: ')
                                            while not exitHK and newpwd != newpwdconf:
                                                msg()
                                                newpwd = getpass.getpass('Retype it please: ')
                                                if not exitHK:
                                                    msg()
                                                    newpwdconf = getpass.getpass('Confirm it please: ')
                                            if not exitHK and newpwd == newpwdconf:
                                                with open(os.path.join(filepath, srcfolder, 'metadata.json')) as f:
                                                    data = json.load(f)
                                                data['password'] = False if newpwd == '' else hashlib.sha512(newpwd.encode()).hexdigest()
                                                with open(os.path.join(filepath, srcfolder, 'metadata.json'), 'w') as f:
                                                    json.dump(data, f, indent=4)
                                                exitHK = True
                                    else:
                                        if not exitHK:
                                            attempts -= 1
                                            msg()
                                            print(f'{col.WARNING}This password is not valid for me {col.ENDC}')
                            else:
                                msg()
                                print('I think you are acting very suspicious, so  I\'m afraid you can no longer enter the password')
                                exitHK = True
                    # Extra args
                    elif res[0] in apps:  
                        try:
                            run = getattr(importlib.import_module('%s.%s' % (binfolder, appCap)), appCap)
                            args = []
                            for x in apps[res[0]]['args']:
                                args.append(eval('%s' % x))
                            run(*args)
                            
                        except Exception as ex:
                            msg(1)
                            msg(2)
                            print('{0}Command {1}{2}{0} is not working properly!{1}'.format(col.WARNING, col.ENDC, res[0]))
                            msg(3)
                            print(f'{col.WARNING}Please contact with the creator or try to reinstall it{col.ENDC}')
                            msg()
                            print(f'{col.RED}{ex}{col.ENDC}')
                        
                    else:
                        msg(1)
                        msg(2)
                        print('{0}Command {1}{2}{0} is not indexed on my database{1}'.format(col.WARNING, col.ENDC, res[0]))
                        msg(3)
                        print(f'{col.WARNING}Type {col.ENDC}list{col.WARNING} if you are lost{col.ENDC}')

        # Pool
        
        global attempts, root, data, cliexit, srcfolder, apps, dirpath
        
        cliexit     = False
        MAXATTEMPTS = 5
        attempts    = MAXATTEMPTS
        binfolder   = 'bin'
        srcfolder   = 'src'
        
        filepath    = os.path.dirname(os.path.abspath(__file__))
        apps        = json.load(getJSON('apps'))
        data        = json.load(getJSON('metadata'))
        
        dirpath    = os.path.join(filepath, 'root')

        appname     = data['appname']

        # Main loop
        
        utils.Fancyprint.data = data
        
        msg(1)
        msg(2)
        print(f'Welcome to {appname}')
        msg(3)
        print(f'A Python\'s exclusive terminal by LoXewyX{col.GREEN}')
        
        graffiti()
        print(col.ENDC)

        while not cliexit:
            refresh()
            print('┌' + '─' * (2 + (4 if root else len(data['user'])) + 1 + len(data['hostname']) + 2) + '┐')
            print('└┤ {0}@{1} [{2}] {3} '.format
                (
                    f'{col.RED}root{col.ENDC}' if root else data['user'],
                    data['hostname'],
                    f'{col.RED}#{col.ENDC}' if root else f'{col.GREEN}${col.ENDC}',
                    '{0}{1}{2}'.format(col.GRAY, data['rootpath'] if root else data['dirpath'], col.ENDC)
                ),
                end=''
            )
            
            response(input().split('&&'))