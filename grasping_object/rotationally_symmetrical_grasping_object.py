from grasping_object import GraspingObject
import markov_logic_network.ground_atom_builder as gab


class RotationallySymmetricalGraspingObject(GraspingObject):
    def __init__(self, object_type, orientation):
        super(RotationallySymmetricalGraspingObject, self).__init__(object_type, orientation)

    def transform_to_mln_database(self, mln):
        database = super(RotationallySymmetricalGraspingObject, self).transform_to_mln_database(mln)
        database.add_true_ground_atom(gab.get_is_rotationally_symmetric(self.type))

        return database

