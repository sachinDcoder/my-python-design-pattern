from enum import Enum, auto


class State(Enum):
    LOCKED = auto()
    FAILED = auto()
    UNLOCKED = auto()


def main():
    code = '1234'
    state = State.LOCKED
    entry = ''

    while True:
        if state == State.LOCKED:
            entry += input(entry)
            if entry == code:
                state = State.UNLOCKED
            if not code.startswith(entry):
                state = State.FAILED
        elif state == State.FAILED:
            print('FAILED')
            state = State.LOCKED
            entry = ''
        elif state == State.LOCKED:
            print('LOCKED')
        elif state == State.UNLOCKED:
            print('UNLOCKED')
            break
        else:
            print('Invalid')


if __name__ == "__main__":
    main()
