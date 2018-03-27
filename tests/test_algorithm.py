from game.mcts.algorithm import MonteCarloTreeSearch
from game.mcts.node import Node
import unittest


class TestMonteCarloTreeSearch(unittest.TestCase):
    def setUp(self):
        self.mcts = MonteCarloTreeSearch(root_state=4)

    def test_selectNode_returnedNode(self):
        exp_node = Node(state=4)
        self.mcts.root.child_nodes = [Node(parent=self)]
        self.mcts.root.child_nodes[0].child_nodes = [exp_node]
        selected_node = self.mcts.select()
        self.assertIs(selected_node, exp_node)

    def test_expand_newNodeAssigned(self):
        self.mcts.expand(node=self.mcts.root, state=4)
        self.assertEquals(len(self.mcts.root.child_nodes), 1)
