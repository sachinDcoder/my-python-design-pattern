from enum import Enum, auto


class State(Enum):
    OFF_HOOK = auto()
    CONNECTING = auto()
    CONNECTED = auto()
    ON_HOLD = auto()
    ON_HOOK = auto()


class Trigger(Enum):
    CALL_DIALED = auto()
    HANG_UP = auto()
    CALL_CONNECTED = auto()
    PLACED_ON_HOLD = auto()
    TAKEN_OFF_HOLD = auto()
    LEFT_MESSAGE = auto()


def main():
    rules = {
        State.OFF_HOOK: [
            (Trigger.CALL_DIALED, State.CONNECTING)
        ],
        State.CONNECTING: [
            (Trigger.HANG_UP, State.ON_HOOK),
            (Trigger.CALL_CONNECTED, State.CONNECTED)
        ],
        State.CONNECTED: [
            (Trigger.PLACED_ON_HOLD, State.ON_HOLD),
            (Trigger.LEFT_MESSAGE, State.ON_HOOK),
            (Trigger.HANG_UP, State.ON_HOOK)
        ],
        State.ON_HOLD: [
            (Trigger.TAKEN_OFF_HOLD, State.CONNECTED),
            (Trigger.HANG_UP, State.ON_HOOK),
        ]
    }

    state = State.OFF_HOOK
    exit_state = State.ON_HOOK

    while state != exit_state:
        print(f'The phone is currently {str(state.name).lower()}')

        for i in range(len(rules[state])):
            t = rules[state][i][0]
            print(f'{i}: {t}')

        try:
            idx = int(input("Select the trigger: "))
            state = rules[state][idx][1]
        except IndexError as e:
            print(f'Invalid input {e}. Please try again..')

    print("We are done using the phone!")


if __name__ == "__main__":
    main()