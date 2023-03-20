class ConditionalTable:
    def __init__(self,from_values=[],to_values=[],slope_values=[],cut_values= [],inputs=[],outputs=[]):
        self.from_values = from_values
        self.to_values = to_values
        self.slope_values = slope_values
        self.cut_values = cut_values
        self.inputs = inputs
        self.outputs = outputs

class PSDMatrix:
    def __init__(self,count=None,rows=[],columns=[],values=[]):
        self.count = count
        self.rows = rows
        self.columns = columns
        self.values = values

class JointGroup:
    def __init__(self,lods=[],values=[],joints=[],inputs=[],outputs=[]):
        self.lods = lods
        self.values = values
        self.joints = joints
        self.inputs = inputs
        self.outputs = outputs

class BlendShapesData:
    def __init__(self,lods=[],inputs=[],outputs=[]):
        self.lods = lods
        self.inputs = inputs
        self.outputs = outputs


class AnimatedMapsData:
    def __init__(self,lods=[],conditional_table = ConditionalTable()):
        self.lods = lods
        self.conditional_table = conditional_table

class JointsData:
    def __init__(self,joint_row_count=None,joint_column_count=None,joint_variable_attribute_indices=[],joint_groups=[]):
        self.joint_row_count = joint_row_count
        self.joint_column_count = joint_column_count
        self.joint_variable_attribute_indices = joint_variable_attribute_indices
        self.joint_groups = joint_groups

class Behavior:
    def __init__(self,gui_to_raw=ConditionalTable(),psd=PSDMatrix(),blend_shapes=BlendShapesData(),animated_maps=AnimatedMapsData(),joints=JointsData()):
        self.gui_to_raw = gui_to_raw
        self.psd = psd
        self.blend_shapes = blend_shapes
        self.animated_maps = animated_maps
        self.joints = joints
