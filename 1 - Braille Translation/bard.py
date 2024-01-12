def solution(plaintext):
    # Create a dictionary mapping lowercase letters to their Braille representations
    braille_chars = {
        "a": "100000",
    "b": "110000",
    "c": "100100",
    "d": "100110",
    "e": "100010",
    "f": "110100",
    "g": "110110",
    "h": "110010",
    "i": "010100",
    "j": "010110",
    "k": "101000",
    "l": "111000",
    "m": "101100",
    "n": "101110",
    "o": "101010",
    "p": "111100",
    "q": "111110",
    "r": "111010",
    "s": "011100",
    "t": "011110",
    "u": "101001",
    "v": "111001",
    "w": "010111",
    "x": "101101",
    "y": "101111",
    "z": "101011"
    }

    # Add a capital mark to uppercase letters
    braille_chars_upper = {
        chr(ord('A') + i): '000001'+braille_chars[chr(ord('a') + i)] 
        for i in range(26)
    }

    # Convert the input text to Braille
    translated_braille = []
    for char in plaintext:
        if char.islower():
            translated_braille.append(braille_chars[char])
        elif char.isupper():
            translated_braille.append(braille_chars_upper[char])
        else:
            # Handle spaces
            translated_braille.append('000000')

    # Concatenate the Braille representations into a single string
    translated_braille_string = ''.join(translated_braille)

    return translated_braille_string
