from .node import Node


class MonteCarloTreeSearch:
    def __init__(self, root_state):
        self.root = Node(state=root_state)

    def select(self):
        node = self.root
        while node.has_childs():
            node = node.random_child()
        return node

    def expand(self, node, state):
        # is move required? check later
        new_node = Node(parent=node, state=state)
        node.child_nodes.append(new_node)
