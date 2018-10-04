from markov_logic_network.database import Database
import markov_logic_network.ground_atom_builder as gab
from markov_logic_network.grasping_type_mln import grasping_type_mln
from markov_logic_network.is_a_generator import get_is_a_ground_atoms


class GraspingObject(object):
    def __init__(self, object_type, orientation):
        self.type = object_type
        self.orientation = orientation

    def get_most_probable_grasping_type(self):
        learned_objects = grasping_type_mln.domains['learnedObject']

        evidence_database = self.transform_to_mln_database(grasping_type_mln)
        is_a_ground_atoms = get_is_a_ground_atoms(self.type, learned_objects)

        for ground_atom in is_a_ground_atoms.keys():
            similarity = is_a_ground_atoms[ground_atom]
            evidence_database.add_ground_atom_with_truth_value(ground_atom, similarity)

        return grasping_type_mln.infer(evidence_database)

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
