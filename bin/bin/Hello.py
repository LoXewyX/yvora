from utils.Fancyprint import Fancyprint as pc
import utils.Fancyprint

class Hello():
    def __init__(self, data):
        import random
        
        utils.Fancyprint.data = data
        pc()
        print(
            random.choice([
                'How\'s it going?',
                'Hey',
                'What\'s up',
                'Sup',
                'Hi',
                'How are you',
                'What\'s new',
                'Nice to see you',
                'How\'s everything'
            ])
        )