from high_level_markov_logic_network.database import Database
from high_level_markov_logic_network.fuzzy_markov_logic_network.is_a_generator import get_is_a_ground_atoms
import grasping_type_inference.ground_atom_builder as gab
from grasping_type_inference.grasping_type_mln import grasping_type_mln


class GraspingObject(object):
    def __init__(self, object_type, orientation):
        self.type = object_type
        self.orientation = orientation

    def get_most_probable_grasping_type(self):
        learned_objects = grasping_type_mln.domains['learnedObject']

        evidence_database = self.transform_to_mln_database(grasping_type_mln)
        is_a_ground_atoms = get_is_a_ground_atoms(self.type, learned_objects)

        for ground_atom in is_a_ground_atoms:
            evidence_database.add_ground_atom(ground_atom)

        print 'Evidence database:'

        for evidence in evidence_database.ground_atoms:
            print evidence

        return grasping_type_mln.infer(evidence_database)

    def transform_to_mln_database(self, mln):
        database = Database(mln)

        database.add_ground_atom(gab.get_obj_to_be_grasped(self.type))
        database.add_ground_atom(self.orientation.transform_facing_robot_face_to_ground_atom())
        database.add_ground_atom(self.orientation.transform_bottom_face_to_ground_atom())

        return database

    def __eq__(self, other):
        if (self.type != other.type) or (self.orientation != other.orientation):
            return False
        else:
            return True
