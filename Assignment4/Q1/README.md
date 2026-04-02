# Australian Map Coloring

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Algorithm](https://img.shields.io/badge/Algorithm-Backtracking-orange)
![Problem](https://img.shields.io/badge/Problem-Map%20Coloring-green)

## Project Overview

This project implements the **Map Coloring Problem** using the **Backtracking Algorithm** in Python.

The objective is to assign colors to different regions of Australia such that **no two adjacent regions have the same color**.

The map is represented as a **graph**, where regions are nodes and shared borders are edges. The algorithm explores all possibilities using backtracking to find a valid solution.

This project demonstrates:

* Constraint Satisfaction Problems (CSP)
* Backtracking algorithm
* Graph representation using dictionaries
* Recursion in Python

---

## Requirements

* Python **3.8 or higher**

No external libraries are required.

---

## Project Structure
```
Q1/
│
├── Australia.py
├── README.md
```

---

## Problem Representation

### Regions
```
Western Australia
Northern Territory
Queensland
South Australia
New South Wales
Victoria
Tasmania
```

### Colors Used


Red
Green
Blue


### Neighbor Relationships

```
Western Australia → Northern Territory, South Australia
Northern Territory → Western Australia, South Australia, Queensland
Queensland → Northern Territory, South Australia, New South Wales
South Australia → Western Australia, Northern Territory, Queensland, New South Wales, Victoria
New South Wales → Queensland, South Australia, Victoria
Victoria → South Australia, New South Wales
Tasmania → (No neighbors)
```

---

## How to Run the Program

1. Clone the repository


git clone https://github.com/Shashanth060/AI-CS2201--Assignments


2. Navigate to the project folder


cd "AI-CS2201--Assignments\Assignment4\Q1"


3. Run the Python script


python Australia.py


---

## Example Output

```
Solution:
Western Australia -> Red
Northern Territory -> Green
Queensland -> Red
South Australia -> Blue
New South Wales -> Green
Victoria -> Red
Tasmania -> Red
```

---

## Algorithm Used

### Backtracking Algorithm

Backtracking is used to solve constraint satisfaction problems by trying possible solutions and undoing choices when constraints are violated.

Steps used in this implementation:

1. Start with an empty assignment.
2. Select an unassigned region.
3. Try assigning a valid color.
4. Check constraints with neighboring regions.
5. Recursively continue for remaining regions.
6. Backtrack if no valid color is possible.

Time Complexity:


O(m^n)


Where:

* **n** = number of regions
* **m** = number of colors

---

## Technologies Used

- Python
- Recursion
- Backtracking Algorithm
- Graph Representation

---

## License

This project is open-source and free to use for educational purposes.