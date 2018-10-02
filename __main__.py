from pracmln.mlnquery import MLNQuery
from markov_logic_network.grasping_type_mln import grasping_type_pracmln_project, grasping_type_mln
from word_net import determine_path_similarity_between_two_concepts
from grasping_object.grasping_object import GraspingObject
from grasping_object.orientation import Orientation

if __name__ == "__main__":

    project = grasping_type_pracmln_project
    query_config = project.queryconf

    orientation = Orientation('front', 'bottom')
    grasping_object = GraspingObject('tankard.n.01', orientation)

    evidence_database = grasping_object.transform_to_mln_database(grasping_type_mln)

    for learned_object in grasping_type_mln.domains['learnedObject']:
        similarity = determine_path_similarity_between_two_concepts(grasping_object.type, learned_object)
        ground_atom = 'is_a({},{})'.format(grasping_object.type, learned_object)
        evidence_database.add_ground_atom_with_truth_value(ground_atom, similarity)

    mln_query = MLNQuery(query_config, mln=grasping_type_mln, db=evidence_database.pracmln_database, verbose=0)

    result = mln_query.run()
    for ground_atom in result.results.keys():
        if result.results[ground_atom] == 1:
            print ground_atom
