# 6 kyu

# In this kata you have to write a simple Morse code decoder. While the Morse code is now mostly superceded by voice and digital data communication channels, it still has its use in some applications around the world.

# The Morse code encodes every character as a sequence of "dots" and "dashes". For example, the letter A is coded as .-, letter Q is coded as --.-, and digit 1 is coded as .----. The Morse code is case-insensitive, traditionally capital letters are used. When the message is written in Morse code, a single space is used to separate the character codes and 3 spaces are used to separate words. For example, the message HEY JUDE in Morse code is .... . -.--   .--- ..- -.. ..

# NOTE: Extra spaces before or after the code have no meaning and should be ignored.

# In addition to letters, digits and some punctuation, there are some special service codes, the most notorious of those is the international distress signal SOS (that was first issued by Titanic), that is coded as ...---.... These special codes are treated as single special characters, and usually are transmitted as separate words.

# Your task is to implement a function that would take the morse code as input and return a decoded human-readable string.


def getCharacter(morse_code):
    morseCodeLookup = {
        ".-": "a",
        "-...": "b",
        "-.-.": "c",
        "-..": "d",
        ".": "e",
        "..-.": "f",
        "--.": "g",
        "....": "h",
        "..": "i",
        ".---": "j",
        "-.-": "k",
        ".-..": "l",
        "--": "m",
        "-.": "n",
        "---": "o",
        ".--.": "p",
        "--.-": "q",
        ".-.": "r",
        "...": "s",
        "-": "t",
        "..-": "u",
        "...-": "v",
        ".--": "w",
        "-..-": "x",
        "-.--": "y",
        "--..": "z",
        ".----": "1",
        "..---": "2",
        "...--": "3",
        "....-": "4",
        ".....": "5",
        "-....": "6",
        "--...": "7",
        "---..": "8",
        "----.": "9",
        "-----": "0",
        "...---...": "SOS",
        "-.-.--": "!",
        ".-.-.-": "."
    }
    return morseCodeLookup.get(morse_code)


def decodeMorse(morse_code):
    morseCode = morse_code.strip().replace("   ", " + ")  # let space be "+"
    keys = morseCode.split(" ")
    result = ""
    for key in keys:
        if key is "+":
            result += " "
        else:
            result += getCharacter(key)
    print("[{}] translates to [{}]!").format(morse_code, result)
    return result.upper().strip()


if __name__ == "__main__":
    decodeMorse(".... . -.--   .--- ..- -.. .")  # "HEY JUDE"
    decodeMorse("...---...")  # SOS
    # "SOS! THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG."
    decodeMorse("      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-  ")
