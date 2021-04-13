# 2. Print current date by using 2 threads.
# 1) Define a subclass using Thread class.
# 2) Instantiate the subclass and trigger the thread
from threading import Thread
import time
from datetime import datetime


class Date(Thread):

    def run(self):
        print(f"Current date: {datetime.date(datetime.now())}")
        time.sleep(1)


def main():

    thread1 = Date()
    thread1.start()
    thread2 = Date()
    thread2.start()
    thread1.join()
    thread2.join()


if __name__ == '__main__':
    main()
