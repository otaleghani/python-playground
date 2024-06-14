class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplemented("Not implemented error")

    def props_to_html(self):
        result = ' '.join([f"{key}='{value}'".format(key, value) for key, value in self.props.items()])
        return " " + result

    def __repr__(self):
        print(f"Tag: {self.tag}")
        print(f"Value: {self.value}")
        print(f"Children: {self.children}")
        print(f"Props: {self.props}")

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("Error")
        if self.tag is None:
            return self.value
        attributes = ""
        if self.props is not None:
            attributes = self.props_to_html()
        return f"<{self.tag}{attributes}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("No tag provided")
        if self.children is None or self.children is []:
            raise ValueError("No children")
        formatted_props = ""
        if self.props is not None:
            formatted_props = self.props_to_html() 
        start = f"<{self.tag}{formatted_props}>"
        end = f"</{self.tag}>"
        middle = ""
        for node in self.children:
            middle += node.to_html()
        return start + middle + end