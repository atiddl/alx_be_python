import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method with various scenarios."""
        self.assertEqual(self.calc.add(2, 3), 5)          # Basic addition
        self.assertEqual(self.calc.add(-1, 1), 0)         # Negative and positive
        self.assertEqual(self.calc.add(0, 0), 0)          # Zeros
        self.assertEqual(self.calc.add(-5, -5), -10)      # Two negatives
        self.assertEqual(self.calc.add(100, 200), 300)    # Larger numbers

    def test_subtraction(self):
        """Test the subtraction method with various scenarios."""
        self.assertEqual(self.calc.subtract(10, 5), 5)    # Basic subtraction
        self.assertEqual(self.calc.subtract(-1, 1), -2)   # Negative result
        self.assertEqual(self.calc.subtract(0, 0), 0)     # Zeros
        self.assertEqual(self.calc.subtract(-5, -5), 0)   # Two negatives
        self.assertEqual(self.calc.subtract(100, 200), -100)  # Negative result

    def test_multiplication(self):
        """Test the multiplication method with various scenarios."""
        self.assertEqual(self.calc.multiply(2, 3), 6)     # Basic multiplication
        self.assertEqual(self.calc.multiply(-1, 1), -1)   # Negative and positive
        self.assertEqual(self.calc.multiply(0, 5), 0)     # Zero multiplication
        self.assertEqual(self.calc.multiply(-5, -5), 25)  # Two negatives
        self.assertEqual(self.calc.multiply(10, 0), 0)    # Zero multiplication

    def test_division(self):
        """Test the division method with various scenarios."""
        self.assertEqual(self.calc.divide(10, 5), 2.0)    # Basic division
        self.assertEqual(self.calc.divide(-10, 5), -2.0)  # Negative dividend
        self.assertEqual(self.calc.divide(0, 5), 0.0)     # Zero dividend
        self.assertEqual(self.calc.divide(10, -5), -2.0)  # Negative divisor
        self.assertIsNone(self.calc.divide(10, 0))        # Division by zero
        self.assertIsNone(self.calc.divide(0, 0))         # Zero by zero

if __name__ == "__main__":
    unittest.main()