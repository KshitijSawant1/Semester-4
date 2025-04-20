Here’s a clear and simple explanation of **Experiment 08: SCAN and LOOK Disk Scheduling Algorithms**, broken into understandable sections for your practical:

---

### 🧠 **Learning Objective**
To understand how **SCAN** and **LOOK** algorithms work for disk scheduling, especially in managing disk head movement to service requests efficiently.

---

### ⚙️ **Tools**
- Programming Languages: Python / C / Java  
- Platform: Any terminal-based system or IDE for execution

---

### 📚 **Theory Overview**

#### 🔁 SCAN Disk Scheduling Algorithm (Elevator Algorithm)
- The disk arm/head **moves in one direction**, servicing all requests until it hits the end of the disk.
- Once it reaches the end, it **reverses** its direction and continues servicing remaining requests.
- It behaves like an **elevator**: goes to the top, comes back to the bottom servicing requests.

**Working Steps:**
1. Sort all disk requests.
2. Move the head in a chosen direction (left or right).
3. Service all requests in that direction.
4. When no more requests in that direction, reverse.
5. Continue until all requests are serviced.

**Advantages:**
- Simple and avoids starvation.
- More efficient than FCFS.
  
**Disadvantages:**
- Longer waiting for some requests (just missed ones).
- Unfair to requests just behind the head’s direction.

---

#### 👀 LOOK Disk Scheduling Algorithm (Optimized SCAN)
- Similar to SCAN, but instead of going till the **end of the disk**, it stops at the **last request** in that direction.
- Saves time by avoiding unnecessary travel.

**Working Steps:**
1. Sort all disk requests.
2. Move in the specified direction and look for pending requests.
3. Service all in that direction.
4. Stop when no more requests remain.
5. Reverse direction and repeat.

**Advantages:**
- Reduces seek time over SCAN.
- Avoids scanning unnecessary empty parts of the disk.

**Disadvantages:**
- Can starve requests in the opposite direction.
- Not ideal for real-time systems.

---

### 📌 **Comparison of SCAN vs LOOK**
| Feature               | SCAN                          | LOOK                          |
|-----------------------|-------------------------------|-------------------------------|
| Direction             | Goes till end of disk         | Goes till last request only   |
| Performance           | Slightly slower               | More optimized                |
| Efficiency            | May scan empty areas          | Skips unnecessary scans       |
| Starvation            | Rare                          | May occur                     |
| Real-time suitability | Better                        | Slightly less suitable        |

---

### 🧪 **Result and Discussion**
After implementation:
- You’ll observe how different request sequences affect the total **seek time**.
- You can compare **head movement patterns** for both SCAN and LOOK.

---

### 🎯 **Learning Outcomes**
- LO1: Analyze and differentiate between SCAN and LOOK based on logic.
- LO2: Understand how the order of requests impacts algorithm performance.

---

### 📘 **Course Outcomes**
After completing this experiment, you'll be able to:
- Evaluate disk scheduling performance.
- Apply SCAN and LOOK in simulations to reduce seek time and improve efficiency.

---

### ✅ **Conclusion (Example)**
This experiment helped understand how disk scheduling works and why algorithms like SCAN and LOOK are important for optimizing head movement. SCAN was easier to understand, while LOOK provided better performance. We now know when to choose which algorithm based on disk request patterns.

---