from abc import ABC, abstractmethod


class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass


class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass


class FaxMachine(ABC):
    @abstractmethod
    def fax(self, document):
        pass


class MultiFunctionPrinter(Printer, Scanner, FaxMachine):

    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def fax(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


class OldFashionPrintter(Printer):
    def print(self, document):
        print(f"OldFashionPrintter is printing the document: {document}...")


class Photocopier(Printer, Scanner):
    def print(self, document):
        print(f"Photocopier is printing the document: {document}...")

    def scan(self, document):
        print(f"Photocopier is scanning the document: {document}...")


class MySuperPrinter(MultiFunctionPrinter):

    def print(self, document):
        print(f"MySuperPrinter is printing the document: {document}...")

    def fax(self, document):
        print(f"MySuperPrinter is faxing the document: {document}...")

    def scan(self, document):
        print(f"MySuperPrinter is scanning the document: {document}...")


def main():
    msp = MySuperPrinter()
    msp.print("Working")
    msp.fax("Working")
    msp.scan("Working")

    ofp = OldFashionPrintter()
    ofp.print("Working")

    pc = Photocopier()
    pc.print("Working")
    pc.scan("Working")


if __name__ == "__main__":
    main()
