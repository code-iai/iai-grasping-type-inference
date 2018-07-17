from prac.core.base import PRACModule, PRACPIPE, PRACDatabase
from prac.core.inference import PRACInferenceStep, FrameNode
from prac.pracutils.utils import prac_heading
from pracmln import Database
from pracmln.mln.base import parse_mln
from pracmln.mln.util import colorize
from pracmln.utils.project import MLNProject



class GraspingTypeInferer(PRACModule):
    def __init__(self, prac):
        self.grasping_type_pracmln_project = None
        self.grasping_type_mln = None

        super(GraspingTypeInferer, self).__init__(prac)

        self.__init_instance_variables__()

    def __init_instance_variables__(self):
        self.grasping_type_pracmln_project = MLNProject.open('mln/grasping_type.pracmln')
        self.__read_grasping_type_mln__()

    def __read_grasping_type_mln__(self):
        mln_text = self.grasping_type_pracmln_project.mlns.get('grasping_type.mln')
        self.grasping_type_mln = parse_mln(mln_text, logic='FuzzyLogic', grammar='PRACGrammar')



    #def __call__(self, node, **params):



