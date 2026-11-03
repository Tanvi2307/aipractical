
import heapq

# Goal state
goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


# Calculate Manhattan Distance
def heuristic(state):
    distance = 0

    for i in range(9):
        if state[i] == 0:
            continue

        current_row = i // 3
        current_col = i % 3

        goal_index = state[i] - 1 #gives the correct index of the tile in the goal state

        goal_row = goal_index // 3
        goal_col = goal_index % 3

        distance += abs(current_row - goal_row)
        distance += abs(current_col - goal_col)

    return distance


# Generate neighboring states - generate all possible next moves
def get_neighbors(state): #It accepts the current state and returns all valid states that can be reached by moving one tile.
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

            new_zero = new_row * 3 + new_col #this calculates the index of the new position of the empty space (0) after the move.

            new_state = list(state)

            # Swap empty space with adjacent tile
            new_state[zero], new_state[new_zero] = (
                new_state[new_zero], new_state[zero]
            )

            neighbors.append(tuple(new_state))

    return neighbors


# A* Search Algorithm
def astar(start):

    # Priority queue: (f, g, state)
    pq = []
    heapq.heappush(pq, (heuristic(start), 0, start))

    # Store the minimum cost to reach each state
    g_score = {start: 0}

    # Store parent states for path reconstruction
    parent = {start: None} # this dictionary remembers where each state came from

    while pq:

        f, g, current = heapq.heappop(pq)

        # Ignore outdated entries
        if g != g_score[current]:
            continue

        # Goal reached
        if current == goal:

            path = []
            temp = current #temp starts at the goal state.We continue until we reach the starting state, whose parent is None

            while temp is not None:
                path.append(temp)
                temp = parent[temp]

            return path[::-1]

        # Explore neighboring states
        for neighbor in get_neighbors(current):

            new_g = g + 1

            if neighbor not in g_score or new_g < g_score[neighbor]:

                g_score[neighbor] = new_g

                new_f = new_g + heuristic(neighbor)

                parent[neighbor] = current

                heapq.heappush(
                    pq, (new_f, new_g, neighbor)
                )

    return None


# Print the puzzle
def display(state):

    for i in range(0, 9, 3):
        print(state[i:i+3])

    print()


# Initial state
start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)


# Execute A* Search
solution = astar(start)

if solution:

    print("Solution found!")
    print("Total moves:", len(solution) - 1)

    for step, state in enumerate(solution):

        print("Step", step)
        display(state)

else:
    print("No solution exists!")
