# 6 kyu

# Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.


def spinWords(sentence):
    newSentence = ""
    for word in sentence.split(" "):
        if (len(word) > 4): newSentence += word[::-1]
        else: newSentence += word
    print(newSentence.strip())
    return newSentence.strip()

if __name__ == "__main__":
    spinWords("Hey fellow warriors")  # "Hey wollef sroirraw"
    spinWords("This is a test")  # "This is a test"
    spinWords("This is another test")  # "This is rehtona test"
