import unittest


class AllGroundAtomsWithTheirTruthValuesTest(unittest.TestCase):
    def test_should_return_all_ground_atoms_with_correct_truth_values(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
