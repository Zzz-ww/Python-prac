import threading

# 创建一个rlock对象
lock = threading.RLock()

# 初始化共享资源
abce = 0

# 本线程访问共享资源
lock.acquire()
abce = abce + 1

# 这个线程尝试访问共享资源
lock.acquire()
abce = abce + 2
lock.release()

print(abce)