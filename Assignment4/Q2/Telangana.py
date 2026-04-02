regions = [
    "Adilabad", "Kumuram Bheem Asifabad", "Mancherial", "Nirmal",
    "Nizamabad", "Kamareddy", "Jagtial", "Peddapalli",
    "Rajanna Sircilla", "Karimnagar", "Jayashankar Bhupalpally",
    "Mulugu", "Bhadradri Kothagudem", "Khammam",
    "Mahabubabad", "Warangal Rural", "Hanumakonda",
    "Jangaon", "Siddipet", "Medak", "Sangareddy",
    "Medchal Malkajgiri", "Hyderabad", "Vikarabad",
    "Rangareddy", "Yadadri Bhuvanagiri", "Nalgonda",
    "Suryapet", "Mahabubnagar", "Narayanpet",
    "Wanaparthy", "Jogulamba Gadwal", "Nagarkurnool"
]

colors = ["Red", "Green", "Blue", "Brown"]

neighbors = {
    "Adilabad": ["Kumuram Bheem Asifabad", "Nirmal"],
    "Kumuram Bheem Asifabad": ["Adilabad", "Nirmal", "Mancherial"],
    "Mancherial": ["Kumuram Bheem Asifabad", "Nirmal", "Jagtial", "Peddapalli", "Jayashankar Bhupalpally"],
    "Nirmal": ["Adilabad", "Kumuram Bheem Asifabad", "Mancherial", "Nizamabad", "Jagtial"],
    "Jagtial": ["Mancherial", "Nirmal", "Peddapalli", "Karimnagar", "Rajanna Sircilla", "Nizamabad"],
    "Peddapalli": ["Mancherial", "Jagtial", "Karimnagar", "Jayashankar Bhupalpally"],
    "Karimnagar": ["Jagtial", "Peddapalli", "Rajanna Sircilla", "Siddipet", "Jayashankar Bhupalpally", "Hanumakonda"],
    "Rajanna Sircilla": ["Jagtial", "Karimnagar", "Siddipet", "Kamareddy", "Medak", "Nizamabad"],
    "Siddipet": ["Rajanna Sircilla", "Karimnagar", "Medak", "Jangaon", "Yadadri Bhuvanagiri", "Medchal Malkajgiri", "Kamareddy", "Hanumakonda"],
    "Medak": ["Siddipet", "Medchal Malkajgiri", "Sangareddy", "Kamareddy"],
    "Sangareddy": ["Medak", "Kamareddy", "Vikarabad", "Rangareddy", "Medchal Malkajgiri"],
    "Kamareddy": ["Nizamabad", "Rajanna Sircilla", "Medak", "Sangareddy", "Siddipet"],
    "Nizamabad": ["Nirmal", "Jagtial", "Kamareddy", "Rajanna Sircilla"],
    "Jangaon": ["Siddipet", "Hanumakonda", "Yadadri Bhuvanagiri", "Warangal Rural", "Mahabubabad", "Suryapet"],
    "Yadadri Bhuvanagiri": ["Siddipet", "Jangaon", "Rangareddy", "Medchal Malkajgiri", "Suryapet", "Nalgonda"], 
    "Suryapet": ["Yadadri Bhuvanagiri", "Jangaon", "Mahabubabad", "Khammam", "Nalgonda"],
    "Mahabubabad": ["Jangaon", "Warangal Rural", "Mulugu", "Bhadradri Kothagudem", "Khammam", "Suryapet"],
    "Khammam": ["Mahabubabad", "Bhadradri Kothagudem", "Suryapet"],
    "Bhadradri Kothagudem": ["Mulugu", "Mahabubabad", "Khammam"],
    "Warangal Rural": ["Jangaon", "Jayashankar Bhupalpally", "Hanumakonda", "Mulugu", "Mahabubabad"],
    "Hanumakonda": ["Warangal Rural", "Jayashankar Bhupalpally", "Siddipet", "Karimnagar", "Jangaon"],
    "Mulugu": ["Warangal Rural", "Jayashankar Bhupalpally", "Bhadradri Kothagudem", "Mahabubabad"],
    "Jayashankar Bhupalpally": ["Mancherial", "Peddapalli", "Karimnagar", "Hanumakonda", "Mulugu", "Warangal Rural"],
    "Mahabubnagar": ["Nagarkurnool", "Wanaparthy", "Narayanpet", "Vikarabad", "Rangareddy"],
    "Nagarkurnool": ["Rangareddy", "Mahabubnagar", "Wanaparthy", "Nalgonda"],
    "Wanaparthy": ["Nagarkurnool", "Mahabubnagar", "Jogulamba Gadwal", "Narayanpet"],
    "Jogulamba Gadwal": ["Narayanpet", "Wanaparthy"],
    "Narayanpet": ["Mahabubnagar", "Vikarabad", "Wanaparthy", "Jogulamba Gadwal"],
    "Vikarabad": ["Sangareddy", "Rangareddy", "Mahabubnagar", "Narayanpet"],
    "Rangareddy": ["Hyderabad", "Medchal Malkajgiri", "Vikarabad", "Mahabubnagar", "Nagarkurnool", "Yadadri Bhuvanagiri", "Nalgonda", "Sangareddy"],
    "Hyderabad": ["Rangareddy", "Medchal Malkajgiri"],
    "Medchal Malkajgiri": ["Hyderabad", "Rangareddy", "Sangareddy", "Medak", "Siddipet", "Yadadri Bhuvanagiri"],
    "Nalgonda": ["Yadadri Bhuvanagiri", "Suryapet", "Nagarkurnool", "Rangareddy"]
    
}


def is_safe(region, color, assignment):
    for neighbor in neighbors.get(region, []):
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

            
            del assignment[region]

    return None


solution = backtrack({})

if solution:
    import networkx as nx
    import matplotlib.pyplot as plt

    print("Solution:")
    for region in regions:
        print(f"{region} -> {solution[region]}")

    G = nx.Graph()

    
    for region in regions:
        G.add_node(region)

    
    for region, nbrs in neighbors.items():
        for nbr in nbrs:
            G.add_edge(region, nbr)

    
    color_map = []
    for node in G.nodes():
        color = solution[node]
        if color == "Red":
            color_map.append("red")
        elif color == "Green":
            color_map.append("green")
        elif color == "Blue":
            color_map.append("blue")
        else:
            color_map.append("brown")

    
    plt.figure(figsize=(12,10))
    pos = {
    
    "Adilabad": (4,11),
    "Kumuram Bheem Asifabad": (5,11),

    "Nirmal": (4,10),
    "Mancherial": (5,10),

    
    "Nizamabad": (3,9),
    "Kamareddy": (4,9.4),
    "Jagtial": (5,9),
    "Peddapalli": (6,9),

    "Rajanna Sircilla": (5,8),
    "Karimnagar": (6,8),

    
    "Siddipet": (5,7),
    "Medak": (4,7),
    "Sangareddy": (3,6),

    "Medchal Malkajgiri": (5,6),
    "Hyderabad": (5,4.6),
    "Rangareddy": (4,5),

    
    "Jayashankar Bhupalpally": (7,9),
    "Mulugu": (8,9),

    "Warangal Rural": (7,8),
    "Hanumakonda": (7,7.3),
    "Jangaon": (6,6.7),

    "Mahabubabad": (8,7),

    
    "Bhadradri Kothagudem": (9,6),
    "Khammam": (8,6),
    "Suryapet": (7,6),

    
    "Yadadri Bhuvanagiri": (6,6),
    "Nalgonda": (6,5),

    
    "Mahabubnagar": (4,4),
    "Narayanpet": (3,4),
    "Wanaparthy": (4,3),
    "Jogulamba Gadwal": (3,3),
    "Nagarkurnool": (5,4),

    
    "Vikarabad": (3,5)
    }   
    nx.draw(
        G, pos,
        with_labels=True,
        node_color=color_map,
        node_size=1000,
        font_size=7,
        edge_color="black",
        linewidths=1
    )

    plt.title("Telangana District Map Coloring")
    plt.axis('off')
    plt.show()
else:
    print("No solution found")
