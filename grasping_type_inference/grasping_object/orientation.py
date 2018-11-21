import grasping_type_inference.ground_atom_builder as gab


class Orientation:
    def __init__(self, facing_robot_face, bottom_face):
        self.facing_robot_face = facing_robot_face
        self.bottom_face = bottom_face

    def transform_facing_robot_face_to_ground_atom(self):
        return gab.get_facing_robot_face(self.facing_robot_face)

    def transform_bottom_face_to_ground_atom(self):
        return gab.get_bottom_face(self.bottom_face)

    def __eq__(self, other):
        if (self.facing_robot_face != other.facing_robot_face) or (self.bottom_face != other.bottom_face):
            return False
        else:
            return True

