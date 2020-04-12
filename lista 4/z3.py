import random


class Node(object):
    def __init__(self, value, nodes):
        self.value = value
        self.nodes = nodes


def generate_tree(height):
    val = str(random.randint(1, 10))

    if height == 1:
        return Node(val, [])

    nodes_count = random.randint(1, 5)
    main_id = random.randint(0, nodes_count - 1)

    nodes = [generate_tree(height - 1) if i == main_id else generate_tree(random.randint(1, height - 1)) for i in
             range(nodes_count)]

    return Node(val, nodes)


def dfs(t):
    yield t.value
    for node in t.nodes:
        yield from dfs(node)


def bfs(tree):
    if tree is None:
        return
    else:
        yield from bfs_internal([tree])


def bfs_internal(nodes):
    to_check = []
    for node in nodes:
        if node is None:
            continue
        yield node.value
        for el in node.nodes:
            to_check.append(el)
    if len(to_check) > 0:
        yield from bfs_internal(to_check)
