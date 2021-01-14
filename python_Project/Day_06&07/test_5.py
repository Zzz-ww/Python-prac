# 定义元组, 元组里面的元素是不可修改的
t = ('zjw', 24, True, 'Shenyang')
print(t)
print()

# 获取元组中的元素
print(t[0])
print()

# 遍历
for elem in t:
    print(elem)
    print()

# 重新给元组赋值
# t[0] = '王大锤'  # TypeError
# 变量t重新引用了新的元组原来的元组将被垃圾回收
t = ('lyl', 23, True, 'Dalian')
print(t)
print()

# 将元组转化成列表
person = list(t)
print(person)
print()

# 列表是可以修改元素的！！！
person[0] = 'xiaoxiaoliu'
print(person)
print()

# 将列表转成元组
fruits_list = ['apple', 'banana']
fruits_tuple = tuple(fruits_list)
print(fruits_list)
print(fruits_tuple)