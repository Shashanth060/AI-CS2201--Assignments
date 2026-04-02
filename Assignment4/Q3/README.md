# Sudoku Solver

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Algorithm](https://img.shields.io/badge/Algorithm-Backtracking-orange)
![Problem](https://img.shields.io/badge/Problem-Sudoku-green)

## Project Overview

This project implements a **Sudoku Solver** using the **Backtracking Algorithm** in Python.

The program takes an incomplete Sudoku grid and fills in the missing values such that:

- Each row contains numbers from 1 to 9 without repetition
- Each column contains numbers from 1 to 9 without repetition
- Each 3×3 subgrid contains numbers from 1 to 9 without repetition

The algorithm recursively tries possible values and backtracks when constraints are violated.

This project demonstrates:

* Constraint Satisfaction Problem (CSP)
* Backtracking algorithm
* Recursive problem solving
* Grid-based logic implementation

---

## Requirements

* Python **3.8 or higher**

No external libraries are required.

---

## Project Structure
```
Q3/
│
├── Sudoku.py
├── README.md
```

---

## Input Format

The Sudoku grid is represented as a **2D list (9x9)**.

- Empty cells are represented using `0`
- Filled cells contain numbers from `1` to `9`
```
Example:
    [0,0,3,0,2,0,6,0,0],
    [9,0,0,3,0,5,0,0,1],
    [0,0,1,8,0,6,4,0,0],
    [0,0,8,1,0,2,9,0,0],
    [7,0,0,0,0,0,0,0,8],
    [0,0,6,7,0,8,2,0,0],
    [0,0,2,6,0,9,5,0,0],
    [8,0,0,2,0,3,0,0,9],
    [0,0,5,0,1,0,3,0,0]
```

---

## How to Run the Program

1. Clone the repository


git clone https://github.com/Shashanth060/AI-CS2201--Assignments


2. Navigate to the project folder


cd "AI-CS2201--Assignments\Assignment4\Q3"


3. Run the Python script


python Sudoku.py

---

## Example Output
```
Sudoku Puzzle:

0 0 3 | 0 2 0 | 6 0 0 
9 0 0 | 3 0 5 | 0 0 1 
0 0 1 | 8 0 6 | 4 0 0 
---------------------
0 0 8 | 1 0 2 | 9 0 0 
7 0 0 | 0 0 0 | 0 0 8 
0 0 6 | 7 0 8 | 2 0 0 
---------------------
0 0 2 | 6 0 9 | 5 0 0 
8 0 0 | 2 0 3 | 0 0 9 
0 0 5 | 0 1 0 | 3 0 0

Solved Sudoku:

4 8 3 | 9 2 1 | 6 5 7
9 6 7 | 3 4 5 | 8 2 1
2 5 1 | 8 7 6 | 4 9 3
---------------------
5 4 8 | 1 3 2 | 9 7 6 
7 2 9 | 5 6 4 | 1 3 8
1 3 6 | 7 9 8 | 2 4 5
---------------------
3 7 2 | 6 8 9 | 5 1 4
8 1 4 | 2 5 3 | 7 6 9
6 9 5 | 4 1 7 | 3 8 2
```

---

## Algorithm Used

### Backtracking Algorithm

Backtracking is used to solve Sudoku by trying possible numbers and undoing assignments when constraints are violated.

Steps used in this implementation:

1. Find an empty cell in the grid.
2. Try placing numbers from 1 to 9.
3. Check if the number is valid in:
   - Current row
   - Current column
   - 3×3 subgrid
4. Recursively solve the rest of the grid.
5. Backtrack if no valid number is found.

---

## Time Complexity
O(9^(n*n))

Where:

* **n = 9** (grid size)

---

## Technologies Used

- Python
- Backtracking Algorithm
- Recursion
- Grid-based Problem Solving

---

## License

This project is open-source and free to use for educational purposes.
