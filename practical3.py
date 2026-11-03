from collections import deque

def tower_of_hanoi(n):
    # Initial state: all disks are on peg A
    start = (tuple(range(n, 0, -1)), (), ())
    
    # Goal state: all disks are on peg C
    goal = ((), (), tuple(range(n, 0, -1)))

    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, path = queue.popleft()

        # Check goal state
        if state == goal:
            return path

        # Generate possible moves
        for i in range(3):
            if not state[i]:
                continue

            # Top disk of peg i
            disk = state[i][-1]

            for j in range(3):
                if i == j:
                    continue

                # Move is valid if destination is empty
                # or top disk is larger than current disk
                if not state[j] or state[j][-1] > disk:

                    new_state = [list(peg) for peg in state]
                    new_state[i].pop()
                    new_state[j].append(disk)

                    new_state = tuple(tuple(peg) for peg in new_state)

                    if new_state not in visited:
                        visited.add(new_state)

                        move = f"Move disk {disk} from {chr(65+i)} to {chr(65+j)}"

                        queue.append(
                            (new_state, path + [move])
                        )

    return None


# Main program
n = int(input("Enter number of disks: "))

solution = tower_of_hanoi(n)

print("\nSolution using State Space Search:")
for step, move in enumerate(solution, 1):
    print(f"{step}. {move}")