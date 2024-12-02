from collections import deque

def water_jug_bfs(jug1_capacity, jug2_capacity, target):
    # BFS queue to store states (x, y)
    queue = deque([(0, 0)])  # Start with both jugs empty
    visited = set()         # To track visited states

    while queue:
        x, y = queue.popleft()
        
        # If we reached the target
        if x == target or y == target:
            return f"Solution found: Jug1 = {x}, Jug2 = {y}"

        # Mark the state as visited
        if (x, y) in visited:
            continue
        visited.add((x, y))

        # Generate all possible next states
        possible_states = [
            (jug1_capacity, y),       # Fill jug1
            (x, jug2_capacity),       # Fill jug2
            (0, y),                   # Empty jug1
            (x, 0),                   # Empty jug2
            (x - min(x, jug2_capacity - y), y + min(x, jug2_capacity - y)),  # Pour jug1 -> jug2
            (x + min(y, jug1_capacity - x), y - min(y, jug1_capacity - x)),  # Pour jug2 -> jug1
        ]

        # Add the new states to the queue if not visited
        for state in possible_states:
            if state not in visited:
                queue.append(state)

    return "No solution"

# Example Usage
jug1 = 4  # Capacity of Jug 1
jug2 = 3  # Capacity of Jug 2
target = 2  # Target amount of water
print(water_jug_bfs(jug1, jug2, target))
