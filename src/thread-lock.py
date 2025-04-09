import threading
import time
from concurrent.futures import ThreadPoolExecutor

# Shared resource
counter = 0
# Create a lock object
lock = threading.Lock()
executor = ThreadPoolExecutor(max_workers=3)

def increment_counter(amount, thread_name):
    global counter
    
    print(f"{thread_name} is attempting to acquire the lock")
    
    # Acquire the lock before modifying the shared resource
    lock.acquire()
    try:
        print(f"{thread_name} has acquired the lock")
        local_counter = counter
        # Simulate some processing time
        time.sleep(0.1)
        # Update the shared resource
        counter = local_counter + amount
        print(f"{thread_name} updated counter to {counter}")
    finally:
        # Always release the lock, even if an exception occurs
        lock.release()
        print(f"{thread_name} has released the lock")

# Create multiple threads that will try to update the counter
threads = []
for i in range(5):
    thread = threading.Thread(target=increment_counter, args=(1, f"Thread-{i}"))
    threads.append(thread)
    thread.start()

    #executor
    executor.submit(increment_counter(1 , f"Thread-{i}" ))

# Wait for all threads to complete
for thread in threads:
    thread.join()

print(f"Final counter value: {counter}")