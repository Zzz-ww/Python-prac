"""
@property装饰器:

之前我们讨论过Python中属性和方法访问权限的问题，虽然我们不建议将属性设置为私有的，
但是如果直接将属性暴露给外界也是有问题的，比如我们没有办法检查赋给属性的值是否有效。
我们之前的建议是将属性命名以单下划线开头，通过这种方式来暗示属性是受保护的，不建议外界直接访问，
那么如果想访问属性可以通过属性的getter（访问器）和setter（修改器）方法进行对应的操作。
如果要做到这点，就可以考虑使用@property包装器来包装getter和setter方法，使得对属性的访问既安全又方便，
代码如下所示:
"""


class Rect:
    def __init__(self, area):
        self.__area = area

    # 定义一个矩形类，并定义用 @property 修饰的方法操作类中的 area 私有属性，代码如下：
    # 使用 ＠property 修饰了 area() 方法，这样就使得该方法变成了 area 属性的 getter 方法。
    # 需要注意的是，如果类中只包含该方法，那么 area 属性将是一个只读属性。
    # 在使用 Rect 类时，无法对 area 属性重新赋值
    @property
    def area(self):
        return self.__area

    # 而要想实现修改 area 属性的值，还需要为 area 属性添加 setter 方法，就需要用到 setter 装饰器，它的语法格式如下：
    @area.setter
    def area(self, value):
        self.__area = value

    @area.deleter
    def area(self):
        self.__area = 0


rect = Rect(30)
# 直接通过方法名来访问 area 方法
print("矩形的面积是：", rect.area)

rect.area = 90
print("修改后的面积：", rect.area)

del rect.area
print("删除后的area值为：", rect.area)
