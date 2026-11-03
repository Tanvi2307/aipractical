def vacuum_reflex_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Move right"
    elif location == "B":
        return "Move left"
    
environment = {
    "A":"Dirty",
    "B":"Dirty"
}
location = "A"
print("Initial Environment:", environment)
print()

while True:
    status = environment[location]
    action = vacuum_reflex_agent(location, status)
    print(f"Agent location: {location}")
    print(f"Room status: {status}")
    print(f"Action: {action}\n")
    
    if action == "Suck":
        environment[location] = "Clean"
    elif action == "Move right":
        location = "B"
    elif action == "Move left":
        location = "A"
        
    if environment["A"] == "Clean" and environment["B"] == "Clean":
        print("Final environment:", environment)
        print("Both rooms are clean")
        break;

