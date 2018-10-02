from pracmln.utils.project import MLNProject
from pracmln.mln.base import parse_mln
import os
from definitions import ROOT_DIR

grasping_type_pracmln_project = None


def __read_grasping_type_mln_project__():
    path_to_grasping_type_mln = os.path.join(ROOT_DIR, 'mln', 'grasping_type.pracmln')
    return MLNProject.open(path_to_grasping_type_mln)


def __read_grasping_type_mln__():
    global grasping_type_pracmln_project

    mln_text = grasping_type_pracmln_project.mlns.get('grasping_type.mln')

    return parse_mln(mln_text, logic='FuzzyLogic', grammar='PRACGrammar')


grasping_type_pracmln_project = __read_grasping_type_mln_project__()
grasping_type_mln = __read_grasping_type_mln__()





