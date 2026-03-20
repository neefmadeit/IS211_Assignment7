import random

# Set seed for testability
random.seed(0)

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_points(self, points):
        self.score += points


class PigGame:
    def __init__(self):
        self.die = Die()
        self.player1 = Player("Player 1")
        self.player2 = Player("Player 2")
        self.current_player = self.player1

    def switch_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def play_turn(self):
        turn_total = 0
        print(f"\n{self.current_player.name}'s turn!")

        while True:
            print(f"Current turn total: {turn_total}, Total game score: {self.current_player.score}")
            choice = input("Roll (r) or Hold (h)? ").strip().lower()

            while choice not in ['r', 'h']:
                choice = input("Please enter 'r' to roll or 'h' to hold: ").strip().lower()

            if choice == 'r':
                roll = self.die.roll()
                print(f"{self.current_player.name} rolled: {roll}")

                if roll == 1:
                    print("Rolled a 1! Turn over. No points added.")
                    return  # Turn ends, no points added
                else:
                    turn_total += roll

            elif choice == 'h':
                print(f"{self.current_player.name} holds.")
                self.current_player.add_points(turn_total)
                print(f"Added {turn_total} points to total score.")
                return

    def play(self):
        print("Welcome to the game of Pig!")
        while self.player1.score < 100 and self.player2.score < 100:
            self.play_turn()
            self.switch_player()

        # Game over
        winner = self.player1 if self.player1.score >= 100 else self.player2
        print(f"\n{winner.name} wins with a score of {winner.score}!")
        print("Game over.")


# Run the game
if __name__ == "__main__":
    game = PigGame()
    game.play()