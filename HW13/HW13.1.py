# 1. Write the method that return the number of threads currently in execution.
# Also prepare the method that will be executed with threads and run during the first method counting.

from threading import Thread, activeCount
import time


def func():
    time.sleep(1)


def threads_number():
    print(f"Number of active threads: {activeCount()}")


threading1 = Thread(target=func)
threading2 = Thread(target=func)

threading1.start()
threading2.start()

threads_number()

threading1.join()
threading2.join()
