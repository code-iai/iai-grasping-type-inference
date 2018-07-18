from face import Face

__FACING_ROBOT_FACE__ = 'facing_robot_face'
__BOTTOM_FACE__ = 'bottom_face'
__OBJ_TO_BE_GRASPED__ = 'obj_to_be_grasped'
__IS_ROTATIONALLY_SYMMETRIC__ = 'is_rotationally_symmetric'
__IS_A__ = 'is_a'
__GRASP_TYPE__ = 'grasp_type'


def get_facing_robot_face(arg):
    ground_atom_value = arg

    if type(arg) is Face:
        ground_atom_value = arg.value

    return __get_ground_atom_with_one_arg__(__FACING_ROBOT_FACE__, ground_atom_value)


def get_bottom_face(arg):
    ground_atom_value = arg

    if type(arg) is Face:
        ground_atom_value = arg.value

    return __get_ground_atom_with_one_arg__(__BOTTOM_FACE__, ground_atom_value)


def get_obj_to_be_grasped(arg):
    return __get_ground_atom_with_one_arg__(__OBJ_TO_BE_GRASPED__, arg)


def get_is_rotationally_symmetric(arg):
    return __get_ground_atom_with_one_arg__(__IS_ROTATIONALLY_SYMMETRIC__, arg)


def get_grasp_type(arg):
    return __get_ground_atom_with_one_arg__(__GRASP_TYPE__, arg)


def __get_ground_atom_with_one_arg__(ground_atom_name, arg):
    parameter = '({})'.format(arg)
    return ground_atom_name + parameter
