from prac.core.base import PRACModule, PRACPIPE, PRACDatabase
from prac.core.inference import PRACInferenceStep, FrameNode
from prac.pracutils.utils import prac_heading
from pracmln import Database
from pracmln.mln.base import parse_mln
from pracmln.mln.util import colorize
from pracmln.utils.project import MLNProject



class GraspingTypeInferer(PRACModule):
    def __init__(self, prac):
        super(GraspingTypeInferer, self).__init__(prac)

        self.__init_instance_variables__()

    #def __call__(self, node, **params):




