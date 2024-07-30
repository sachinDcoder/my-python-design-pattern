from abc import ABC, abstractmethod


class Game(ABC):
    def __init__(self, number_of_players):
        self.number_of_players = number_of_players
        self.current_player = 0

    def run(self):
        self.start()
        while not self.have_winner:
            self.take_turn()
        print(f'Player {self.winning_player} wins!')

    @property
    @abstractmethod
    def have_winner(self):
        pass

    @property
    @abstractmethod
    def winning_player(self):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def take_turn(self):
        pass


class Chess(Game):
    def __init__(self):
        super().__init__(2)
        self.max_turns = 10  # Simulation
        self.turn = 1

    def start(self):
        print(f'Starting the chess game with {self.number_of_players} players...')

    def take_turn(self):
        print(f'Turn {self.turn} taken by the player {self.current_player}')
        self.turn += 1
        self.current_player = 1 - self.current_player

    @property
    def have_winner(self):
        return self.turn == self.max_turns

    @property
    def winning_player(self):
        return self.current_player


def main():
    chess_game = Chess()
    chess_game.run()


if __name__ == "__main__":
    main()



