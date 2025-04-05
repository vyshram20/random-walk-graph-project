import random

def batched_random_walk(graph, start_node, walk_length, batch_size):
    walks = []
    for _ in range(batch_size):
        walk = [start_node]
        current = start_node
        for _ in range(walk_length - 1):
            neighbors = graph.get(current, [])
            if not neighbors:
                break
            current = random.choice(neighbors)
            walk.append(current)
        walks.append(walk)
    return walks
