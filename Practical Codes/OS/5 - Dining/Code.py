import threading
import time

n = 5  # Number of philosophers
chopsticks = [threading.Semaphore(1) for _ in range(n)]

def philosopher(i):
    while True:
        print(f"Philosopher {i} is thinking")
        time.sleep(1)
        left = chopsticks[i]
        right = chopsticks[(i + 1) % n]

        left.acquire()
        right.acquire()

        print(f"Philosopher {i} is eating")
        time.sleep(2)

        left.release()
        right.release()

        print(f"Philosopher {i} finished eating")

threads = [threading.Thread(target=philosopher, args=(i,)) for i in range(n)]

for t in threads:
    t.start()
