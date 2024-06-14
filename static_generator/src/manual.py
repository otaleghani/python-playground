from textnode import TextNode
from htmlnode import LeafNode, ParentNode
from main import text_node_to_html_node

def main():
    # TEST LEAFs
    leaf = LeafNode("a","Scopri sandrone",{"href":"sandrone"})
    #print(leaf.to_html())
    # TEST PARENTs
    p_node = ParentNode("div", [LeafNode("h1", "I'm inside", {"class": "heading"})])
    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text", {"alt": "/src/anvedi"}),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
            p_node, 
        ],
    )
    #print(node.to_html())

    bold = TextNode("testo", "bold")
    bold.repr()
    
    bold_tag = text_node_to_html_node(bold)
    bold_tag.__repr__()


main()