regions = [
    "Western Australia",
    "Northern Territory",
    "Queensland",
    "South Australia",
    "New South Wales",
    "Victoria",
    "Tasmania"
]

colors = ["Red", "Green", "Blue"]

neighbors = {
    "Western Australia": ["Northern Territory", "South Australia"],
    "Northern Territory": ["Western Australia", "South Australia", "Queensland"],
    "Queensland": ["Northern Territory", "South Australia", "New South Wales"],
    "South Australia": ["Western Australia", "Northern Territory", "Queensland", "New South Wales", "Victoria"],
    "New South Wales": ["Queensland", "South Australia", "Victoria"],
    "Victoria": ["South Australia", "New South Wales"],
    "Tasmania": []
}


def is_safe(region, color, assignment):
    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(assignment):
    
    if len(assignment) == len(regions):
        return assignment

    
    for region in regions:
        if region not in assignment:
            break

    
    for color in colors:
        if is_safe(region, color, assignment):
            assignment[region] = color

            result = backtrack(assignment)
            if result:
                return result

            # Backtrack
            del assignment[region]

    return None


solution = backtrack({})

if solution:
    print("Solution:")
    for region in regions:
        print(f"{region} -> {solution[region]}")
else:
    print("No solution found")