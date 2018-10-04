import unittest
from test.utils.test_object_generator import get_grasping_object
import markov_logic_network.grasping_type_mln as grasping_type_mln


class GraspingTypeInfererTest(unittest.TestCase):
    def test_test(self):
        grasping_object = get_grasping_object()
        grasping_object_database = grasping_object.transform_to_mln_database(grasping_type_mln.get_mln())
        self.assertEqual(True, True)


if __name__ == "__main__":
    unittest.main()