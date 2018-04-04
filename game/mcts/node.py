import math
from random import choice


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

    @property
    def wins_ratio(self):
        return self.wins / self.visits if self.visits > 0 else 0.0

    @property
    def value(self):
        return self.wins_ratio

    # Upper Confidence Bounds
    def UCB(self, C):
        if self.parent is None:
            raise ValueError('No UCB value for root node!')
        conf_interval = math.sqrt(math.log(self.parent.visits) / self.visits)

        return self.value + C * conf_interval

    def add_child(self, node):
        self.child_nodes.append(node)

    def update(self, result):
        assert result in [0, 1]
        self.visits += 1
        self.wins += result

    def has_childs(self):
        return bool(self.child_nodes)

    def random_child(self):
        return choice(self.child_nodes)
