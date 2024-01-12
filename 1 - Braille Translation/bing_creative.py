# A dictionary that maps each lowercase letter to its Braille representation
braille_dict = {
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

# A constant that represents the Braille capitalization mark
CAPITAL_MARK = "1"

# A constant that represents the Braille blank character
BLANK_CHAR = "000000"

def solution(plaintext):
    # Initialize an empty string to store the output
    output = ""
    # Loop through each character in the plaintext
    for char in plaintext:
        # If the character is a space, append the blank character to the output
        if char == " ":
            output += BLANK_CHAR
        # If the character is uppercase, append the capitalization mark and the corresponding Braille representation to the output
        elif char.isupper():
            output += braille_dict[char.lower()] + CAPITAL_MARK
        # If the character is lowercase, append the corresponding Braille representation to the output
        elif char.islower():
            output += braille_dict[char]
    # Return the output string
    return output