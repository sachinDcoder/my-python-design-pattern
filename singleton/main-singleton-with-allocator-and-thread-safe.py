import threading


class Database:
    _instance = None
    _lock = threading.Lock()  # Adding a lock for thread safety

    def __init__(self):
        """
        Initializes the database. This method is called every time an instance is created,
        but it will always return the same instance due to the Singleton pattern.
        """
        print("Loading the database...")

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:  # Double-checked locking for thread safety
                    cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)

        return cls._instance


def main():
    d1 = Database()
    d2 = Database()
    print(d1 == d2)


if __name__ == "__main__":
    main()
