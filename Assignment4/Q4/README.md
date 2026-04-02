# Cryptarithmetic Solver (TWO + TWO = FOUR)

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Algorithm](https://img.shields.io/badge/Algorithm-Brute%20Force-orange)
![Problem](https://img.shields.io/badge/Problem-Cryptarithmetic-green)

## Project Overview

This project solves a **Cryptarithmetic Puzzle** using Python.

The puzzle:
TWO + TWO =FOUR


Each letter represents a unique digit (0–9). The goal is to find digit assignments such that the equation holds true.

The program uses **permutations (brute-force approach)** to test all possible digit combinations and identify valid solutions.

This project demonstrates:

* Cryptarithmetic problem solving
* Permutations using itertools
* Brute-force search technique
* Logical constraint checking

---

## Requirements

* Python **3.8 or higher**

### Required Libraries


itertools


(Note: This is a built-in Python module, no installation required)

---

## Project Structure

```
Q4/
│
├── cryptarithmetic_problem.py
├── README.md
```

---

## Problem Representation

### Equation


TWO + TWO = FOUR


### Constraints

- Each letter represents a **unique digit (0–9)**
- No two letters can have the same digit
- Leading digits **T** and **F cannot be 0**

---

## How to Run the Program

1. Clone the repository


git clone https://github.com/Shashanth060/AI-CS2201--Assignments


2. Navigate to the project folder


cd "AI-CS2201--Assignments\Assignment4\Q4"


3. Run the Python script


python cryptarithmetic_problem.py


---

## Example Output

```
Solution: {'T': 7, 'W': 3, 'O': 4, 'F': 1, 'U': 6, 'R': 8}
734 + 734 = 1468
Solution: {'T': 7, 'W': 6, 'O': 5, 'F': 1, 'U': 3, 'R': 0}
765 + 765 = 1530
Solution: {'T': 8, 'W': 3, 'O': 6, 'F': 1, 'U': 7, 'R': 2}
836 + 836 = 1672
Solution: {'T': 8, 'W': 4, 'O': 6, 'F': 1, 'U': 9, 'R': 2}
846 + 846 = 1692
Solution: {'T': 8, 'W': 6, 'O': 7, 'F': 1, 'U': 3, 'R': 4}
867 + 867 = 1734
Solution: {'T': 9, 'W': 2, 'O': 8, 'F': 1, 'U': 5, 'R': 6}
928 + 928 = 1856
Solution: {'T': 9, 'W': 3, 'O': 8, 'F': 1, 'U': 7, 'R': 6}
938 + 938 = 1876
```
---

## Algorithm Used

### Brute Force using Permutations

The program generates all possible digit assignments for the letters using permutations and checks which one satisfies the equation.

Steps used in this implementation:

1. List all unique letters in the equation.
2. Generate all permutations of digits (0–9).
3. Assign digits to letters.
4. Skip cases where leading digits are 0.
5. Form numerical values of words.
6. Check if the equation holds.
7. Store valid solutions.

---

## Time Complexity
O(10Pn)


Where:

* **n** = number of unique letters  
* **P** = permutations  

---

## Technologies Used

- Python
- itertools (permutations)
- Brute Force Algorithm

---

## License

This project is open-source and free to use for educational purposes.
