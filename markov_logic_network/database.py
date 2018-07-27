from pracmln.mln.database import Database as PRACMLNDatabase


class Database():
    def __init__(self, pracmln_mln):
        self.pracmln_database = PRACMLNDatabase(pracmln_mln)

    def add_true_ground_atom(self, ground_atom):
        self.__add_ground_atom_with_truth_value__(ground_atom, 1.0)

    def add_false_ground_atom(self, ground_atom):
        self.__add_ground_atom_with_truth_value__(ground_atom, 0.0)

    def __add_ground_atom_with_truth_value__(self, ground_atom, truth_value):
        self.pracmln_database.add(ground_atom, truth_value)

    def get_all_ground_atoms_with_their_truth_values(self):
        return self.pracmln_database.gndatoms()

    def __eq__(self, other):
        return False

