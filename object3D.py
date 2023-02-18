"""Classe of 3D objects"""
###########################
#EXIT CODES : 
#1 : Arguemnt error with the arg "id_"
#
###########################

class Object3D(object):
    def __init__(self, points, color, id_='DO NOT TOUCH IT !'):
        """It is a class for create other 3D objects.
        Arguments : 
        - points : list of tuples with 3 coord.
        - id : the id is attributed by the Screen class. DO NOT TOUCH, exceept you know what you are doing !"""
        self.list_points = points
        self.list_edge = []
        self.color = color
        if id_ == "DO NOT TOUCH IT !":
            raise AttributeError("Sorry, but you must give this argument (id_). For it, you have to use Screen.get_id(), it gener id.")
            exit(1)
        self.id_ = id_

    def get(self, what="ALL"):
        """Return the coords of the points.
        Arguments :
        - what : which point return (a number or "ALL", "ALL" is default.)
        """
        if what == "ALL":
            return self.list_points
        else:
            return self.list_points[what]

    def give_top(self, oy, oz):
        """Give the order of priority of the points."""
        pass

    def create_edge(self, points):
        """Create a new edge.
        Arguments :
        - points : a list with 2 points."""

    def create_face(self, points, skin=("color", "blue")):
        """Create a new face.
        Arguments : 
        - points : a list of points
        - a tuple with the type of the skin of the face, and the skin. Default : type:color and skin:blue."""

class Cube(Object3D):
    def __init__(self, points, color, id_='DO NOT TOUCH IT !'):
        """This class from Object3d allow to create a cube."""
        super(Object3D, self).__init__(points, color, id_)
        #Check if there are 8 points.
        if not(len(points) == 8):
            raise AttributeError("A cube must have 8 points ! For create an other object, use Object3d !")
        