import unittest

from src.Utils.statistics import calculate_third_quartil


class TestQuartileCalculation(unittest.TestCase):

    def test_empty_list(self):
        """Test when the list is empty."""
        result = calculate_third_quartil([])
        self.assertEqual(result, 0)

    def test_single_element(self):
        """Test when the list has one element."""
        result = calculate_third_quartil([10])
        self.assertEqual(result, 10)

    def test_multiple_elements(self):
        """Test with a list of multiple elements."""
        result = calculate_third_quartil([1, 2, 3, 4, 5])
        self.assertAlmostEqual(result, 4)

    def test_with_negative_numbers(self):
        """Test with a list that includes negative numbers."""
        result = calculate_third_quartil([-5, -1, 0, 1, 3])
        self.assertAlmostEqual(result, 1)


if __name__ == "__main__":
    unittest.main()
