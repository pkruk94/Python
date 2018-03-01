mors = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
     	'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.',  '.': '.-.-.-', ',': '--..--',
        '?': '..--..', '!': '-.-.--', ' ': '//'
        }

alfabet = {y:x for x,y in mors.items()} #odwrócony słownik morsa


def szyfruj(plik):
    zaszyfrowana = []
    wiad = open(plik).read().strip()
    for i in wiad:
        zaszyfrowana.append(mors[i.upper()])
    zaszyfrowana = ' '.join(zaszyfrowana)
    print(zaszyfrowana)

def deszyfruj(plik):
    odszyfrowana = []
    wiad = open(plik).read().strip().split(' ')
    for i in wiad:
        odszyfrowana.append(alfabet[i])
    odszyfrowana = ''.join(odszyfrowana)
    print(odszyfrowana)

