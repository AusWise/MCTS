from .node import Node
from copy import deepcopy
import time
from random import choice
import random


class MonteCarloTreeSearch:
    def __init__(self, root_state, engine):
        self.root = Node(state=root_state)
        self.engine = engine
        self.time_limit = 3
        self.exploration_threeshold = 0.98

    def select(self):
        node = self.root
        while node.has_childs():
            if random.random() > self.exploration_threeshold:
                break
            node = node.random_child()
        return node

    def expand(self, node, state):
        # is move required? check later
        new_node = Node(parent=node, state=state)
        node.child_nodes.append(new_node)

    def backpropagate(self, node, result):
        _node = node
        while _node is not None:
            _node.update(result=result)
            _node = _node.parent

    def simulate(self, node):
        state_copy = deepcopy(self.engine.board)
        initial_state = self.engine.board
        self.engine.board = state_copy
        player = initial_state.active_player
        winner = None
        while winner is None:
            move = choice(self.engine.moves)
            winner = self.engine.performMove(move)
        self.engine.board = initial_state
        return 1 if winner.name == player.name else 0

    def run(self):
        start_t = time.time()
        i = 0
        while time.time() - start_t < self.time_limit:
            node = self.select()
            self.expand(node=node, state=self.engine.board)
            result = self.simulate(node=node)
            self.backpropagate(node=node, result=result)
        print('MCTS run {} times'.format(i))
