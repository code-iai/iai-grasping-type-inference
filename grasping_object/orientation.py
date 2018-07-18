class Orientation:
    def __init__(self, facing_robot_face, bottom_face):
        self.facing_robot_face = facing_robot_face
        self.bottom_face = bottom_face

    def transform_facing_robot_face_to_ground_atom(self):
        return 'facing_robot_face({})'.format(self.facing_robot_face.value)

    def transform_bottom_face_to_ground_atom(self):
        return 'bottom_face({})'.format(self.bottom_face.value)
