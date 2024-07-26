import time


def time_it(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f"{func.__name__} took {int(end - start) * 1000} ms")

    return wrapper


@time_it
def some_op_with_decorator():
    print("Starting Operation")
    time.sleep(1)
    print("Operation Done")
    return "Done"


def some_op_without_decorator():
    print("Starting Operation")
    time.sleep(1)
    print("Operation Done")
    return "Done"


def main():
    some_op_with_decorator()
    time_it(some_op_without_decorator)()


if __name__ == "__main__":
    main()