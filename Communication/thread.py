from time import sleep
from threading import Thread
import os

def some_task():
    os.startfile("top_block.py")

t = Thread(target=some_task)  # run the some_task function in another
                              # thread
t.daemon = True               # Python will exit when the main thread
                              # exits, even if this thread is still
                              # running
t.start()

snooziness = int(5)
sleep(snooziness)
print("\n\n\n\n\n\nhi\n\n\n\n\n\n\n\n")
os.startfile("thread_test.py")
