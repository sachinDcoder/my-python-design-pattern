class HtmlElement:
    indent_size = 2

    def __init__(self, name="", text=""):
        self.name = name
        self.text = text
        self.elements = []

    def __str(self, indent):
        lines = []
        i = ' ' * (indent * self.indent_size)
        lines.append(f'{i}<{self.name}>')

        if self.text:
            i1 = ' ' * ((indent + 1) * self.indent_size)
            lines.append(f'{i1}{self.text}')

        for e in self.elements:
            lines.append(e.__str(indent + 1))

        lines.append(f'{i}</{self.name}>')
        return '\n'.join(lines)

    @staticmethod
    def create(name):
        return HtmlBuilder(name)

    def __str__(self):
        return self.__str(0)


class HtmlBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.__root = HtmlElement(name=root_name)

    def add_child(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(name=child_name, text=child_text)
        )

    def add_child_fluent(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(name=child_name, text=child_text)
        )
        return self

    def clear(self):
        self.__root = HtmlElement(self.root_name)

    def __str__(self):
        return str(self.__root)


def without_builder():
    # Simple para html
    hello = 'hello'
    parts = ['<p>', hello, '</p>']
    print(''.join(parts))

    # Html list with 2 words
    words = ['hello', 'world']
    parts = ['<ul>']
    for w in words:
        parts.append(f'  <li>{w}</li>')
    parts.append('</ul>')
    print('\n'.join(parts))


def ordinary_builder():
    # html_builder = HtmlBuilder('ul')
    html_builder = HtmlElement.create('ul')
    html_builder.add_child('li', 'hello')
    html_builder.add_child('li', 'world')
    print(html_builder)


def fluent_builder():
    html_builder = HtmlElement.create('ul')
    html_builder\
        .add_child_fluent('li', 'hello')\
        .add_child_fluent('li', 'world')
    print(html_builder)


def main():
    print('without_builder(): ')
    without_builder()

    print('\nordinary builder(): ')
    ordinary_builder()

    print('\nfluent builder(): ')
    fluent_builder()


if __name__ == "__main__":
    main()