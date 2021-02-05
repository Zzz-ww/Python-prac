"""
假设排序已经在前几轮已经成有序序列，可是我们的排序算法仍然“兢兢业业”地继续执行第七轮、第八轮。

这种情况下，如果我们能判断出数列已经有序，并且做出标记，剩下的几轮排序就可以不必执行，提早结束工作。
"""


def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # 这个标志位也是可以放到简单冒泡排序中的，当已经排序好后，减少循环次数
        swapped = False

        # Last i elements are already
        # in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to
            # n-i-1. Swap if the element
            # found is greater than the
            # next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # IF no two elements were swapped
        # by inner loop, then break
        if swapped == False:
            break


# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array :")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")
