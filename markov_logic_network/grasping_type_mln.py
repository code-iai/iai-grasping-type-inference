import os
from definitions import ROOT_DIR
from markov_logic_network.mln import MarkovLogicNetwork


def __get_grasping_type_mln__():
    path_to_grasping_type_mln = os.path.join(ROOT_DIR, 'mln', 'grasping_type.pracmln')

    return MarkovLogicNetwork(path_to_grasping_type_mln)


grasping_type_mln = __get_grasping_type_mln__()





