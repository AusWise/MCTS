import unittest
from game.mcts.algorithm import MonteCarloTreeSearch
from game.mcts.node import Node
from unittest.mock import Mock


class TestMonteCarloTreeSearch(unittest.TestCase):
    def setUp(self):
        self.mcts = MonteCarloTreeSearch(root_state=4, engine=Mock())

    def test_selectNode_returnedNode(self):
        exp_node = Node(state=4)
        self.mcts.root.child_nodes = [Node(parent=self)]
        self.mcts.root.child_nodes[0].child_nodes = [exp_node]
        selected_node = self.mcts.select_UCB_leaf(self.mcts.root)
        self.assertIs(selected_node, exp_node)

    def test_expand_newNodesCreated(self):
        self.mcts.engine.moves = [Mock() for _ in range(5)]
        self.mcts.expand(node=self.mcts.root, state=4)
        self.assertEquals(len(self.mcts.root.child_nodes), 5)

    def test_backpropagate(self):
        self.mcts.root.visits = 3
        child = Node(parent=self.mcts.root)
        self.mcts.root.child_nodes = [child]
        self.mcts.backpropagate(child, 1)
        self.assertEqual(self.mcts.root.visits, 4)
        self.assertEqual(self.mcts.root.wins, 1)

    def test_selectUCB_returnNodeWithHigestUCBvalue(self):
        def mock_node(ucb):
            n = Mock(sec_spec=Node)
            n.UCB.return_value = ucb
            return n

        ucb_vals = [0.2, 0.79, 0.66]
        self.mcts.root.child_nodes = [mock_node(ucb) for ucb in ucb_vals]
        exp_ret = self.mcts.root.child_nodes[1]
        ret = self.mcts.select_UCB(self.mcts.root)
        self.assertIs(ret, exp_ret)
