class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if not self.props:
            return ""
        attributes = []
        for key, value in self.props.items():
            attribute_string = f' {key}="{value}"'
            attributes.append(attribute_string)

        return "".join(attributes)

    def __repr__(self):
        return (
            f"HTMLNode(tag={self.tag!r}, value={self.value!r}, "
            f"children={len(self.children) if self.children else 0}, "
            f"props={self.props!r})"
        )
