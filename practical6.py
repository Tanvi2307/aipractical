
def dfs(capacity_a, capacity_b, target):

    stack = [(0, 0)]
    visited = set()
    parent = {}

    while stack:

        state = stack.pop()
        a, b = state

        if state in visited:
            continue

        visited.add(state)

        if a == target or b == target:

            path = []
            while state is not None:
                path.append(state)
                state = parent.get(state)

            return path[::-1]

        next_states = [
            (capacity_a, b),  # Fill Jug A
            (a, capacity_b),  # Fill Jug B
            (0, b),           # Empty Jug A
            (a, 0),           # Empty Jug B
            (a - min(a, capacity_b - b), 
             b + min(a, capacity_b - b)),  # Pour A into B
            (a + min(b, capacity_a - a), 
             b - min(b, capacity_a - a))   # Pour B into A
        ]

        for next_state in next_states:

            if next_state not in visited:
                if next_state not in parent:
                    parent[next_state] = state

                stack.append(next_state)

    return None


capacity_a = 4
capacity_b = 3
target = 2

solution = dfs(capacity_a, capacity_b, target)

if solution:
    print("Solution Found!")
    for step in solution:
        print(step)
else:
    print("No solution exists!")
