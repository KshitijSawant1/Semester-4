import heapq

# Goal state definition
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Heuristic function - Manhattan Distance
def manhattan(state):
    dist = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                goal_x = (val - 1) // 3
                goal_y = (val - 1) % 3
                dist += abs(i - goal_x) + abs(j - goal_y)
    return dist

# Find the blank space (0)
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Generate next possible states
def get_neighbors(state):
    x, y = find_blank(state)
    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    neighbors = []

    for dx, dy in moves:
        nx, ny = x+dx, y+dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

# Convert state for hashing
def serialize(state):
    return tuple(tuple(row) for row in state)

# A* Search Implementation
def a_star(start):
    open_set = []
    heapq.heappush(open_set, (manhattan(start), 0, start, []))
    visited = set()

    while open_set:
        f, g, current, path = heapq.heappop(open_set)

        if current == goal_state:
            return path + [current]

        visited.add(serialize(current))

        for neighbor in get_neighbors(current):
            if serialize(neighbor) not in visited:
                heapq.heappush(open_set, (g + 1 + manhattan(neighbor), g + 1, neighbor, path + [current]))

    return None

# Initial State
initial_state = [
    [1, 4, 3],
    [2, 5, 6],
    [8, 7, 0]
]

# Solve
solution = a_star(initial_state)

# Output
print("Steps to solve the 8-Puzzle using A* with Manhattan Distance:\n")

for i, step in enumerate(solution):
    h_n = manhattan(step)
    g_n = i
    f_n = g_n + h_n

    print(f"Step {i}: g(n) = {g_n}, h(n) = {h_n}, f(n) = {f_n}")
    for row in step:
        print(row)
    print()
