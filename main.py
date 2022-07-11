def binary_search(ur_list, item):
    low = 0
    high = len(ur_list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = ur_list[mid]

        if guess == item:
            return mid

        if guess > item:
            high = mid - 1

        else:
            low = mid + 1
    return None


test_list = []
for i in range(1, 101):
    test_list.append(i)
print(binary_search(test_list, 6))