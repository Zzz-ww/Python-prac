"""
字典
"""

# 创建字典的字面量语法
scores = {'小明': 100, '小米': 99}
print(scores)

# 创建字典的构造器语法
items1 = dict(one=1, two=2, three=3)

# 通过zip函数将两个序列压成字典
items2 = dict(zip(['a', 'b', 'c'], '123'))

# 创建字典的推导式语法
items3 = {num: num ** 2 for num in range(1, 10)}

print(items1, items2, items3)

# 通过键可以获取字典中对应的值
print(scores['小明'])

# 对字典中所有键值对进行遍历
for key in scores:
    print(f'{key}: {scores[key]}')

# 更新字典中的元素
scores['小明'] = 80
scores.update(小米=60)
print(scores['小明'], scores['小米'])
print('---------------')

# 删除字典中的元素
print(scores.popitem())
print(scores.popitem())
print(scores.pop('小明', 100))

# 清空字典
scores.clear()
print(scores)
