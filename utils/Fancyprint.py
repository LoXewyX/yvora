from utils.Colors import TerminalColors as col

data = {
    'pc': '?pc'
}

def Fancyprint(style=0):
    if style == 0:
        print('%s%s%s ├┐' % (col.GREEN, data['pc'], col.ENDC))
        print('┌' + '─' * (len(data['pc']) + 1) + '┘')
        print('└┤ ', end='')
        
    elif style == 1:
        print('%s%s%s ├┐' % (col.GREEN, data['pc'], col.ENDC))
        print('┌' + '─' * (len(data['pc']) + 1) + '┘')
    
    elif style == 2:
        print('├┤ ', end='')
    
    elif style == 3:
        print('└┤ ', end='')
    
    elif style == 4:
        print('%s%s%s ├┐' % (col.GREEN, data['pc'], col.ENDC))
        print('┌' + '─' * (len(data['pc']) + 1) + '┘')
        
    elif style == 5:
                print('├─ ', end='')
            
    elif style == 6:
        print('└─ ', end='')
        
    elif style == 7:
        print('│')
        
def graffiti(version):      
        
    print(
        '   __ __ _____ _____ _____ _____\n' +
        '  |  |  |  |  |     | __  |  _  |\n' +
        '  |_   _|  |  |  |  |    -|     |\n' +
        '    |_|  \___/|_____|__|__|__|__|\n\n' +
        '  v%s' % version
    )