class Buffer:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.buffer = [' '] * (width * height)

    def __getitem__(self, item):
        return self.buffer.__getitem__(item)

    def write(self, text):
        self.buffer += text


class ViewPort:
    def __init__(self, buffer=Buffer()):
        self.buffer = buffer
        self.offset = 0

    def get_char_at(self, index):
        return self.buffer[self.offset + index]

    def append(self, text):
        self.buffer.write(text)

    def set_offset(self, offset):
        if 0 <= offset < len(self.buffer.buffer):
            self.offset = offset


class Console:
    def __init__(self):
        buffer = Buffer()
        self.current_viewport = ViewPort(buffer)
        self.buffers = [buffer]
        self.viewports = [self.current_viewport]

    def write(self, text):
        self.current_viewport.buffer.write(text)

    def get_char_at(self, index):
        return self.current_viewport.get_char_at(index)

    def set_viewport_offset(self, offset):
        self.current_viewport.set_offset(offset)


def main():
    console = Console()
    console.write("Hello")
    console.set_viewport_offset(100)
    print(console.get_char_at(0))


if __name__ == "__main__":
    main()


