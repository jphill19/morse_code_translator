import re

morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',
    '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ':'  ', # The space key is so I can add spaces between words
}


def decode_morse(input_string: str):
    """Translate a string of Morse Code into English"""
    output_string = ''
    for letter in input_string.split(' '):
        if letter not in morse_code_dict.values():
            output_string += ' '
            continue
        
        if letter == '':
            output_string += ' '
            continue
        # The following line converts the morse_code_dict to a list, then finds the index of the letter in the list, then finds the key at that index
        output_string += list(morse_code_dict.keys())[list(morse_code_dict.values()).index(letter)]



    output_string = re.sub(' +', ' ', output_string)
    
    return output_string

def encode_to_morse(input_string: str):
    """Translate a string into Morse Code"""
    output_string = ''
    for letter in input_string:
        if letter.upper() not in morse_code_dict.keys():
            output_string += ' '
            continue
        output_string += morse_code_dict[letter.upper()] + ' '
    return output_string

