class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, entry):
        self.entries.append(entry)

    def remove(self, entry):
        self.entries.remove(entry)

    def __str__(self):
        return "\n".join(self.entries)


class PersistenceManager:
    @staticmethod
    def save_to_file(filename, journal):
        file = open(filename, "w")
        file.write(str(journal))
        file.close()


class Reader:
    @staticmethod
    def read_from_file(filename):
        with open(filename) as file:
            print(file.read())


def main():
    journal = Journal()
    journal.add_entry("Hello")
    journal.add_entry("There")
    print(journal)
    journal.remove("Hello")
    print(journal)

    file = "file.txt"
    PersistenceManager.save_to_file(file, journal)
    Reader.read_from_file(file)


if __name__ == "__main__":
    main()