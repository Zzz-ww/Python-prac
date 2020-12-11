"""
猜数字
"""
import random

count = 0
random_num = random.randint(1, 100)

while True:
    count += 1
    number = int(input("请输入你的答案："))

    if number > random_num:
        print("大")
    elif number < random_num:
        print("小")
    else:
        print("对")
        break

    print('猜了%d次' % count)

    if count > 7:
        print("失败")