from grasping_object.grasping_object import GraspingObject
from grasping_object.orientation import Orientation


if __name__ == "__main__":
    orientation = Orientation('front', 'bottom')
    grasping_object = GraspingObject('tankard.n.01', orientation)

    result = grasping_object.get_most_probable_grasping_type()

    for ground_atom in result.results.keys():
        if result.results[ground_atom] == 1:
            print ground_atom
