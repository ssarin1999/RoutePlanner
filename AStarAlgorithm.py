#Used http://theory.stanford.edu/~amitp/GameProgramming/ImplementationNotes.html to help understand implementation
import math
from queue import PriorityQueue


def shortest_path(graph, start, goal):
    
    queue = PriorityQueue()
    queue.put(start, 0)
    
    prev = {start: None}
    cost = {start: 0}

    while not queue.empty():
        currentNode = queue.get()

        if currentNode == goal:
            createPath(prev, start, goal)

        for node in graph.roads[currentNode]:
            updateCost = cost[currentNode] + heuristic(graph.intersections[currentNode], graph.intersections[node])
            
            if node not in cost or updateCost < cost[node]:
                cost[node] = updateCost
                totalCost = updateCost + heuristic(graph.intersections[currentNode], graph.intersections[node])
                queue.put(node, totalCost)
                prev[node] = currentNode

    return createPath(prev, start, goal)

def createPath(prev, start, goal):
    currentNode = goal
    path = [currentNode]
    
    while currentNode != start:
        currentNode = prev[currentNode]
        path.append(currentNode)
        
    path.reverse()
   
    return path

def heuristic(start, goal):
    return math.sqrt(((start[0] - goal[0]) ** 2) + ((start[1] - goal[1]) ** 2))

