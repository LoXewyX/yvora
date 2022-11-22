import os, json

def get_route(dirpath, srcfolder):
    return os.path.join(dirpath, '..', srcfolder, "metadata.json")

def get_userpath(dirpath, data, root):
    return dirpath if root else os.path.join(dirpath, data['user'])

def get_relpath(res, dirpath, srcfolder, root):
    route = get_route(dirpath, srcfolder)
    
    with open(route) as f:
        data = json.load(f)
        
    userpath = get_userpath(dirpath, data, root)
    osfolders = res[1][1:] if res[1].startswith('/') or res[1].startswith('\\') else res[1]
    
    if res[1].startswith('/') or res[1].startswith('\\'):
        return os.path.abspath(
            os.path.join(userpath, osfolders)
        )
    else:
        return os.path.abspath(os.path.join(userpath, data['rootpath' if root else 'dirpath'][1:], osfolders))
    