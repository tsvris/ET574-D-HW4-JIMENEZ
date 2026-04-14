import unittest
from main import Reel, SlotMachine


class TestSlotMachine(unittest.TestCase):

    #  1. Test Reel spin bounds
    def test_reel_spin_bounds(self):
        reel = Reel()
        for _ in range(100):  # test multiple spins
            value = reel.spin()
            self.assertTrue(0 <= value <= 9)

    #  2. Test evaluate_spin outcomes
    def test_evaluate_spin(self):
        machine = SlotMachine()

        self.assertEqual(machine.evaluate_spin(5, 5, 5), "Win")
        self.assertEqual(machine.evaluate_spin(0, 3, 7), "Lose")
        self.assertEqual(machine.evaluate_spin(2, 3, 4), "Spin Again")

    #  3. Test play_round return structure
    def test_play_round_structure(self):
        machine = SlotMachine()
        result = machine.play_round()

        self.assertEqual(len(result), 5)
        self.assertIsInstance(result[0], int)
        self.assertIsInstance(result[1], int)
        self.assertIsInstance(result[2], int)
        self.assertIsInstance(result[3], int)
        self.assertIsInstance(result[4], str)

    #extra tests

    #  4. Edge case: all zeros → should be Win
    def test_all_zeros(self):
        machine = SlotMachine()
        result = machine.evaluate_spin(0, 0, 0)
        self.assertEqual(result, "Win")

    #  5. All same non-zero values → Win
    def test_all_same_values(self):
        machine = SlotMachine()
        result = machine.evaluate_spin(9, 9, 9)
        self.assertEqual(result, "Win")

    #  6. No match and no zero → Spin Again
    def test_no_match_no_zero(self):
        machine = SlotMachine()
        result = machine.evaluate_spin(1, 2, 3)
        self.assertEqual(result, "Spin Again")

    #  7. Any zero (not all same) → Lose
    def test_contains_zero(self):
        machine = SlotMachine()
        result = machine.evaluate_spin(0, 5, 5)
        self.assertEqual(result, "Lose")


if __name__ == "__main__":
    unittest.main()