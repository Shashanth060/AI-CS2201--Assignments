import csv
import heapq


graph = {}

with open("indian-cities-dataset.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        city1 = row["Origin"]
        city2 = row["Destination"]
        distance = int(row["Distance"])

        if city1 not in graph:
            graph[city1] = {}
        graph[city1][city2] = distance

        if city2 not in graph:
            graph[city2] = {}
        graph[city2][city1] = distance



def dijkstra(graph, start, end):

    pq = [(0, start)]
    distances = {city: float('inf') for city in graph}
    previous = {city: None for city in graph}

    distances[start] = 0

    while pq:
        current_distance, current_city = heapq.heappop(pq)

        if current_city == end:
            break

        for neighbor, weight in graph[current_city].items():

            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_city
                heapq.heappush(pq, (new_distance, neighbor))



    path = []
    city = end

    while city:
        path.append(city)
        city = previous[city]

    path.reverse()

    return distances[end], path



source = input("Enter source city: ")
destination = input("Enter destination city: ")

distance, path = dijkstra(graph, source, destination)



print("\nShortest Distance:", distance, "km")
print("Shortest Path:")

print(" -> ".join(path))