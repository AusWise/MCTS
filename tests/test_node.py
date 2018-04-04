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

    def test_hasChilds_shouldReturnFalse(self):
        self.assertFalse(self.node.has_childs())

    def test_hasChilds_shouldReturnTrue(self):
        self.node.child_nodes = ['n1', 'n2']
        self.assertTrue(self.node.has_childs())

    def test_pickRandomChild_returnedCorrectType(self):
        self.node.child_nodes = [1, 2, 3]
        node = self.node.random_child()
        self.assertIsInstance(node, int)

    def test_getWinsRatio_returnFloat(self):
        self.node.visits = 4
        self.node.wins = 2
        self.assertEquals(self.node.wins_ratio, 0.5)

    def test_getWinsRatioWhenNoVisits_returnsZero(self):
        self.node.visits = 0
        self.node.wins = 0
        self.assertEquals(self.node.wins_ratio, 0.0)
