from grasping_object.orientation import Orientation
from grasping_object.grasping_object import GraspingObject
from grasping_object.rotationally_symmetrical_grasping_object import RotationallySymmetricalGraspingObject
from markov_logic_network.database import Database

from face import Face

GRASPING_OBJECT_TYPE = 'cup.n.01'
FACING_ROBOT_FACE = Face.FRONT
BOTTOM_FACE = Face.BOTTOM
GRASP_TYPE = 'topGrasp'


def get_rotationally_symmetrical_grasping_object():
    orientation = get_orientation_object()
    return RotationallySymmetricalGraspingObject(GRASPING_OBJECT_TYPE, orientation)


def get_grasping_object():
    orientation = get_grasping_object()
    return GraspingObject(GRASPING_OBJECT_TYPE, orientation)


def get_orientation_object():
    return Orientation(FACING_ROBOT_FACE, BOTTOM_FACE)


def get_grasping_object_as_mln_database(mln, ground_atoms):
    database = Database(mln)
    map(database.add_ground_atom, ground_atoms)

    return database
