import threading
import time
import random

# Number of philosophers
N = 5

# Forks: one between each philosopher (represented as semaphores)
forks = [threading.Semaphore(1) for _ in range(N)]

# Mutex to prevent race condition when checking fork availability
mutex = threading.Semaphore(1)

# States
THINKING = 0
HUNGRY = 1
EATING = 2

# Track state of each philosopher
state = [THINKING] * N

# Condition variables for each philosopher
conditions = [threading.Condition() for _ in range(N)]

def left(i):
    return (i + N - 1) % N

def right(i):
    return (i + 1) % N

def test(i):
    # Check if philosopher i can eat
    if state[i] == HUNGRY and state[left(i)] != EATING and state[right(i)] != EATING:
        state[i] = EATING
        conditions[i].acquire()
        conditions[i].notify()
        conditions[i].release()

def pickup(i):
    mutex.acquire()
    state[i] = HUNGRY
    print(f"Philosopher {i} is HUNGRY.")
    test(i)
    if state[i] != EATING:
        conditions[i].acquire()
        mutex.release()
        conditions[i].wait()
        conditions[i].release()
    else:
        mutex.release()

def putdown(i):
    mutex.acquire()
    state[i] = THINKING
    print(f"Philosopher {i} puts down forks and starts THINKING.")
    test(left(i))
    test(right(i))
    mutex.release()

def philosopher(i):
    while True:
        print(f"Philosopher {i} is THINKING.")
        time.sleep(random.uniform(1, 3))
        pickup(i)
        print(f"Philosopher {i} is EATING.")
        time.sleep(random.uniform(1, 2))
        putdown(i)

# Start all philosopher threads
for i in range(N):
    threading.Thread(target=philosopher, args=(i,)).start()

