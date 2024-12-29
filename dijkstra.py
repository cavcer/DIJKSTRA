import heapq

def dijkstra(graph,source):
    distances = { node: float("infinity") for node in graph}
    distances[source]= 0


    priority_queue = [(0,source)]
    

    while priority_queue:
        
        current_distance ,current_node = heapq.heappop(priority_queue)


        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor]= distance
                heapq.heappush(priority_queue, (distance, neighbor))


    return distances

graph = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'C': 3, 'D': 2},
    'C': {'A': 10, 'B': 3, 'D': 4},
    'D': {'B': 2, 'C': 4}
}

source_node = "A"

shortest_path = dijkstra(graph,source_node)

print(shortest_path)



