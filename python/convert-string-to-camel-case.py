# 6 kyu

# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized. 

def to_camel_case(text):
    text = text.replace("-", " ").replace("_", " ")
    words = text.split(" ")
    camelCase = ""
    for i in range(len(words)):
      if i is 0:
        camelCase += words[0]
      else:
        letters = list(words[i])
        letters[0] = letters[0].upper()
        letters = "".join(letter for letter in letters)
        camelCase += letters
    print(camelCase)

if __name__ == "__main__":
    to_camel_case('') # 
    to_camel_case("the_stealth_warrior") # "theStealthWarrior" 
    to_camel_case("The-Stealth-Warrior") # "TheStealthWarrior" 
    to_camel_case("A-B-C") # "ABC"