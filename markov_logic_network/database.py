from pracmln.mln.database import Database as PRACMLNDatabase


class Database():
    def __init__(self, pracmln_mln):
        self.pracmln_database = PRACMLNDatabase(pracmln_mln)

    def add_ground_atom(self, ground_atom):
        self.pracmln_database.add(ground_atom)
