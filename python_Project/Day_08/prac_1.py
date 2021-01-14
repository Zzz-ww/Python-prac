"""
练习1：定义一个类描述数字时钟。
"""

from time import sleep


class Clock(object):
    def __init__(self, h=0, m=0, s=0):

        # 如果希望属性是私有的，在给属性命名时可以用两个下划线作为开头
        self._h = h
        self._m = m
        self._s = s

    def run(self):
        self._s += 1
        if self._s == 60:
            self._s = 0
            self._m += 1
            if self._m == 60:
                self._m = 0
                self._h += 1
                if self._h == 24:
                    self._h = 0

    def show(self):

        # %d是整型输出格式。bai02的意思是如果输du出的整型数zhi不足两位，dao左侧用0补齐。
        return '%02d:%02d:%02d' % \
              (self._h, self._m, self._s)


def main():
    clock = Clock(22, 22, 22)
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


if __name__ == '__main__':
    main()