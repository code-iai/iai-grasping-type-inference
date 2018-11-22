from grasping_type_inference.grasping_object.grasping_object import GraspingObject
from grasping_type_inference.grasping_object.orientation import Orientation


class Inference(object):
    def __init__(self, *evidences):
        self._facing_robot_face, self._bottom_face, self._object_type = evidences

    def get_most_probable_result(self):
        orientation = Orientation(self._facing_robot_face, self._bottom_face)
        grasping_object = GraspingObject(self._object_type, orientation)

        result = grasping_object.get_most_probable_grasping_type()

        solution = None
        max_prob = 0

        for ground_atom in result.results.keys():
            if result.results[ground_atom] >= max_prob:
                solution = ground_atom
                max_prob = result.results[ground_atom]

        return solution