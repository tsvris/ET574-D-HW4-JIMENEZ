import random


class Reel:
    def __init__(self, max_value=9):
        self.max_value = max_value

    def spin(self):
        return random.randint(0, self.max_value)


class SlotMachine:
    def __init__(self):
        self.reel1 = Reel()
        self.reel2 = Reel()
        self.reel3 = Reel()

    def evaluate_spin(self, r1, r2, r3):
        # All match → Win
        if r1 == r2 == r3:
            return "Win"
        # Any zero → Lose
        elif 0 in (r1, r2, r3):
            return "Lose"
        # Otherwise → Spin Again
        else:
            return "Spin Again"

    def play_round(self):
        r1 = self.reel1.spin()
        r2 = self.reel2.spin()
        r3 = self.reel3.spin()

        total = r1 + r2 + r3
        result = self.evaluate_spin(r1, r2, r3)

        return (r1, r2, r3, total, result)


def main():
    machine = SlotMachine()

    while True:
        print("\n--- Slot Machine ---")
        print("1. Play a round")
        print("2. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            r1, r2, r3, total, result = machine.play_round()
            print(f"Reels: {r1}, {r2}, {r3}")
            print(f"Total: {total}")
            print(f"Result: {result}")

        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()