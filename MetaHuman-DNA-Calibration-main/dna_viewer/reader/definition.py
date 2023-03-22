print("reade.definition")
#from dna import BinaryStreamReader

from ..model.definition import Definition as DefinitionModel
from ..model.geometry import Point3


class Definition:

    def __init__(self, stream_reader):
        self.reader = stream_reader
        self.definition = None

    def read(self):
        self.definition = DefinitionModel()

        self.add_controls()
        self.add_joints()
        self.add_blend_shape_channels()
        self.add_animated_maps()
        self.add_meshes()
        self.add_mesh_blend_shape_channel_mapping()
        self.add_neutral_joints()

        return self.definition

    def add_neutral_joints(self):
        neutral_joint_translation_xs = self.reader.getNeutralJointTranslationXs()
        neutral_joint_translation_ys = self.reader.getNeutralJointTranslationYs()
        neutral_joint_translation_zs = self.reader.getNeutralJointTranslationZs()
        neutral_joint_translation_count_x = len(neutral_joint_translation_xs)
        for index in range(neutral_joint_translation_count_x):
            self.definition.neutral_joint_translations.append(
                Point3(
                    x=neutral_joint_translation_xs[index],
                    y=neutral_joint_translation_ys[index],
                    z=neutral_joint_translation_zs[index],
                )
            )
        neutral_joint_rotation_xs = self.reader.getNeutralJointRotationXs()
        neutral_joint_rotation_ys = self.reader.getNeutralJointRotationYs()
        neutral_joint_rotation_zs = self.reader.getNeutralJointRotationZs()
        neutral_joint_rotation_count_x = len(neutral_joint_rotation_xs)
        for index in range(neutral_joint_rotation_count_x):
            self.definition.neutral_joint_rotations.append(
                Point3(
                    x=neutral_joint_rotation_xs[index],
                    y=neutral_joint_rotation_ys[index],
                    z=neutral_joint_rotation_zs[index],
                )
            )

    def add_mesh_blend_shape_channel_mapping(self):
        for index in range(self.reader.getMeshBlendShapeChannelMappingCount()):
            mapping = self.reader.getMeshBlendShapeChannelMapping(index)
            self.definition.mesh_blend_shape_channel_mapping.append(
                (mapping.meshIndex, mapping.blendShapeChannelIndex)
            )
        for lod in range(self.reader.getLODCount()):
            self.definition.mesh_blend_shape_channel_mapping_indices_for_lod.append(
                self.reader.getMeshBlendShapeChannelMappingIndicesForLOD(lod)
            )

    def add_meshes(self):
        for index in range(self.reader.getMeshCount()):
            self.definition.meshes.names.append(self.reader.getMeshName(index))
        for index in range(self.reader.getLODCount()):
            self.definition.meshes.indices_for_lod.append(
                self.reader.getMeshIndicesForLOD(index)
            )

    def add_animated_maps(self):
        for index in range(self.reader.getAnimatedMapCount()):
            self.definition.animated_maps.names.append(
                self.reader.getAnimatedMapName(index)
            )
        for index in range(self.reader.getLODCount()):
            self.definition.animated_maps.indices_for_lod.append(
                self.reader.getAnimatedMapIndicesForLOD(index)
            )

    def add_blend_shape_channels(self):
        for index in range(self.reader.getBlendShapeChannelCount()):
            self.definition.blend_shape_channels.names.append(
                self.reader.getBlendShapeChannelName(index)
            )
        for index in range(self.reader.getLODCount()):
            self.definition.blend_shape_channels.indices_for_lod.append(
                self.reader.getBlendShapeChannelIndicesForLOD(index)
            )

    def add_joints(self):
        for index in range(self.reader.getJointCount()):
            self.definition.joints.names.append(self.reader.getJointName(index))
            self.definition.joints.parent_index.append(
                self.reader.getJointParentIndex(index)
            )
        for index in range(self.reader.getLODCount()):
            self.definition.joints.indices_for_lod.append(
                self.reader.getJointIndicesForLOD(index)
            )

    def add_controls(self):
        for index in range(self.reader.getGUIControlCount()):
            self.definition.gui_control_names.append(
                self.reader.getGUIControlName(index)
            )
        for index in range(self.reader.getRawControlCount()):
            self.definition.raw_control_names.append(
                self.reader.getRawControlName(index)
            )
