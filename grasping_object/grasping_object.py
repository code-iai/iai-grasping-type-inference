from markov_logic_network.database import Database


class GraspingObject:
    def __init__(self, object_type, orientation):
        self.type = object_type
        self.orientation = orientation

    def transform_to_mln_database(self, mln):
        database = Database(mln)

        database.add_ground_atom(self.__transform_type_to_ground_atom__())
        database.add_ground_atom(self.orientation.transform_facing_robot_face_to_ground_atom())
        database.add_ground_atom(self.orientation.transform_bottom_face_to_ground_atom())

        return database

    def __transform_type_to_ground_atom__(self):
        return 'obj_to_be_grasped({})'.format(self.type)