from pracmln.mlnquery import MLNQuery
from pracmln.utils.project import MLNProject
from pracmln.mln.base import parse_mln


class MarkovLogicNetwork:
    def __init__(self, path_to_pracmln_project):
        self.pracmln_project = MLNProject.open(path_to_pracmln_project)
        self.__config__ = self.pracmln_project.queryconf
        self.__logic__ = self.__config__.config['logic']
        self.__grammar__ = self.__config__.config['grammar']
        self.__mln_name__ = self.__config__.config['mln']
        self.pracmln = self.__parse_mln_from_text__()
        self.domains = self.pracmln.domains

    def __parse_mln_from_text__(self):
        mln_text = self.pracmln_project.mlns.get(self.__mln_name__)
        return parse_mln(mln_text, logic=self.__logic__, grammar=self.__grammar__)

    def infer(self, database):
        mln_query = MLNQuery(self.__config__,
                             mln=self.pracmln,
                             db=database.pracmln_database,
                             verbose=0)

        return mln_query.run()