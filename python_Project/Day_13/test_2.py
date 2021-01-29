"""
多进程模拟
"""

from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep


def download_task(filename):
    print('启动下载进程，进程号为[%d]' % getpid())
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成！共耗费%d秒' % (filename, time_to_download))


def main():
    start = time()
    p1 = Process(target=download_task, args=('py',))
    p1.start()
    p2 = Process(target=download_task, args=('Java',))
    p2.start()

    # join方法表示等待进程执行结束
    p1.join()
    p2.join()
    end = time()
    print('一共耗费了%.2f秒' % (end - start))


if __name__ == '__main__':
    main()
