from .node import Node


class MonteCarloTreeSearch:
    def __init__(self, root_state):
        self.root = Node(state=root_state)

    def select(self):
        node = self.root
        while node.has_childs():
            node = node.random_child()
        return node
