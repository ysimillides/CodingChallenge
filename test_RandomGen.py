import unittest
import next_num as man_ahl


class TestRandomGen(unittest.TestCase):
    """
    This class tests that the RandomGen class  functions properly, raising the required error messages where relevant,
    and giving the necessary output. As the numbers are supposedly random in our original class, we test the class
    against special input cases, such as prob =1 , and then we further check that all error messages are correctly raised
    for incorrect input
    """
    #Initially this test was to check what happens when prob = 0. This has now being written into the class
    # def test_prob0(self):
    #     test_nums = [-1, 0, 1, 2, 3]
    #     test_probabilities = [0.0, 0, 0, 0, 0]
    #     instance = man_ahl.RandomGen(test_nums, test_probabilities)
    #     self.assertEqual(instance.next_num(), "No answer, probabilities where equal to zero")

    def test_prob1(self):
        test_nums = [-1, 0, 1, 2, 3]
        test_probabilities = [0, 0, 1, 0, 0]
        instance = man_ahl.RandomGen(test_nums, test_probabilities)
        self.assertEqual(instance.next_num(), 1)

    def test_raise_error_length(self):
        test_nums = [-1, 0, 1, 2, 3, 4, 5]
        test_probabilities = [0, 0, 1, 0, 0]
        with self.assertRaises(ValueError):
            instance = man_ahl.RandomGen(test_nums, test_probabilities)

    def test_raise_error_negative(self):
        test_nums = [-1, 0, 1, 2, 3]
        test_probabilities = [-1, 0.2, 1, 0.4, 0.4]
        with self.assertRaises(ValueError):
            instance = man_ahl.RandomGen(test_nums, test_probabilities)

    def test_raise_error_greater_one(self):
        test_nums = [-1, 0, 1, 2, 3]
        test_probabilities = [0, 1.1, 0, 0.1, 0.2]
        with self.assertRaises(ValueError):
             instance = man_ahl.RandomGen(test_nums, test_probabilities)

    def test_raise_error_total_(self):
        test_nums = [-1, 0, 1, 2, 3]
        test_probabilities = [0.3, 0.3, 0.3, 0.1, 0.1]
        with self.assertRaises(ValueError):
            instance = man_ahl.RandomGen(test_nums, test_probabilities)

if __name__ == '__main__':
    unittest.main()
