from textnode import TextNode, TextType


def main():
    # Create a test TextNode here
    # For example, you could create a bold text node with a URL
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)


if __name__ == "__main__":
    main()
