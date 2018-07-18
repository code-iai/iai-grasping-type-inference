from grasping_object import GraspingObject


class RotationallySymmetricalGraspingObject(GraspingObject):
    def __init__(self, object_type, orientation):
        super(RotationallySymmetricalGraspingObject, self).__init__(object_type, orientation)

    def transform_to_mln_database(self, mln):
        database = super(RotationallySymmetricalGraspingObject, self).transform_to_mln_database(mln)
        database.add_ground_atom('is_rotationally_symmetric({})'.format(self.type))

        return database
