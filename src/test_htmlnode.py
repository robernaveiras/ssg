import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_with_props(self):
        node = HTMLNode(
            tag="a", props={"href": "https://www.example.com", "target": "_blank"}
        )
        self.assertEqual(
            node.props_to_html(), ' href="https://www.example.com" target="_blank"'
        )

    def test_props_to_html_without_props(self):
        node = HTMLNode(tag="p")  # No props provided
        self.assertEqual(node.props_to_html(), "")

    def test_repr(self):
        node = HTMLNode(tag="div", value="Some value", children=[], props={})
        expected_repr = "HTMLNode(tag='div', value='Some value', children=0, props={})"
        self.assertEqual(repr(node), expected_repr)


if __name__ == "__main__":
    unittest.main()
