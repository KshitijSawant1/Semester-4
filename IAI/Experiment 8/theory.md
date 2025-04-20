Here’s a complete write-up for **Experiment 8 – Apply Wumpus World on a Given Problem**, including **Theory**, **Code & Output**, **Learning Outcomes**, and a sample **Conclusion**:

---

## 🧪 **Experiment 8 – Apply Wumpus World on Given Problem**

### 🎯 **Learning Objective**  
Students should be able to gain knowledge about **Wumpus World** and how to model and solve it using logical reasoning and agent-based systems.

---

## 🛠️ Tools Required:
- Python (Recommended for simulation)
- Jupyter Notebook / Any IDE
- Optional: Kivy or Tkinter for GUI

---

## 📘 **Theory:**

### 🔎 **What is Wumpus World?**

Wumpus World is a **grid-based environment** used in Artificial Intelligence to demonstrate how agents can make **informed decisions** based on **perception and inference**.

### 🧱 **Environment Layout:**
- A 4x4 grid.
- The agent starts at `(1,1)`.
- Hazards:
  - **Wumpus**: a monster that kills the agent.
  - **Pits**: the agent falls and dies.
  - **Gold**: the agent’s goal.
- **Perceptions**:
  - **Stench**: Wumpus is nearby.
  - **Breeze**: A pit is nearby.
  - **Glitter**: Gold is at the current cell.
  - **Bump**: Agent hits a wall.
  - **Scream**: Wumpus is killed.

### 🧠 **Agent Logic:**
- Uses **propositional logic** and **forward inference** to make decisions.
- Avoids Wumpus and pits.
- Grabs gold and exits.

---

## 🧪 **Code (Python Simulation)**

```python
# Simplified Wumpus World Simulation (No movement AI, just logical inference on 4x4)
grid = [
    ['Safe', 'Breeze', 'Pit', 'Breeze'],
    ['Breeze', 'Wumpus', 'Breeze', 'Safe'],
    ['Safe', 'Breeze', 'Safe', 'Glitter'],
    ['Safe', 'Safe', 'Safe', 'Safe']
]

percepts = {
    'Breeze': 'Pit nearby',
    'Stench': 'Wumpus nearby',
    'Glitter': 'Gold here!',
    'Safe': 'No danger'
}

# Agent starting at (0,0)
x, y = 0, 0

# Show percepts
print(f"Agent at ({x},{y}) - Perception: {percepts[grid[x][y]]}")
```

### ✅ Sample Output:
```
Agent at (0,0) - Perception: No danger
```

---

## 📊 **Learning Outcomes:**

- **LO8.1:** Describe the structure and rules of Wumpus World.
- **LO8.2:** Explain how an intelligent agent uses perceptions to infer safe moves.
- **LO8.3:** Implement a logical reasoning system in a grid environment.

---

## 📈 **Steps to Solve Wumpus World Problem:**

1. **Initialize** the environment: Define grid, agent start, and locations of Wumpus, pits, and gold.
2. **Perceive** the environment: Use percepts (Breeze, Stench, Glitter).
3. **Infer** danger: Using logic like “If there is a breeze, then at least one neighbor has a pit.”
4. **Mark Safe/Unsafe cells**: Based on current and past perceptions.
5. **Take Action**: Move, grab gold, or shoot arrow if danger inferred.

---

## ✅ **Conclusion:**

By applying the **Wumpus World model**, students understand how **AI agents** use **inference, perception, and logic** to navigate unknown environments safely. This experiment lays the foundation for concepts in **rule-based systems**, **knowledge representation**, and **decision-making in AI**.

---

## 📋 For Faculty Use:

| Correction Parameters            | Weight     |
|----------------------------------|------------|
| Formative Assessment             | 40%        |
| Timely Completion of Practical   | 40%        |
| Attendance / Learning Attitude   | 20%        |
| **Total Marks Obtained**         | XX/100     |

---

