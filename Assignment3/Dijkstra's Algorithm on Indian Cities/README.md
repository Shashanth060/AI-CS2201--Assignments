# Indian Cities Shortest Path Finder (Dijkstra Algorithm)

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Algorithm](https://img.shields.io/badge/Algorithm-Dijkstra-orange)
![Data](https://img.shields.io/badge/Dataset-Kaggle-green)

## Project Overview

This project implements **Dijkstra's Algorithm** in Python to find the **shortest path between two cities in India**.

The program reads a dataset of city connections and distances from a CSV file and constructs a **graph representation**. Using this graph, it calculates the **minimum distance and optimal path** between a source city and a destination city.

This project demonstrates:

* Graph representation using dictionaries
* File handling with CSV
* Priority Queue using `heapq`
* Implementation of Dijkstra's shortest path algorithm

---

Dataset Source

The dataset used in this project is taken from:

https://www.kaggle.com/datasets/kbdharun/a-star-algorithm-route-planning-dataset

File used: indian-cities-dataset.csv

---

## Requirements

* Python **3.8 or higher**

Install required libraries (only standard libraries are used):

```
csv
heapq
```

Since these are built into Python, **no external installation is required**.

---

## Project Structure

```
Dijkstra's Algorithm on Indian Cities/
│
├── dijkstra_pathfinder.py
├── indian-cities-dataset.csv
├── README.md
└── docs
    └── output.png
```

---

## Dataset Format

The dataset file `indian-cities-dataset.csv` must contain the following columns:

```
Origin,Destination,Distance
Delhi,Jaipur,281
Delhi,Agra,233
Agra,Jaipur,240
Mumbai,Pune,150
```

Where:

* **Origin** → Starting city
* **Destination** → Connected city
* **Distance** → Distance between cities (in km)

The program automatically builds a **bidirectional graph** from this dataset.

---

## How to Run the Program

1. Clone the repository

```
git clone https://github.com/your-username/UGV-Path-Planning-Simulator.git
```

2. Navigate to the project folder

```
cd UGV-Path-Planning-Simulator
```

3. Run the Python script

```
python dijkstra_pathfinder.py
```

4. Enter the source and destination cities when prompted.

Example:

```
Enter source city: Delhi
Enter destination city: Jaipur
```

Output:

```
Shortest Distance: 308 km
Shortest Path:
Delhi -> Jaipur
```

---

## Example Output

```
Enter source city: Delhi
Enter destination city: Varanasi

Shortest Distance: 865 km
Shortest Path:
Delhi -> Lucknow -> Varanasi
```
![Example](docs/output.png)

---

## Algorithm Used

### Dijkstra's Algorithm

Dijkstra’s algorithm finds the **shortest path between nodes in a weighted graph**.

Steps used in this implementation:

1. Initialize all city distances as infinity.
2. Set the source city distance to 0.
3. Use a **priority queue (min-heap)** to always expand the closest city.
4. Update distances to neighboring cities if a shorter path is found.
5. Store the previous city to reconstruct the path.

Time Complexity:

```
O((V + E) log V)
```

Where:

* **V** = number of cities
* **E** = number of roads

---

## Technologies Used

- Python

- CSV file handling

- Priority Queue (heapq)

- Graph Algorithms

---

## License

This project is open-source and free to use for educational purposes.
