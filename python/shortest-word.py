# 7 kyu

# Simple, given a string of words, return the length of the shortest word(s).
# String will never be empty and you do not need to account for different data types.


def find_short(s):
    print(f"s: {s}")
    words = s.split()
    print(f"words: {words}")
    # let first word initially be shortest
    currentShortest = len(list(words[0]))

    for i in range(len(words)):
        if len(list(words[i])) < currentShortest:
            currentShortest = len(list(words[i]))

    print(
        f"Shortest word is {currentShortest} characters long!"
    )
    return currentShortest


if __name__ == "__main__":
    find_short("bitcoin take over the world maybe who knows perhaps")  # 3
    find_short("lets talk about javascript the best language")  # 3
    find_short("i want to travel the world writing code one day")  # 1
    find_short("Lets all go on holiday somewhere very cold")  # 2
