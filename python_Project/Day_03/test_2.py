"""
百分制转成等级制
"""

score = int(input("请输入成绩："))
if score > 85:
    print("HD")
else:
    if score > 75:
        print("D")
    else:
        if score > 65:
            print("C")
        else:
            if score > 50:
                print("P")
            else:
                print("F")