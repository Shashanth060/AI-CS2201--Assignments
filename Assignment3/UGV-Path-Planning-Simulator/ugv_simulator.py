import tkinter as tk
from tkinter import ttk
import random
import heapq
import time
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np
from matplotlib.patches import Patch

SIZE = 70

DENSITY_LEVELS = {
    "Low": 0.10,
    "Medium": 0.25,
    "High": 0.40
}


def generate_grid(size, density):

    grid = [[0 for _ in range(size)] for _ in range(size)]

    for i in range(size):
        for j in range(size):
            if random.random() < density:
                grid[i][j] = 1

    return grid



def heuristic(a, b):

    return abs(a[0] - b[0]) + abs(a[1] - b[1])



def astar(grid, start, goal):

    rows = len(grid)
    cols = len(grid[0])

    open_list = []
    heapq.heappush(open_list, (0, start))

    g = {start: 0}
    parent = {}

    nodes_expanded = 0

    while open_list:

        _, current = heapq.heappop(open_list)
        nodes_expanded += 1

        if current == goal:

            path = []

            while current in parent:
                path.append(current)
                current = parent[current]

            path.append(start)

            return path[::-1], nodes_expanded

        x, y = current

        neighbors = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]

        for nx, ny in neighbors:

            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:

                new_cost = g[current] + 1

                if (nx,ny) not in g or new_cost < g[(nx,ny)]:

                    g[(nx,ny)] = new_cost

                    h = heuristic((nx,ny), goal)

                    f = new_cost + h

                    heapq.heappush(open_list, (f,(nx,ny)))

                    parent[(nx,ny)] = current

    return None, nodes_expanded



def visualize(grid, path, start, goal, nodes=None, runtime=None, path_length=None, replans=None):

    size = len(grid)

    display = np.zeros((size, size))

    for i in range(size):
        for j in range(size):
            if grid[i][j] == 1:
                display[i][j] = 1

    if path:
        for x, y in path:
            display[x][y] = 2

    display[start[0]][start[1]] = 3
    display[goal[0]][goal[1]] = 4

    cmap = ListedColormap([
        "white",   # free
        "red",     # obstacle
        "blue",    # path
        "green",   # start
        "yellow"   # goal
    ])

    fig, ax = plt.subplots(figsize=(8,8))

    ax.imshow(display, cmap=cmap)

    ax.set_xticks(range(0, size, 10))
    ax.set_yticks(range(0, size, 10))

    ax.grid(color="gray", linestyle="-", linewidth=0.3)

    ax.set_title("UGV Path Planning Grid")


    info_text = ""

    if replans is not None:
        info_text += f"Replans: {replans}\n"

    if nodes is not None:
        info_text += f"Nodes Expanded: {nodes}\n"

    if runtime is not None:
        info_text += f"Time Taken: {runtime:.4f} sec\n"

    if path_length is not None:
        info_text += f"Path Length: {path_length}"
    else:
        info_text += "No Path Found"

    plt.figtext(
        0.72, 0.88,
        info_text,
        fontsize=10,
        bbox=dict(facecolor='white', alpha=0.9)
    )


    legend_elements = [
        Patch(facecolor='red', label='Obstacle'),
        Patch(facecolor='blue', label='Path'),
        Patch(facecolor='green', label='Start'),
        Patch(facecolor='yellow', label='Goal')
    ]

    ax.legend(
        handles=legend_elements,
        loc='center left',
        bbox_to_anchor=(1.02, 0.5)
    )

    plt.tight_layout()
    plt.show()



def run_dynamic_simulation(start, goal):

    grid = generate_grid(SIZE, 0.20)

    grid[start[0]][start[1]] = 0
    grid[goal[0]][goal[1]] = 0

    current = start
    final_path = [start]

    total_nodes = 0
    replans = 0
    start_time = time.time()

    while current != goal:

        path, nodes = astar(grid, current, goal)

        replans += 1
        total_nodes += nodes

        if not path or len(path) < 2:
            print("No path available")
            break

        next_step = path[1]

        current = next_step
        final_path.append(current)


        for _ in range(15):

            x = random.randint(0, SIZE-1)
            y = random.randint(0, SIZE-1)

            if (x,y) != current and (x,y) != goal:
                grid[x][y] = random.choice([0,1])

    end_time = time.time()

    runtime = end_time - start_time

    visualize(
        grid,
        final_path,
        start,
        goal,
        total_nodes,
        runtime,
        len(final_path),
        replans
    )



def run_algorithm():

    env_type = env_var.get()

    sx = int(start_x.get())
    sy = int(start_y.get())
    gx = int(goal_x.get())
    gy = int(goal_y.get())

    start = (sx, sy)
    goal = (gx, gy)

    if env_type == "Static":

        density = DENSITY_LEVELS[density_var.get()]

        grid = generate_grid(SIZE, density)

        grid[sx][sy] = 0
        grid[gx][gy] = 0

        start_time = time.time()

        path, nodes = astar(grid, start, goal)

        end_time = time.time()

        result_text.delete(1.0, tk.END)

        result_text.insert(tk.END, f"Nodes Expanded: {nodes}\n")
        result_text.insert(tk.END, f"Time Taken: {end_time-start_time:.4f} seconds\n")

        if path:
            result_text.insert(tk.END, f"Path Length: {len(path)}\n")
        else:
            result_text.insert(tk.END, "No Path Found\n")

        path_length = len(path) if path else None

        visualize(
            grid,
            path,
            start,
            goal,
            nodes,
            end_time-start_time,
            path_length
        )

    else:

        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Running Dynamic Simulation...\n")

        run_dynamic_simulation(start, goal)

def update_env_options(event=None):

    if env_var.get() == "Static":
        density_label.grid()
        density_menu.grid()

    else:
        density_label.grid_remove()
        density_menu.grid_remove()


root = tk.Tk()
root.title("UGV Path Planning Simulator")

tk.Label(root, text="Environment Type").grid(row=0, column=0)

env_var = tk.StringVar()

env_menu = ttk.Combobox(root, textvariable=env_var, state="readonly")
env_menu['values'] = ("Static", "Dynamic")
env_menu.current(0)
env_menu.grid(row=0, column=1)

env_menu.bind("<<ComboboxSelected>>", update_env_options)

density_var = tk.StringVar()

density_label = tk.Label(root, text="Obstacle Density")
density_label.grid(row=1, column=0)

density_menu = ttk.Combobox(root, textvariable=density_var, state="readonly")
density_menu['values'] = ("Low", "Medium", "High")
density_menu.current(1)
density_menu.grid(row=1, column=1)


tk.Label(root, text="Start X").grid(row=2, column=0)
start_x = tk.Entry(root)
start_x.insert(0,"0")
start_x.grid(row=2, column=1)

tk.Label(root, text="Start Y").grid(row=3, column=0)
start_y = tk.Entry(root)
start_y.insert(0,"0")
start_y.grid(row=3, column=1)


tk.Label(root, text="Goal X").grid(row=4, column=0)
goal_x = tk.Entry(root)
goal_x.insert(0,"69")
goal_x.grid(row=4, column=1)

tk.Label(root, text="Goal Y").grid(row=5, column=0)
goal_y = tk.Entry(root)
goal_y.insert(0,"69")
goal_y.grid(row=5, column=1)


run_button = tk.Button(root, text="Run A*", command=run_algorithm)
run_button.grid(row=6, column=0, columnspan=2, pady=10)


result_text = tk.Text(root, height=6, width=35)
result_text.grid(row=7, column=0, columnspan=2)

root.mainloop()