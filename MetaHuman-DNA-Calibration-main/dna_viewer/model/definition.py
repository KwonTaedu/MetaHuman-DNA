from ..model.geometry import Point3

class NamesAndIndices(object):
    def __init__(self,names = None, indices_for_lod = None):
        self.names = names if names else []
        self.indices_for_lod = indices_for_lod if indices_for_lod else []


class Joints(NamesAndIndices):
    def __init__(self,parent_index = None):
        super(Joints,self).__init__()
        self.parent_index = parent_index if parent_index else []

class Definition:
    def __init__(self,joints = None, 
                 blend_shape_channels = None ,
                 animated_maps = None, 
                 meshes = None,
                 gui_control_names = None,
                 raw_control_names= None,
                 mesh_blend_shape_channel_mapping = None, 
                 mesh_blend_shape_channel_mapping_indices_for_lod = None
                 ,neutral_joint_translations = None,
                 neutral_joint_rotations = None
        ):
        
        self.joints = joints if joints else Joints()
        self.blend_shape_channels = blend_shape_channels if blend_shape_channels else NamesAndIndices()
        self.animated_maps = animated_maps if animated_maps else NamesAndIndices()
        self.meshes = meshes if meshes else NamesAndIndices()
        self.gui_control_names = gui_control_names if gui_control_names else []
        self.raw_control_names = raw_control_names if raw_control_names else []
        self.mesh_blend_shape_channel_mapping = mesh_blend_shape_channel_mapping if mesh_blend_shape_channel_mapping else []
        self.mesh_blend_shape_channel_mapping_indices_for_lod = mesh_blend_shape_channel_mapping_indices_for_lod if mesh_blend_shape_channel_mapping_indices_for_lod else []
        self.neutral_joint_translations = neutral_joint_translations if neutral_joint_translations else []
        self.neutral_joint_rotations = neutral_joint_rotations if neutral_joint_rotations else []