# 6 kyu

# Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which are substrings of strings of a2.


def in_array(wordsOne, wordsTwo):
    substrings = []
    for wordOne in wordsOne:
        for wordTwo in wordsTwo:
            if wordTwo.__contains__(wordOne):
                if wordOne not in substrings:
                    print(f"{wordOne} in {wordsTwo}")
                    substrings.insert(0, wordOne)
    substrings.sort()
    print(f"substrings: {substrings}")
    return substrings


if __name__ == "__main__":
    wordsOne = ["live", "arp", "strong"]
    wordsTwo = ["lively", "alive", "harp", "sharp", "armstrong"]
    in_array(wordsOne, wordsTwo)  # ['arp', 'live', 'strong']
