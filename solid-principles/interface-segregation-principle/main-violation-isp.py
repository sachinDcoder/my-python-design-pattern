from abc import ABC, abstractmethod


class Machine(ABC):
    @abstractmethod
    def print(self, document):
        raise NotImplementedError()

    @abstractmethod
    def fax(self, document):
        raise NotImplementedError()

    @abstractmethod
    def scan(self, document):
        raise NotImplementedError()


# It is okay if we need a multi printer which supports all
class MultiFunctionPrinter(Machine):

    def print(self, document):
        print(f"MultiFunctionPrinter is printing the document: {document}...")

    def fax(self, document):
        print(f"MultiFunctionPrinter is faxing the document: {document}...")

    def scan(self, document):
        print(f"MultiFunctionPrinter is scanning the document: {document}...")


# Getting ISP violation
class OldFashionPrintter(Machine):
    def print(self, document):
        print(f"OldFashionPrintter is printing the document: {document}...")

    def fax(self, document):
        pass  # do-nothing

    def scan(self, document):
        """Not Supported"""
        raise NotImplementedError("Printer can scan!")


def main():
    mfp = MultiFunctionPrinter()
    mfp.print("Working")
    mfp.fax("Working")
    mfp.scan("Working")

    ofp = OldFashionPrintter()
    ofp.print("Working")
    ofp.fax("Working")
    ofp.scan("Working")


if __name__ == "__main__":
    main()
