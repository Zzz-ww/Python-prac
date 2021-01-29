"""
单线程模拟
"""


from random import randint
from time import time, sleep


def download_task(filename):
    print('开始下载%s...' % filename)
    time_download = randint(5, 10)
    sleep(time_download)
    print('%s下载完成, 耗费%d秒' % (filename, time_download))


def main():
    start = time()
    download_task('py')
    download_task('Java')
    end = time()
    print('共耗费%d秒' % (end - start))


if __name__ == '__main__':
    main()
