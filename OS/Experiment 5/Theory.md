### 🧪 **Experiment 05 – Dining Philosopher Problem**

---

### **Learning Objective:**

To understand and implement the **Dining Philosopher Problem** using synchronization techniques and observe how deadlock and starvation can be avoided.

---

### **Tools:**

- Python (with `threading` module)
- Java / C (alternate implementations, optional)

---

### **Theory:**

The **Dining Philosopher Problem** is a classic synchronization problem that illustrates the challenges of allocating shared resources among multiple processes.

- **Scenario:** Five philosophers sit around a table with a fork (chopstick) between each pair. A philosopher needs both forks to eat.
- **States:** Each philosopher can be in one of three states:
  - **Thinking**
  - **Hungry**
  - **Eating**

To eat, a philosopher must:

1. Acquire the left and right forks (semaphores).
2. Eat.
3. Release the forks and return to thinking.

This problem helps highlight issues like:

- **Deadlock:** When all philosophers pick up one fork and wait forever.
- **Starvation:** When a philosopher never gets both forks due to poor scheduling.

---

### **Semaphore-Based Solution (Python Implementation):**

```python
import threading
import time
import random

num_philosophers = 5
forks = [threading.Semaphore(1) for _ in range(num_philosophers)]
mutex = threading.Semaphore(1)

def philosopher(index):
    while True:
        print(f"Philosopher {index} is thinking...")
        time.sleep(random.randint(1, 5))

        mutex.acquire()
        left = index
        right = (index + 1) % num_philosophers

        forks[left].acquire()
        forks[right].acquire()
        mutex.release()

        print(f"Philosopher {index} is eating...")
        time.sleep(random.randint(1, 5))

        forks[left].release()
        forks[right].release()

philosopher_threads = []
for i in range(num_philosophers):
    t = threading.Thread(target=philosopher, args=(i,))
    philosopher_threads.append(t)
    t.start()

for t in philosopher_threads:
    t.join()
```

---

### **Output Snapshot (Sample):**

```
Philosopher 0 is thinking...
Philosopher 1 is thinking...
...
Philosopher 2 is eating...
...
Philosopher 2 is thinking...
...
```

---

### **Result and Discussion:**

✔ Each philosopher alternates between thinking and eating.  
✔ Forks are locked using semaphores, ensuring no two adjacent philosophers eat simultaneously.  
✔ Use of a mutex avoids race conditions during resource acquisition.

---

### **Learning Outcomes:**

- **LO4.1**: Identified critical section problems in concurrent execution.
- **LO4.2**: Demonstrated proper synchronization techniques to avoid deadlocks.

---

### **Course Outcome:**

- **CO3**: Understood the challenges of concurrency and synchronization, and implemented solutions that avoid deadlocks and starvation.

---

### ✅ **Conclusion:**

- Successfully implemented the Dining Philosopher Problem using semaphores in Python.
- Gained practical understanding of **critical sections**, **process synchronization**, and **deadlock avoidance**.
- Explored how semaphores can be used to coordinate shared resource access in concurrent systems.

---
