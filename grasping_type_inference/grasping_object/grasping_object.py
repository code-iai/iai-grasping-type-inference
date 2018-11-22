# Copyright © 2018 Institute for Artificial Intelligence - University of Bremen
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of
# the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from high_level_markov_logic_network.database import Database
from high_level_markov_logic_network.fuzzy_markov_logic_network.is_a_generator import get_is_a_ground_atoms
import grasping_type_inference.ground_atom_builder as gab
from grasping_type_inference.grasping_type_mln import grasping_type_mln


class GraspingObject(object):
    def __init__(self, object_type, orientation):
        self.type = object_type
        self.orientation = orientation

    def get_most_probable_grasping_type(self):
        learned_objects = grasping_type_mln.domains['learnedObject']

        evidence_database = self.transform_to_mln_database(grasping_type_mln)
        is_a_ground_atoms = get_is_a_ground_atoms(self.type, learned_objects)

        for ground_atom in is_a_ground_atoms:
            evidence_database.add_ground_atom(ground_atom)

        return grasping_type_mln.infer(evidence_database)

    def transform_to_mln_database(self, mln):
        database = Database(mln)

        database.add_ground_atom(gab.get_obj_to_be_grasped(self.type))
        database.add_ground_atom(self.orientation.transform_facing_robot_face_to_ground_atom())
        database.add_ground_atom(self.orientation.transform_bottom_face_to_ground_atom())

        return database

    def __eq__(self, other):
        if (self.type != other.type) or (self.orientation != other.orientation):
            return False
        else:
            return True
