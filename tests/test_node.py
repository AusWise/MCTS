from game.mcts.node import Node
import unittest


class TestNode(unittest.TestCase):
    def setUp(self):
        self.node = Node()

    def test_reportResults(self):
        self.node.update(0)
        self.node.update(1)
        self.assertEquals(self.node.visits, 2)
        self.assertEquals(self.node.wins, 1)
