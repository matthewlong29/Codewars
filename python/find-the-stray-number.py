# 7 kyu

# You are given an odd-length array of integers, in which all of them are the same, except for one single number.
# Complete the method which accepts such an array, and returns that single different number.
# The input array will always be valid! (odd-length >= 3)


def stray(arr):
    print(f"len(arr): {len(arr)}")
    if arr[len(arr) - 1] != arr[len(arr) - 2] and arr[len(arr) - 1] != arr[len(arr) - 3]:
        print(f"Odd number: {arr[len(arr) - 1]}")
        return arr[len(arr) - 1]
    for i in range(2, len(arr)):
        oddNum = arr[i - 2]
        if arr[i] != oddNum and arr[i - 1] != oddNum:
            print(f"Odd number: {oddNum}")
            return oddNum
        else:
            print(f"{arr[i]} is not odd.")
    print(f"Odd number: {oddNum}")
    return oddNum


if __name__ == "__main__":
    arr1 = [1, 1, 1, 1, 1, 1, 2]  # 2
    arr2 = [2, 3, 2, 2, 2]  # 3
    arr3 = [3, 2, 2, 2, 2]  # 3
    stray(arr1)
    print("---")
    stray(arr2)
    print("---")
    stray(arr3)
    print("---")
