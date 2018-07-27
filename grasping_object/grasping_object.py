from markov_logic_network.database import Database
import markov_logic_network.ground_atom_builder as gab


class GraspingObject(object):
    def __init__(self, object_type, orientation):
        self.type = object_type
        self.orientation = orientation

    def transform_to_mln_database(self, mln):
        database = Database(mln)

        database.add_true_ground_atom(gab.get_obj_to_be_grasped(self.type))
        database.add_true_ground_atom(self.orientation.transform_facing_robot_face_to_ground_atom())
        database.add_true_ground_atom(self.orientation.transform_bottom_face_to_ground_atom())

        return database

    def __eq__(self, other):
        if (self.type != other.type) or (self.orientation != other.orientation):
            return False
        else:
            return True
