from ..model.geometry import Point3


class Joint:
    def __init__(self,name=None,translation=None,orientation=None,parent_name= None):
        self.name = name
        self.translation = translation if translation else Point3()
        self.orientation = orientation if orientation else Point3()
        self.parent_name = parent_name