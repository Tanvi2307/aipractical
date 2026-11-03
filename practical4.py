import random

# Distance matrix between cities
distance = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

cities = len(distance)
k = 3   # Number of states kept in the beam


# Calculate total distance of a route
def calculate_cost(route):
    cost = 0

    for i in range(len(route) - 1):
        cost += distance[route[i]][route[i + 1]]

    # Return to starting city
    cost += distance[route[-1]][route[0]]

    return cost


# Generate neighbouring routes
def generate_neighbors(route):
    neighbors = []

    for i in range(1, len(route)):
        for j in range(i + 1, len(route)):
            new_route = route.copy()

            # Swap two cities
            new_route[i], new_route[j] = new_route[j], new_route[i]

            neighbors.append(new_route)

    return neighbors


# Local Beam Search
def local_beam_search():

    # Generate initial random states
    states = []

    for _ in range(k):
        route = list(range(cities))
        random.shuffle(route)
        states.append(route)

    best_route = None
    best_cost = float("inf")

    while True:
        all_neighbors = []

        # Generate successors of all current states
        for state in states:
            neighbors = generate_neighbors(state)
            all_neighbors.extend(neighbors)

        # Sort states according to their cost
        all_neighbors.sort(key=calculate_cost)

        # Keep only the best k states
        new_states = all_neighbors[:k]

        # Check for improvement
        current_cost = calculate_cost(new_states[0])

        if current_cost < best_cost:
            best_cost = current_cost
            best_route = new_states[0].copy()
            states = new_states
        else:
            break

    return best_route, best_cost


# Main program
best_route, best_cost = local_beam_search()

print("Best Route:")
print(" -> ".join(str(city + 1) for city in best_route)
      + " -> " + str(best_route[0] + 1))

print("Minimum Cost:", best_cost)