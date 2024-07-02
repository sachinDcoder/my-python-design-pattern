class Database:
    _instance = None

    def __init__(self):
        """
        Initializes the database. This method is called every time an instance is created,
        but it will always return the same instance due to the Singleton pattern.
        """
        print("Loading the database...")

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)

        return cls._instance


def main():
    d1 = Database()
    d2 = Database()
    print(d1 == d2)


if __name__ == "__main__":
    main()