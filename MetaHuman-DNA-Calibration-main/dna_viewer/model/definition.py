from ..model.geometry import Point3

class NamesAndIndices:
    def __init__(self,names=[],indices_for_lod={}):
        self.names = names
        self.indices_for_lod = indices_for_lod


class Joints(NamesAndIndices):
    def __init__(self,parent_index=[]):
        self.parent_index = parent_index

# @dataclass
# class Joints(NamesAndIndices):

#     parent_index: List[int] = field(default_factory=list)

class Definition:
    def __init__(self,joints = Joints(), blend_shape_channels = NamesAndIndices(),animated_maps = NamesAndIndices(),meshes = NamesAndIndices(),gui_control_names = [],raw_control_names= [],
                 mesh_blend_shape_channel_mapping = [], mesh_blend_shape_channel_mapping_indices_for_lod = [],neutral_joint_translations = [],neutral_joint_rotations = []):
        self.joints = joints
        self.blend_shape_channels = blend_shape_channels
        self.animated_maps = animated_maps
        self.meshes = meshes
        self.gui_control_names = gui_control_names
        self.raw_control_names = raw_control_names
        self.mesh_blend_shape_channel_mapping = mesh_blend_shape_channel_mapping
        self.mesh_blend_shape_channel_mapping_indices_for_lod = mesh_blend_shape_channel_mapping_indices_for_lod
        self.neutral_joint_translations = neutral_joint_translations
        self.neutral_joint_rotations = neutral_joint_rotations
