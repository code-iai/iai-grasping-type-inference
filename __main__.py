import os

from pracmln.mlnquery import MLNQuery

from definitions import ROOT_DIR
from markov_logic_network.grasping_type_mln import grasping_type_pracmln_project, grasping_type_mln
from markov_logic_network.is_a_generator import get_is_a_ground_atoms
from grasping_object.grasping_object import GraspingObject
from grasping_object.orientation import Orientation
from markov_logic_network.mln import MarkovLogicNetwork

if __name__ == "__main__":
    path_to_grasping_type_mln = os.path.join(ROOT_DIR, 'mln', 'grasping_type.pracmln')
    mln = MarkovLogicNetwork(path_to_grasping_type_mln)

    orientation = Orientation('front', 'bottom')
    grasping_object = GraspingObject('tankard.n.01', orientation)

    learned_objects = grasping_type_mln.domains['learnedObject']

    evidence_database = grasping_object.transform_to_mln_database(grasping_type_mln)
    is_a_ground_atoms = get_is_a_ground_atoms(grasping_object.type, learned_objects)

    for ground_atom in is_a_ground_atoms.keys():
        similarity = is_a_ground_atoms[ground_atom]
        evidence_database.add_ground_atom_with_truth_value(ground_atom, similarity)

    result = mln.infer(evidence_database)

    for ground_atom in result.results.keys():
        if result.results[ground_atom] == 1:
            print ground_atom
