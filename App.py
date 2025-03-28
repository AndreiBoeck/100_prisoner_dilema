import random
import networkx as nx
import matplotlib.pyplot as plt

prisoners = []
boxes = []

non_optimal_fail = 0
non_optimal_jumps = []
paths_non_optimal = []

optimal_fails = 0
optimal_jumps = []
paths_optimal = []

def init_boxes():
    """
    initiate the box array
    :return:
    """
    global boxes
    while len(boxes) < 100:
        num_aleatorio = random.randint(1, 100)
        if num_aleatorio not in boxes:
            boxes.append(num_aleatorio)
    print("Quantidade de caixas geradas:", len(boxes))

def non_optimal(num_prisoner: int):
    """
    choose random boxes
    :param num_prisoner: the prisoner number
    :return: True if it finds the correct number, False otherwise
    """
    global non_optimal_fail, non_optimal_jumps, prisoners, paths_non_optimal
    box_choice = []
    # prisoners have 50 chances, it doesn't repeat the box
    for i in range(1, 51):
        random_pick = random.choice(boxes)
        while random_pick in box_choice:
            random_pick = random.choice(boxes)
        box_choice.append(random_pick)
        if random_pick == prisoners[num_prisoner-1]:
            non_optimal_jumps.append(len(box_choice))
            paths_non_optimal.append(box_choice.copy())
            return True
    non_optimal_fail += 1
    paths_non_optimal.append(box_choice.copy())
    return False

def optimal(num_prisoner: int):
    """
    Follow the best strategy for the problem
    :param num_prisoner: the prisoner number
    :return: True if it finds the correct number, False otherwise
    """
    global optimal_fails, optimal_jumps, prisoners, boxes, paths_optimal
    box_choice = []
    num_choice = num_prisoner
    # Prisoners have 50 chances, but this time with the best strategy
    for i in range(1, 51):
        box = boxes[num_choice-1]
        box_choice.append(box)
        if box == prisoners[num_prisoner - 1]:
            optimal_jumps.append(len(box_choice))
            paths_optimal.append(box_choice.copy())
            return True
        else:
            num_choice = box
    optimal_fails += 1
    paths_optimal.append(box_choice.copy())
    return False

def init_prisoners():
    """
    initiate the prisoners array
    """
    global prisoners
    for i in range(1, 101):
        prisoners.append(i)


def plot_paths(paths, title="Caminhos dos Prisioneiros"):
    """
    Plot a graph (MultiDiGraph) where each aresta represents a transition between two boxes
    in the prisoner path.
    """
    G = nx.MultiDiGraph()

    nodes = set()
    for path in paths:
        for n in path:
            nodes.add(n)
    G.add_nodes_from(nodes)

    for idx, path in enumerate(paths):
        for i in range(len(path) - 1):
            G.add_edge(path[i], path[i + 1], prisoner=idx + 1)


    pos = nx.circular_layout(G)

    plt.figure(figsize=(10, 10))
    nx.draw_networkx_nodes(G, pos, node_color="skyblue", node_size=400)
    nx.draw_networkx_labels(G, pos)

    nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=10, connectionstyle='arc3, rad=0.1')

    plt.title(title)
    plt.show()

def main():
    init_boxes()
    init_prisoners()

    global boxes, non_optimal_fail, non_optimal_jumps, prisoners, paths_non_optimal, optimal_fails, optimal_jumps, paths_optimal

    print("Non Optimal:")
    for i in range(1, 101):
        non_optimal(i)
    print("Falhas (non optimal):", non_optimal_fail)
    print("Saltos (non optimal):", non_optimal_jumps)
    print("Caminhos (non optimal):")
    for path in paths_non_optimal:
        print(path)

    plot_paths(paths_non_optimal, title="Caminhos dos Prisioneiros(Non-Optimal)")

    print("\nOptimal:")
    for i in range(1, 101):
        optimal(i)
    print("Falhas (optimal):", optimal_fails)
    print("Saltos (optimal):", optimal_jumps)
    print("Caminhos (optimal):")
    for path in paths_optimal:
        print(path)

    plot_paths(paths_optimal, title="Caminhos dos Prisioneiros(Optimal)")

if __name__ == '__main__':
    main()
