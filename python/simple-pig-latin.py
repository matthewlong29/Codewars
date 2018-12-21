# 5 kyu
# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

def pig_it(text):
    words = text.split(" ")
    sentence = ""
    print(text)
    for word in words:
        letters = list(word)
        if letters[0] in "!@#$%^&*().,;\"':?":
            sentence += " " + letters[0]
            continue
        letters.insert(len(letters), letters[0])
        letters[0] = " "
        sentence += "".join(letter for letter in letters) + "ay"
    print(sentence.strip())
    return sentence.strip()


if __name__ == "__main__":
    pig_it('Pig latin is cool') # 'igPay atinlay siay oolcay'
    pig_it('This is my string') # 'hisTay siay ymay tringsay'
    pig_it('This a my string !') # 'hisTay siay ymay tringsay'
    pig_it('Hello world !') # elloHay orldway !
