import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("h1", "Sandrone Nazionale", [], {"sandro": "alberto", "modello": "giuditta"})
        node2 = HTMLNode("h1", "Sandrone Nazionale", [], {"sandro": "alberto", "modello": "giuditta"})
        leaf = LeafNode("a","Scopri sandrone",{"href":"sandrone"})
        #self.assertEqual(node, node2)
        node.props_to_html()
        leaf.to_html()


if __name__ == "__main__":
    unittest.main()

