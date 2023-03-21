from ..model.geometry import UV, Layout, Point3


class FaceVertex:
    def __init__(self,position=None,texture_coordinate =None ,normal = None,layout = None,skin_weight_values =[],skin_weight_joint_indices=[]):
        self.position = position
        self.texture_coordinate = texture_coordinate
        self.normal = normal
        self.layout = layout
        self.skin_weight_values = skin_weight_values
        self.skin_weight_joint_indices = skin_weight_joint_indices

