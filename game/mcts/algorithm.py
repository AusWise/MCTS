from .node import Node
from copy import deepcopy
import time
from random import choice


class MonteCarloTreeSearch:
    def __init__(self, root_state, engine):
        self.root = Node(state=root_state)
        self.engine = engine
        self.time_limit = 3
        self.max_simulation_depth = 200
        self.C = 1

    def select_UCB_leaf(self, node):
        while node.has_childs():
            node = self.select_UCB(node)
        return node

    def select_UCB(self, node):
        return max(node.child_nodes, key=lambda n: n.UCB(C=self.C))

    def expand(self, node, state):
        board = self.engine.board
        moves = self.engine.moves
        for move in moves:
            _board = deepcopy(board)
            self.engine.board = board
            self.engine.performMove(move)
            _new_node = Node(parent=node, move=move, state=_board)
            node.child_nodes.append(_new_node)

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
        depth = 0
        while winner is None and depth < self.max_simulation_depth:
            move = choice(self.engine.moves)
            winner = self.engine.performMove(move)
            depth += 1
        self.engine.board = initial_state
        return 1 if winner is not None and winner.name == player.name else 0

    def run(self):
        start_t = time.time()
        i = 0
        print('Running MCTS algorithm')
        while time.time() - start_t < self.time_limit:
            node = self.select_UCB_leaf(self.root)
            self.expand(node=node, state=self.engine.board)
            result = self.simulate(node=node)
            self.backpropagate(node=node, result=result)
            i = i + 1
        print('MCTS: {} iterations'.format(i))
