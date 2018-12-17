# 7 kyu

# Write a function that takes an integer and returns an array [A, B, C], where:
# A is the number of multiples of 3 (but not 5) below the given integer
# B is the number of multiples of 5 (but not 3) below the given integer
# C is the number of multiples of 3 and 5 below the given integer.
# For example, solution(20) should return [5, 2, 1]


def solution(number):
    A = 0
    B = 0
    C = 0

    for i in range(1, number):
        if i % 3 == 0 and i % 5 != 0:
            A += 1
        if i % 3 != 0 and i % 5 == 0:
            B += 1
        if i % 3 == 0 and i % 5 == 0:
            C += 1

    print(f"A: {A}, B: {B}, C: {C}")
    return [A, B, C]


if __name__ == "__main__":
    solution(20)  # [5, 2, 1]
    solution(2)  # [0, 0, 0]
    solution(14)  # [4, 2, 0]
    solution(30)  # [8, 4, 1]
    solution(141)  # [37, 19, 9]
