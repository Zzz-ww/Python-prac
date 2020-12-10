"""
输入半径求圆的周长与面积
"""

r = float(input("请输入圆的半径："))
pi = 3.14
perimeter = 2 * pi * r
area = pi * (r ** 2)
print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)
