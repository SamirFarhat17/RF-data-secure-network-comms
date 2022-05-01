import top_block_no_gui_tx as tbtx
import os
from threading import Thread
import multiprocessing
import time


# Your foo function
def foo(n):
    tbtx.main()
    time.sleep(1)

if __name__ == '__main__':
    # Start foo as a process
    p = multiprocessing.Process(target=foo, name="Foo", args=(10,))
    p.start()

    # Wait 10 seconds for foo
    time.sleep(20)

    # Terminate foo
    p.terminate()

    # Cleanup
    p.join()
