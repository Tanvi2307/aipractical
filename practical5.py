
from collections import deque

# Goal state
goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


# Generate neighboring states
def get_neighbors(state):

    neighbors = []

    zero = state.index(0)

    row = zero // 3
    col = zero % 3

    moves = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    for dr, dc in moves:

        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_zero = new_row * 3 + new_col

            new_state = list(state)

            # Swap empty space with adjacent tile
            new_state[zero], new_state[new_zero] = (
                new_state[new_zero], new_state[zero]
            )

            neighbors.append(tuple(new_state))

    return neighbors


# BFS Algorithm
def bfs(start):

    queue = deque([(start, [])])

    visited = {start}

    while queue:

        state, path = queue.popleft()

        # Check goal state
        if state == goal:
            return path

        # Explore neighboring states
        for neighbor in get_neighbors(state):

            if neighbor not in visited:

                visited.add(neighbor)

                move = "Next State"

                queue.append(
                    (neighbor, path + [neighbor])
                )

    return None


# Display puzzle
def display(state):

    for i in range(0, 9, 3):
        print(state[i:i+3])

    print()


# Main program
start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

solution = bfs(start)

if solution is not None:

    print("Solution found!")
    print("Total moves:", len(solution))

    print("Initial State:")
    display(start)

    for step, state in enumerate(solution, 1):

        print("Step", step)
        display(state)

else:
    print("No solution exists!")
