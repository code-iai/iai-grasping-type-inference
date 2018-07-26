from pracmln.mln.database import Database as PRACMLNDatabase


class Database():
    def __init__(self, pracmln_mln):
        self.pracmln_database = PRACMLNDatabase(pracmln_mln)

    def add_ground_atom(self, ground_atom):
        self.pracmln_database.add(ground_atom)

    def __eq__(self, other):
        return True

    def get_all_ground_atoms_with_their_truth_values(self):
        return self.pracmln_database.gndatoms()

