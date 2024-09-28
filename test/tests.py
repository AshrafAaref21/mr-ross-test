import unittest

# Assuming the calculate_discount function is in the same module
from function import calculate_discount

class TestCalculateDiscount(unittest.TestCase):
    """Unit tests for the calculate_discount function."""

    def setUp(self):
        """Set up test fixtures, if needed."""
        # In this case, no external dependencies or complex setups are required.
        pass

    def tearDown(self):
        """Clean up test fixtures, if needed."""
        # No teardown actions required as no state is maintained.
        pass

    def test_regular_customer_discount(self):
        """Test discount calculation for regular customers."""
        self.assertEqual(calculate_discount(500, "regular"), 0.05)
        self.assertEqual(calculate_discount(1001, "regular"), 0.1)
    
    def test_vip_customer_discount(self):
        """Test discount calculation for VIP customers."""
        self.assertEqual(calculate_discount(600, "vip"), 0.15)
        self.assertEqual(calculate_discount(300, "vip"), 0.1)
    
    def test_new_customer_discount(self):
        """Test discount calculation for new customers."""
        self.assertEqual(calculate_discount(200, "new"), 0.05)

    def test_invalid_customer_type(self):
        """Test invalid customer type raises ValueError."""
        with self.assertRaises(ValueError) as context:
            calculate_discount(500, "invalid")
        self.assertEqual(str(context.exception), "Invalid customer type")

    def test_negative_total_amount(self):
        """Test negative total amount raises ValueError."""
        with self.assertRaises(ValueError) as context:
            calculate_discount(-100, "regular")
        self.assertEqual(str(context.exception), "Total amount must be positive")

    def test_zero_total_amount(self):
        """Test total amount of zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            calculate_discount(0, "vip")
        self.assertEqual(str(context.exception), "Total amount must be positive")
    
    def test_boundary_total_amount(self):
        """Test boundary condition for total amount."""
        self.assertEqual(calculate_discount(1000, "regular"), 0.05)
        self.assertEqual(calculate_discount(500, "vip"), 0.1)

    @unittest.skip("Demonstration of a skipped test")
    def test_example_skipped(self):
        """This test will be skipped."""
        self.assertEqual(calculate_discount(0, "regular"), 0)

    def test_parameterized_discounts(self):
        """Test multiple cases using parameterized inputs."""
        cases = [
            (1001, "regular", 0.1),
            (500, "regular", 0.05),
            (600, "vip", 0.15),
            (300, "vip", 0.1),
            (100, "new", 0.05)
        ]
        for total_amount, customer_type, expected_discount in cases:
            with self.subTest(total_amount=total_amount, customer_type=customer_type):
                self.assertEqual(calculate_discount(total_amount, customer_type), expected_discount)

if __name__ == "__main__":
    unittest.main()
