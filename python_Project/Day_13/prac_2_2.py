"""
在 prac_2_1 代码中，
我故意先去创建了一个列表容器然后填入了100000000个数，
这一步其实是比较耗时间的，
所以为了公平起见，
当我们将这个任务分解到8个进程中去执行的时候，
我们暂时也不考虑列表切片操作花费的时间，
只是把做运算和合并运算结果的时间统计出来，代码如下所示。
"""


from multiprocessing import Process, Queue
from random import randint
from time import time


