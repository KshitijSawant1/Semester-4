Sure! Here's a full explanation of **Experiment 09 – FCFS & SSTF Disk Scheduling Algorithm**, broken down clearly and concisely for your understanding, practicals, and viva preparation:

---

## 🧠 **Learning Objective**
To understand the **logic**, **steps**, and **comparative efficiency** of two fundamental disk scheduling algorithms:
- **FCFS (First Come First Serve)**
- **SSTF (Shortest Seek Time First)**

---

## ⚙️ **Tools Required**
You can implement this in:
- Python
- C
- Java  
(*Python is preferred for quick implementation and better readability.*)

---

## 📚 **Theory Overview**

### 🔸 **1. FCFS Disk Scheduling Algorithm (First Come First Serve)**

#### ➤ **What It Does:**
- Processes disk I/O requests **in the order they arrive**.
- It’s simple, fair (no starvation), but not the most efficient in reducing head movement.

#### ➤ **How It Works (Algorithm):**
1. Take the list of requested track numbers.
2. For each track in the order:
   - Calculate absolute distance from current head position.
   - Add this distance to total seek time.
   - Move head to that track (update current head).
3. Continue until all requests are served.

#### ➤ **Pros:**
- Simple and easy to implement.
- No starvation (all requests will eventually be served).

#### ➤ **Cons:**
- Can result in **large total head movement** (inefficient).
- Doesn't consider proximity to current head.

---

### 🔸 **2. SSTF Disk Scheduling Algorithm (Shortest Seek Time First)**

#### ➤ **What It Does:**
- Always services the **closest request** to the current head position.
- Reduces **total seek time** (more efficient than FCFS).

#### ➤ **How It Works (Algorithm):**
1. Take the list of track requests and initial head position.
2. From all unprocessed requests, **find the one with the minimum distance** to the current head.
3. Add this distance to total seek time.
4. Update current head to this track.
5. Repeat until all requests are served.

#### ➤ **Pros:**
- Better performance than FCFS.
- Lower seek time on average.
- Works well when proximity-based servicing is preferred.

#### ➤ **Cons:**
- **Starvation possible** for requests that are far away from the current head.
- Less predictable due to changing head direction frequently.

---

## 🔄 **Result and Discussion**
After implementing both algorithms, you'll:
- Compare **total seek time**.
- Count the **number of head movements**.
- Observe **how request order** and **initial head position** affect efficiency.
- See how **SSTF generally outperforms FCFS** but may risk starvation.

---

## 🎯 **Learning Outcomes**
- **LO1**: Understand how disk scheduling impacts system speed and efficiency.
- **LO2**: Analyze how the order of requests affects FCFS and SSTF differently.

---

## 📘 **Course Outcome**
- Evaluate and compare **disk access times**, **head movement**, and **algorithm behavior**.
- Understand **trade-offs between simplicity (FCFS)** and **efficiency (SSTF)**.

---

## ✅ **Conclusion (Example Write-Up)**
In this experiment, we implemented FCFS and SSTF disk scheduling algorithms. FCFS served requests fairly but had higher seek times. SSTF significantly reduced total seek time but introduced the possibility of starvation. We learned how request order and disk head location affect performance and efficiency.

---

Would you like the **Python code with a menu** for both FCFS and SSTF as well?