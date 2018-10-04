from pracmln.mln.database import Database as PRACMLNDatabase


class Database():
    def __init__(self, mln):
        self.pracmln_database = PRACMLNDatabase(mln.pracmln)

    def add_true_ground_atom(self, ground_atom):
        self.add_ground_atom_with_truth_value(ground_atom, 1.0)

    def add_false_ground_atom(self, ground_atom):
        self.add_ground_atom_with_truth_value(ground_atom, 0.0)

    def get_ground_atoms_with_truth_values(self):
        return self.pracmln_database.gndatoms()

    def add_ground_atom_with_truth_value(self, ground_atom, truth_value):
        self.pracmln_database.add(ground_atom, truth_value)

    def __eq__(self, other):
        ground_atoms_with_truth_values = \
            __transform_ground_atoms_with_truth_values_to_hash_map__(self.get_ground_atoms_with_truth_values())
        other_ground_atoms_with_truth_values = \
            __transform_ground_atoms_with_truth_values_to_hash_map__(other.get_ground_atoms_with_truth_values())

        return ground_atoms_with_truth_values == other_ground_atoms_with_truth_values


def __transform_ground_atoms_with_truth_values_to_hash_map__(ground_atoms_with_truth_values):
    hash_map = dict()

    for ground_atom, truth_value in ground_atoms_with_truth_values:
        hash_map[ground_atom] = truth_value

    return hash_map
