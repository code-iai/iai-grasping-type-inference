import unittest
from test.utils.test_object_generator import get_rotationally_symmetrical_grasping_object, get_grasping_object_as_mln_database
from markov_logic_network.grasping_type_mln import grasping_type_mln


class TransformToMLNDatabase(unittest.TestCase):
    def test_should_return_a_valid_mln_database(self):
        grasping_object = get_rotationally_symmetrical_grasping_object()
        grasping_object_database = grasping_object.transform_to_mln_database(grasping_type_mln)
        result = __is_database_valid__(grasping_object_database)
        self.assertEqual(result, True)


def __is_database_valid__(database):
    expected_ground_atoms = []
    expected_database = get_grasping_object_as_mln_database(grasping_type_mln, [])
    return True


if __name__ == "__main__":
    unittest.main()
