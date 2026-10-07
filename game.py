import random
from logic import feedback


class Mastermind:
    DIFFICULTIES = {
        "easy": {"length": 3, "symbols": "1234", "turns": 12},
        "medium": {"length": 4, "symbols": "123456", "turns": 10},
        "hard": {"length": 5, "symbols": "12345678", "turns": 8},
    }

    def __init__(self, difficulty="medium"):
        settings = self.DIFFICULTIES[difficulty]
        self.difficulty = difficulty
        self.length = settings["length"]
        self.symbols = settings["symbols"]
        self.code = [random.choice(self.symbols) for _ in range(self.length)]
        self.history = []
        self.turns = settings["turns"]
        self.status = "playing"

    def run(self):
        if self.status != "playing":
            return

        print("Mastermind — choose a difficulty: easy, medium, or hard.")
        difficulty = input("Difficulty > ").strip().lower()

        while difficulty not in self.DIFFICULTIES:
            print("Invalid difficulty. Choose easy, medium, or hard.")
            difficulty = input("Difficulty > ").strip().lower()

        settings = self.DIFFICULTIES[difficulty]
        self.difficulty = difficulty
        self.length = settings["length"]
        self.symbols = settings["symbols"]
        self.code = [random.choice(self.symbols) for _ in range(self.length)]
        self.history = []
        self.turns = settings["turns"]
        self.status = "playing"

        print(
            f"Mastermind — enter {self.length} digits from "
            f"{self.symbols[0]} to {self.symbols[-1]}."
        )

        while self.status == "playing" and self.turns:
            raw = input(f"{self.turns} turns left > ").strip()

            if raw.lower() == "q":
                self.status = "quit"
                return

            if len(raw) != self.length or any(ch not in self.symbols for ch in raw):
                print(
                    f"Enter exactly {self.length} digits from "
                    f"{self.symbols[0]} to {self.symbols[-1]}."
                )
                continue

            guess = list(raw)
            exact, partial = feedback(self.code, guess)
            self.history.append((raw, exact, partial))
            self.turns -= 1

            print("Exact:", exact, " Partial:", partial)

            print("History:")
            for previous_guess, previous_exact, previous_partial in self.history:
                print(
                    f"  {previous_guess} -> "
                    f"Exact: {previous_exact}, Partial: {previous_partial}"
                )

            if exact == self.length:
                self.status = "won"
                print("Cracked the code!")
                return

        if self.status == "playing" and self.turns == 0:
            self.status = "lost"
            print("Game over! The code was", "".join(self.code))