from ..model.geometry import Point3

class Joint:
    def __init__(self,name=None,translation=Point3(),orientation=Point3(),parent_name= None):
        self.name = name
        self.translation = translation
        self.orientation = orientation
        self.parent_name = parent_name
