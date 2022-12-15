from math import inf
from queue import PriorityQueue


def find_best_path(vertices, start_pos, goal_criteria):
    open_set = PriorityQueue()
    best_path_length_to_vertex = {start_pos: 0}

    open_set.put((best_path_length_to_vertex[start_pos], start_pos))

    while not open_set.empty():
        current = open_set.get()[1]
        if goal_criteria(current):
            return best_path_length_to_vertex[current]

        for neighbour in vertices[current].neighbours:
            path_length_to_neighbour_via_current = best_path_length_to_vertex[current] + 1
            if path_length_to_neighbour_via_current < best_path_length_to_vertex.get(
                neighbour, inf
            ):
                best_path_length_to_vertex[neighbour] = path_length_to_neighbour_via_current
                open_set.put((best_path_length_to_vertex[neighbour], neighbour))
    return None
