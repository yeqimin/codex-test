def binary_search(numbers, target):
    """Return the index of target in a sorted list, or -1 when absent."""
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2
        guess = numbers[mid]

        if guess == target:
            return mid
        if guess < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    values = [1, 3, 5, 7, 9, 11, 13]
    print(binary_search(values, 7))
    print(binary_search(values, 7))