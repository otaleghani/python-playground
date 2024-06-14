from textnode import TextNode
from htmlnode import HTMLNode, LeafNode

def text_node_to_html_node(text_node):
    type = text_node.text_type
    text = text_node.text
    url = text_node.url
    if type == "text":
        return LeafNode(None, text)
    if type == "bold":
        return LeafNode("b", text)
    if type == "italic":
        return LeafNode("i", text)
    if type == "code":
        return LeafNode("code", text)
    if type == "link":
        return LeafNode("a", text, {"href": url})
    if type == "image":
        return LeafNode("img", "", {"src": url, "alt": text})
    raise Exception("Type not valid")

def main():
    some = TextNode("This is a text node", "bold", "https://www.boot.dev")
    some.repr()
    alberto = HTMLNode("h1", "Sandrone Nazionale", [], {"sandro": "alberto", "modello": "giuditta"})
    print(alberto.props_to_html())
    alberto.__repr__()

main()
