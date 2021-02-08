"""
双向冒泡：
冒泡排序，每次都是从左往右，交换相邻的元素，从而达到循环一边可以把最大的元素放在右边。
而双向冒泡排序，在完成一次从左往右的冒泡排序后，再从右往左进行冒泡，从而把小的元素放在左边。
下面这张图可以很好地表达：
"""


def bubble_sort(origin_items):
    """高质量冒泡排序(搅拌排序)/双向冒泡排序"""
    comp = lambda x, y: x > y
    items = origin_items[:]
    for i in range(len(items) - 1):
        swapped = False    # 这个标志位也是可以放到简单冒泡排序中的，当已经排序好后，减少循环次数
        for j in range(i, len(items) - 1 - i):  # 正向：把当前循环最大的放到最后
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if swapped:
            swapped = False
            for j in range(len(items) - 2 - i, i, -1):  # 反向：把当前循环最小的放到最前
                if comp(items[j - 1], items[j]):
                    items[j], items[j - 1] = items[j - 1], items[j]
                    swapped = True
        if not swapped:
            break
    return items


def main():
    s = [1, 10, 2, 8, 5]
    print(bubble_sort(s))


if __name__ == '__main__':
    main()