Here’s the enhanced and finalized **write-up for Experiment 5** – _Informed Search on 8-Puzzle Problem_ using Java:

---

## ✅ **Experiment 5 – Apply Informed Search on Any Problem**

### 🎯 **Learning Objective**

Students should be able to gain knowledge about how informed search applies to a given problem statement.

---

### 🧰 **Tools Used**

- Programming Language: Java
- IDE: VS Code / Eclipse
- Concepts: A\* Search, Manhattan Heuristic

---

### 📘 **Theory: What is Informed Search?**

Informed search algorithms use **heuristic functions** to estimate the proximity of a state to the goal. These heuristics enable more **efficient** solutions compared to uninformed methods like BFS or DFS.

---

### 📌 **Heuristic Function (h(n)):**

A commonly used heuristic for the 8-puzzle is the **Manhattan Distance**, which calculates the total horizontal and vertical distance each tile is from its goal position.

---

### 🧩 **Problem Statement – 8 Puzzle**

#### a) Initial State:

```
1 4 3
2 5 6
8 7 _
```

#### b) Goal State:

```
1 2 3
4 5 6
7 8 _
```

---

### ⚙️ **Steps of A\* Algorithm**

1. Initialize the **open list** with the start node.
2. Loop until the goal is found:
   - Select the node with the **lowest f(n)**.
   - Generate **next moves** from the blank position.
   - Calculate:
     - `g(n)` → cost from start
     - `h(n)` → estimated cost to goal
     - `f(n) = g(n) + h(n)`
   - Add new states to the **open list** if not visited.
3. If the **goal state** is reached → return path.
4. If **open list is empty** → no solution exists.

---

### 💻 **Code**

✅ Your complete Java code with A\* implementation was already shared above.

---

### 📥 **Output (Sample of Final Steps)**

```
Step 22: g(n) = 22, h(n) = 0, f(n) = 22
[1, 2, 3]
[4, 5, 6]
[7, 8, 0]
```

---

### 📈 **Learning Outcomes**

- **LO5.1**: Described informed search with real examples like the 8-puzzle problem.
- **LO5.2**: Demonstrated A\* search (informed search) with Manhattan Distance as a heuristic.
- **LO5.3**: Understood how A\* ensures an **optimal solution** when heuristic is admissible.

---

### 📘 **Course Outcomes**

Upon completion of the experiment, students are able to:

- Understand heuristic-based problem-solving.
- Differentiate informed and uninformed approaches.
- Implement optimal path search using Java.

---

### ✅ **Conclusion**

The A\* search algorithm efficiently solved the 8-puzzle by using the Manhattan Distance heuristic to evaluate the best path toward the goal. This demonstrates how informed search provides optimal results while minimizing unnecessary exploration.
