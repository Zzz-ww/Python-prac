def select_sort(items):
    """简单选择排序"""
    compare = lambda x, y: x < y
    # Traverse through all array elements
    for i in range(len(items) - 1):
        min_idx = i
        for j in range(i + 1, len(items)):

            # Find the minimum element in remaining
            # unsorted array
            if compare(items[j], items[min_idx]):
                min_idx = j
        # Swap the found minimum element with
        # the first element
        items[i], items[min_idx] = items[min_idx], items[i]
    return items


def main():
    items = [64, 25, 12, 22, 11]
    print(select_sort(items))


if __name__ == '__main__':
    main()
