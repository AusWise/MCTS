class Node:
    def __init__(self, parent=None, move=None, state=None):
        # None for root node
        self.parent = parent
        # move which lead to current state
        self.move = move

        self.state = state
        self.visits = 0
        self.wins = 0
        self.child_nodes = []

    def add_child(self, node):
        self.child_nodes.append(node)

    def update(self, result):
        assert result in [0, 1]
        self.visits += 1
        self.wins += result
