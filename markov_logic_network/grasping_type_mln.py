from pracmln.utils.project import MLNProject
from pracmln.mln.base import parse_mln
import os
from definitions import ROOT_DIR


def __read_grasping_type_mln__():
    path_to_grasping_type_mln = os.path.join(ROOT_DIR, 'mln', 'grasping_type.pracmln')
    grasping_type_pracmln_project = MLNProject.open(path_to_grasping_type_mln)
    mln_text = grasping_type_pracmln_project.mlns.get('grasping_type.mln')

    return parse_mln(mln_text, logic='FuzzyLogic', grammar='PRACGrammar')


grasping_type_mln = __read_grasping_type_mln__()


