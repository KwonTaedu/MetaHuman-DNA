

class ConditionalTable:
    def __init__(self,from_values=None,to_values=None,slope_values=None,cut_values= None,inputs=None,outputs=None):
        self.from_values = from_values if from_values else []
        self.to_values = to_values if to_values else []
        self.slope_values = slope_values if slope_values else []
        self.cut_values = cut_values if cut_values else []
        self.inputs = inputs if inputs else []
        self.outputs = outputs if outputs else []
    

class PSDMatrix:
    def __init__(self,count=None,rows=None,columns=None,values=None):
        self.count = count 
        self.rows = rows if rows else []
        self.columns = columns if columns else []
        self.values = values if values else []

class JointGroup:
    def __init__(self,lods=None,values=None,joints=None,inputs=None,outputs=None):
        self.lods = lods if lods else []
        self.values = values if values else []
        self.joints = joints if joints else []
        self.inputs = inputs if inputs else []
        self.outputs = outputs if outputs else []

class BlendShapesData:
    def __init__(self,lods=None,inputs=None,outputs=None):
        self.lods = lods if lods else []
        self.inputs = inputs if inputs else []
        self.outputs = outputs if outputs else []


class AnimatedMapsData:
    def __init__(self,lods=None,conditional_table = None):
        self.lods = lods if lods else []
        self.conditional_table = conditional_table if conditional_table else ConditionalTable()

class JointsData:
    def __init__(self,joint_row_count=None,joint_column_count=None,joint_variable_attribute_indices=None,joint_groups=None):
        self.joint_row_count = joint_row_count
        self.joint_column_count = joint_column_count
        self.joint_variable_attribute_indices = joint_variable_attribute_indices if joint_variable_attribute_indices else []
        self.joint_groups = joint_groups if joint_groups else []

class Behavior:
    def __init__(self,gui_to_raw=None,psd=None,blend_shapes=None,animated_maps=None,joints=None):
        self.gui_to_raw = gui_to_raw if gui_to_raw else ConditionalTable()
        self.psd = psd if psd else PSDMatrix()
        self.blend_shapes = blend_shapes if blend_shapes else BlendShapesData()
        self.animated_maps = animated_maps if animated_maps else AnimatedMapsData()
        self.joints = joints if joints else JointsData()
