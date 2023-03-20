from ..const.naming import BLEND_SHAPE_NAME_POSTFIX, FRM_MULTIPLIERS_NAME

class RigLogic:
    def __init__(self,command = "createEmbeddedNodeRL4",name = "",dna_file_path="",control_naming="<objName>.<attrName>",
                 blend_shape_naming = "<objName>" + BLEND_SHAPE_NAME_POSTFIX + ".<attrName>",
                 animated_map_naming = FRM_MULTIPLIERS_NAME + ".<objName>_<attrName>"
                 ):
        self.command = command
        self.name = name
        self.dna_file_path = dna_file_path
        self.control_naming = control_naming
        self.blend_shape_naming = blend_shape_naming
        self.animated_map_naming = animated_map_naming
        

    def with_name(self, name):
        # type : (str) -> None
        self.name = name

        return self

    def with_dna_file_path(self, dna_file_path):
        # type : (str) -> None
        self.dna_file_path = dna_file_path

        return self

    def with_control_naming(self, control_naming):
        # type : (str) -> None
        self.control_naming = control_naming
        return self

    def with_joint_naming(self, joint_naming):
        # type : (str) -> None

        self.joint_naming = joint_naming
        return self

    def with_blend_shape_naming(self, blend_shape_naming):
        # type : (str) -> None

        self.blend_shape_naming = blend_shape_naming
        return self

    def with_animated_map_naming(self, animated_map_naming):
        # type : (str) -> None

        self.animated_map_naming = animated_map_naming
        return self
