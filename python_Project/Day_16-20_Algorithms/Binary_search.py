def bin_search(items, key):
    """折半查找"""
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if key > items[mid]:
            start = mid + 1
        elif key < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1


if __name__ == '__main__':

    items = [2, 3, 4, 10, 40]
    key = 10

    # Function call
    result = bin_search(items, key)
    if result != -1:
        print("Element is present at index % d" % result)
    else:
        print("Element is not present in array")