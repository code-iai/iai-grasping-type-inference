import unittest
from face import Face
from grasping_object.orientation import Orientation


class FacingRobotFaceToGroundAtomTest(unittest.TestCase):
    def test_should_return_facing_robot_face_top_as_ground_atom(self):
        expected_value = "facing_robot_face(top)"
        orientation = Orientation(Face.TOP, Face.BOTTOM)

        self.assertEqual(orientation.transform_facing_robot_face_to_ground_atom(), expected_value)


if __name__ == "__main__":
    unittest.main()