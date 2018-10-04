import unittest
from grasping_object.rotationally_symmetrical_grasping_object import RotationallySymmetricalGraspingObject
from test.utils.test_object_generator import FACING_ROBOT_FACE, BOTTOM_FACE


class EqualsTest(unittest.TestCase):
    def test_should_return_true_if_rotationally_symmetrical_grapsing_objects_are_equal(self):
        object_1 = RotationallySymmetricalGraspingObject(FACING_ROBOT_FACE, BOTTOM_FACE)
        object_2 = RotationallySymmetricalGraspingObject(FACING_ROBOT_FACE, BOTTOM_FACE)
        actual = object_1 == object_2
        self.assertEqual(actual, True)

    def test_should_return_false_if_rotationally_symmetrical_grapsing_objects_are_not_equal(self):
        object_1 = RotationallySymmetricalGraspingObject(FACING_ROBOT_FACE, BOTTOM_FACE)
        object_2 = RotationallySymmetricalGraspingObject(BOTTOM_FACE, FACING_ROBOT_FACE)
        actual = object_1 == object_2
        self.assertEqual(actual, False)


if __name__ == '__main__':
    unittest.main()
