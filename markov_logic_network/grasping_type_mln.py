from pracmln.utils.project import MLNProject
from pracmln.mln.base import parse_mln

__grasping_type_mln__ = None


def __read_grasping_type_mln__():
    global __grasping_type_mln__

    grasping_type_pracmln_project = MLNProject.open('../mln/grasping_type.pracmln')
    mln_text = grasping_type_pracmln_project.mlns.get('grasping_type.mln')
    __grasping_type_mln__ = parse_mln(mln_text, logic='FuzzyLogic', grammar='PRACGrammar')


def get_mln():
    if __grasping_type_mln__ is None:
        __read_grasping_type_mln__()
    return __grasping_type_mln__
