from abc import ABC
from enum import Enum, auto


class OutputFormat(Enum):
    MARKDOWN = auto()
    HTML = auto()


class ListStrategy(ABC):
    def start(self, buffer):
        pass

    def end(self, buffer):
        pass

    def add_list_item(self, buffer, item):
        pass


class MarkdownStrategy(ListStrategy):
    def add_list_item(self, buffer, item):
        buffer.append(f' * {item}\n')


class HtmlStrategy(ListStrategy):
    def start(self, buffer):
        buffer.append(f'<ul>\n')

    def end(self, buffer):
        buffer.append(f'</ul>\n')

    def add_list_item(self, buffer, item):
        buffer.append(f'   <li>{item}</li>\n')


class TextProcessor:
    def __init__(self, list_strategy=HtmlStrategy()):
        self.buffer = []
        self.list_strategy = list_strategy

    def append_list(self, items):
        self.list_strategy.start(self.buffer)
        for item in items:
            self.list_strategy.add_list_item(self.buffer, item)
        self.list_strategy.end(self.buffer)

    def set_output_format(self, output_format):
        if output_format == OutputFormat.MARKDOWN:
            self.list_strategy = MarkdownStrategy()
        elif output_format == OutputFormat.HTML:
            self.list_strategy = HtmlStrategy()

    def clear(self):
        self.buffer.clear()

    def __str__(self):
        return ''.join(self.buffer)


def main():
    items = ['Virat', "Rohit", "Ravinder"]

    text_processor = TextProcessor()
    text_processor.set_output_format(OutputFormat.MARKDOWN)
    text_processor.append_list(items)

    print(text_processor)

    text_processor.set_output_format(OutputFormat.HTML)
    text_processor.clear()
    text_processor.append_list(items)
    print(text_processor)


if __name__ == "__main__":
    main()















