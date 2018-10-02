from pracmln.mlnquery import MLNQuery
from markov_logic_network.grasping_type_mln import grasping_type_pracmln_project, grasping_type_mln
from markov_logic_network.database import Database

if __name__ == "__main__":

    project = grasping_type_pracmln_project
    query_config = project.queryconf
    evidence_database = Database(grasping_type_mln)
    evidence_database.add_ground_atom_with_truth_value('facing_robot_face(front)', 1.0)
    evidence_database.add_ground_atom_with_truth_value('bottom_face(bottom)', 1.0)
    evidence_database.add_ground_atom_with_truth_value('is_a(tankard.n.01, mug.n.01)', 0.66)
    evidence_database.add_ground_atom_with_truth_value('is_a(tankard.n.01, cup.n.01)', 0.33)
    evidence_database.add_ground_atom_with_truth_value('is_a(tankard.n.01, knife.n.01)', 0.1)
    evidence_database.add_ground_atom_with_truth_value('obj_to_be_grasped(tankard.n.01)', 1.0)

    mln_query = MLNQuery(query_config, mln=grasping_type_mln, db=evidence_database.pracmln_database)
    result = mln_query.run()
    pass