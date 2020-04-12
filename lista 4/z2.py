import random


def generate_tree(height):
    if height == 0:
        return None

    val = random.randint(1, 10)

    main_id = random.randint(0, 1)
    other_height = random.randint(0, height-1)

    if main_id == 0:
        return [str(val), generate_tree(height - 1), generate_tree(other_height)]
    else:
        return [str(val), generate_tree(height - 1), generate_tree(other_height)]


def dfs(tree):
    if tree is None:
        return
    yield tree[0]
    yield from dfs(tree[1])
    yield from dfs(tree[2])


def bfs(tree):
    if tree is None:
        return
    else:
        yield from bfs_internal([tree])


def bfs_internal(subtrees):
    to_check = []
    for subtree in subtrees:
        if subtree is None:
            continue
        yield subtree[0]
        to_check.append(subtree[1])
        to_check.append(subtree[2])
    if len(to_check) > 0:
        yield from bfs_internal(to_check)
