from grasping_type_inference.face import Face
from high_level_markov_logic_network.ground_atom import GroundAtom

__FACING_ROBOT_FACE__ = 'facing_robot_face'
__BOTTOM_FACE__ = 'bottom_face'
__OBJ_TO_BE_GRASPED__ = 'obj_to_be_grasped'
__IS_ROTATIONALLY_SYMMETRIC__ = 'is_rotationally_symmetric'
__GRASP_TYPE__ = 'grasp_type'


def get_facing_robot_face(arg):
    ground_atom_value = arg

    if type(arg) is Face:
        ground_atom_value = arg.value

    return GroundAtom(__FACING_ROBOT_FACE__, [ground_atom_value])


def get_bottom_face(arg):
    ground_atom_value = arg

    if type(arg) is Face:
        ground_atom_value = arg.value

    return GroundAtom(__BOTTOM_FACE__, [ground_atom_value])


def get_obj_to_be_grasped(arg):
    return GroundAtom(__OBJ_TO_BE_GRASPED__, [arg])


def get_is_rotationally_symmetric(arg):
    return GroundAtom(__IS_ROTATIONALLY_SYMMETRIC__, [arg])


def get_grasp_type(arg):
    return GroundAtom(__GRASP_TYPE__, [arg])