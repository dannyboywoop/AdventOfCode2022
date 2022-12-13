from math import inf
from queue import PriorityQueue


def _reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    total_path.reverse()
    return total_path


def manhattan_distance(pos1, pos2):
    if len(pos1) != len(pos2):
        raise Exception("Vertices must have the same dimensionality!")
    return sum(abs(pos1[i] - pos2[i]) for i in range(len(pos1)))


def find_best_path(vertices, start_pos, end_pos, heuristic=manhattan_distance):
    open_set = PriorityQueue()
    came_from = {}
    g_score = {start_pos: 0}
    f_score = {start_pos: manhattan_distance(start_pos, end_pos)}

    open_set.put((f_score[start_pos], start_pos))

    while not open_set.empty():
        current = open_set.get()[1]
        if current == end_pos:
            return _reconstruct_path(came_from, current)

        for neighbour in vertices[current].neighbours:
            tentative_g_score = g_score[current] + 1
            if tentative_g_score < g_score.get(neighbour, inf):
                came_from[neighbour] = current
                g_score[neighbour] = tentative_g_score
                f_score[neighbour] = tentative_g_score + heuristic(neighbour, end_pos)
                open_set.put((f_score[neighbour], neighbour))
    return None
