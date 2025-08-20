from collections import deque

def water_jug_bfs(jug1, jug2, target):
    # store visited states to avoid repetition
    visited = set()
    # queue for BFS: each item is (jug1_amount, jug2_amount, steps)
    queue = deque()
    queue.append((0, 0, []))  # start with both jugs empty

    while queue:
        x, y, path = queue.popleft()

        # if the target is reached
        if x == target or y == target:
            path.append((x, y))
            print("Steps to reach target:")
            for step in path:
                print(step)
            return  # return here to stop after printing
          
        if (x, y) in visited:
            continue
        visited.add((x, y))

        # generates all possible next states
        next_states = [
            (jug1, y),  # Fill Jug1
            (x, jug2),  # Fill Jug2
            (0, y),     # Empty Jug1
            (x, 0),     # Empty Jug2
            (0, x + y) if x + y <= jug2 else (x - (jug2 - y), jug2),  # Pour Jug1 → Jug2
            (x + y, 0) if x + y <= jug1 else (jug1, y - (jug1 - x))   # Pour Jug2 → Jug1
        ]

        for state in next_states:
            if state not in visited:
                queue.append((state[0], state[1], path + [(x, y)]))

    print("Target not reachable.")

# Example usage
jug1_capacity = 3
jug2_capacity = 5
target_amount = 4   

water_jug_bfs(jug1_capacity, jug2_capacity, target_amount)
