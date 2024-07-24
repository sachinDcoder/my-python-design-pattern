import random
from typing import List, Optional


class Player:
    def __init__(self, name: str):
        self.name = name
        self.position = 1

    def update_position(self, new_position: int):
        self.position = new_position

    def move(self, no_of_steps: int):
        self.position += no_of_steps


class Dice:
    def __init__(self, side: int = 6):
        self.side = side

    def roll(self) -> int:
        return random.randint(1, self.side)


class Board:
    def __init__(self, size):
        self.size = size
        self.snakes = {}
        self.ladders = {}

    def add_snake(self, start: int, end: int):
        self.snakes[start] = end

    def add_ladder(self, start: int, end: int):
        self.ladders[start] = end

    def get_new_position(self, position: int):
        if position in self.snakes:
            return self.snakes[position]
        elif position in self.ladders:
            return self.ladders[position]
        else:
            return position


class Game:
    def __init__(self, board: Board, dice: Dice, players: List[Player]):
        self.board = board
        self.players = players
        self.dice = dice
        self.curr_player = 0

    def play_turn(self) -> Optional[Player]:
        player = self.players[self.curr_player]
        curr_player_position = player.position
        steps = self.dice.roll()
        new_position = self.board.get_new_position(curr_player_position + steps)
        if self.check_winner(new_position):
            return player

        if new_position < self.board.size:
            player.position = new_position
        self.curr_player = (self.curr_player + 1) % len(self.players)
        return None

    def check_winner(self, new_position: int) -> bool:
        if new_position == self.board.size:
            return True
        return False


class SnakeAndLadder:
    def __init__(self):
        self.game = None

    def play(self):
        board = Board(100)

        # Add snakes and ladders
        board.add_snake(16, 1)
        board.add_snake(47, 27)
        board.add_snake(49, 18)
        board.add_snake(56, 17)
        board.add_snake(62, 15)
        board.add_snake(64, 56)
        board.add_snake(87, 13)
        board.add_snake(93, 19)
        board.add_snake(95, 10)
        board.add_snake(98, 43)

        board.add_ladder(2, 98)
        board.add_ladder(3, 14)
        board.add_ladder(4, 31)
        board.add_ladder(5, 42)
        board.add_ladder(28, 84)
        board.add_ladder(36, 44)
        board.add_ladder(51, 67)
        board.add_ladder(71, 91)
        board.add_ladder(80, 100)

        dice = Dice()
        player_a = Player("A")
        player_b = Player("B")

        self.game = Game(board, dice, [player_a, player_b])

        winner = self.game.play_turn()
        while winner is None:
            winner = self.game.play_turn()

        return winner.name


def main():
    snake_ladder = SnakeAndLadder()
    print(snake_ladder.play())


if __name__ == "__main__":
    main()


