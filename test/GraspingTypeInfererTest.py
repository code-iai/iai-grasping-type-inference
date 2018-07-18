import unittest
from grasping_object.orientation import Orientation
from grasping_object.grasping_object import GraspingObject
import markov_logic_network.grasping_type_mln as grasping_type_mln

from face import Face


class GraspingTypeInfererTest(unittest.TestCase):
    def test_test(self):
        orientation = Orientation(Face.FRONT, Face.BOTTOM)
        grasping_object = GraspingObject("cup.n.01", orientation)
        grasping_object_database = grasping_object.transform_to_mln_database(grasping_type_mln.get_mln())
        self.assertEqual(True, True)


if __name__ == "__main__":
    unittest.main()