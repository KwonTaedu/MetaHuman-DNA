print("1")
#from dna import BinaryStreamReader
print("2")
from ..model.behavior import AnimatedMapsData
from ..model.behavior import Behavior as BehaviorModel
from ..model.behavior import BlendShapesData, ConditionalTable, JointGroup, PSDMatrix

print("HI")
class Behavior:
    def __init__(self,stream_reader):
        self.reader = stream_reader
        self.behavior = None

    def read(self):

        self.behavior = BehaviorModel()
        self.add_gui_to_raw()
        self.add_psd()
        self.add_joints()
        self.add_blend_shapes()
        self.add_animated_maps()
        return self.behavior

    def add_gui_to_raw(self):
        
        self.behavior.gui_to_raw = ConditionalTable(
            inputs=self.reader.getGUIToRawInputIndices(),
            outputs=self.reader.getGUIToRawOutputIndices(),
            from_values=self.reader.getGUIToRawFromValues(),
            to_values=self.reader.getGUIToRawToValues(),
            slope_values=self.reader.getGUIToRawSlopeValues(),
            cut_values=self.reader.getGUIToRawCutValues(),
        )

    def add_psd(self):
        self.behavior.psd = PSDMatrix(
            count=self.reader.getPSDCount(),
            rows=self.reader.getPSDRowIndices(),
            columns=self.reader.getPSDColumnIndices(),
            values=self.reader.getPSDValues(),
        )

    def add_joints(self):

        self.behavior.joints.joint_row_count = self.reader.getJointRowCount()
        self.behavior.joints.joint_column_count = self.reader.getJointColumnCount()
        for lod in range(self.reader.getLODCount()):
            self.behavior.joints.joint_variable_attribute_indices.append(
                self.reader.getJointVariableAttributeIndices(lod)
            )
        for joint_group_index in range(self.reader.getJointGroupCount()):
            self.behavior.joints.joint_groups.append(
                JointGroup(
                    lods=self.reader.getJointGroupLODs(joint_group_index),
                    inputs=self.reader.getJointGroupInputIndices(joint_group_index),
                    outputs=self.reader.getJointGroupOutputIndices(joint_group_index),
                    values=self.reader.getJointGroupValues(joint_group_index),
                    joints=self.reader.getJointGroupJointIndices(joint_group_index),
                )
            )

    def add_blend_shapes(self):
        self.behavior.blend_shapes = BlendShapesData(
            lods=self.reader.getBlendShapeChannelLODs(),
            inputs=self.reader.getBlendShapeChannelInputIndices(),
            outputs=self.reader.getBlendShapeChannelOutputIndices(),
        )

    def add_animated_maps(self):
        self.behavior.animated_maps = AnimatedMapsData(
            lods=self.reader.getAnimatedMapLODs(),
            conditional_table=ConditionalTable(
                from_values=self.reader.getAnimatedMapFromValues(),
                to_values=self.reader.getAnimatedMapToValues(),
                slope_values=self.reader.getAnimatedMapSlopeValues(),
                cut_values=self.reader.getAnimatedMapCutValues(),
                inputs=self.reader.getAnimatedMapInputIndices(),
                outputs=self.reader.getAnimatedMapOutputIndices(),
            ),
        )
