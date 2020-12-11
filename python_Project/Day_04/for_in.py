"""
for in 循环:

1. range(101)：可以用来产生0到100范围的整数，需要注意的是取不到101。
2. range(1, 101)：可以用来产生1到100范围的整数，相当于前面是闭区间后面是开区间。
3. range(1, 101, 2)：可以用来产生1到100的奇数，其中2是步长，即每次数值递增的值。
4. range(100, 0, -2)：可以用来产生100到1的偶数，其中-2是步长，即每次数字递减的值。
"""

total_sum = 0
for x in range(101):
    total_sum += x

even_sum = 0
for x in range(2, 101, 2):
    even_sum += x

odd_sum = 0
for x in range(1, 101, 2):
    odd_sum += x

print("总和： " + str(total_sum))
print("偶数总和：" + str(even_sum))
print("奇数总和：" + str(odd_sum))

print('\n')

print('总和： %d' % total_sum)
print('偶数总和：%d' % even_sum)
print('奇数总和：%d' % odd_sum)
