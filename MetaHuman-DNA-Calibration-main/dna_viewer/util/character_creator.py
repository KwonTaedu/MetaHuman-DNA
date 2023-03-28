import logging

from maya import cmds
from maya.api.OpenMaya import MObject

from ..builder.analog_gui import AnalogGui
from ..builder.gui import Gui
from ..builder.joint import Joint as JointBuilder
from ..builder.mesh import Mesh
from ..config.character import Character
from ..const.naming import (
    ANALOG_GUI_HOLDER,
    FACIAL_ROOT_JOINT,
    FRM_MULTIPLIERS_NAME,
    GEOMETRY_HOLDER_PREFIX,
    GUI_HOLDER,
    LOD_HOLDER_PREFIX,
    LOD_HOLDER_PREFIX_UPPER,
    RIG_HOLDER_PREFIX,
)
from ..model.dna import DNA
from ..model.joint import Joint as JointModel 
from ..util.additional_assembly_script import AdditionalAssemblyScript ###
from ..util.maya_util import Maya
from ..util.rig_logic import RigLogic 
from ..util.shader import Shader as ShaderUtil


class CharacterCreator:
    def __init__(self, config, dna):
        self.config = config
        self.dna = dna
        self.character_name = self.dna.get_character_name()
        self.meshes = {}

    def add_mesh_to_display_layer(self, mesh_name, lod):
        cmds.editDisplayLayerMembers((LOD_HOLDER_PREFIX_UPPER+lod), mesh_name)

    def add_joints(self):
        joints = self.dna.read_all_neutral_joints()
        builder = JointBuilder(
            joints,
            self.config.modifiers.linear_modifier,
            self.config.modifiers.angle_modifier,
        )
        builder.process()
        return joints

    def add_joints_to_character(self):

        if self.config.options.add_joints:
            logging.info("adding joints to character...")
            joints = self.add_joints()

            if self.config.create_character_node:
                cmds.parent(joints[0].name, self.character_name)

    def create_character_node(self):

        if self.config.create_character_node:
            logging.info("building character node...")
            if not cmds.objExists(self.character_name):
                cmds.createNode("transform", n=self.character_name)

    def create_geometry_node(self):

        if self.config.create_character_node:
            logging.info("adding geometry node")
            name = GEOMETRY_HOLDER_PREFIX+self.character_name
            if not cmds.objExists(name):
                cmds.createNode("transform", n=name)
                cmds.parent(name, self.character_name)

    def create_rig_node(self):
        if self.config.create_character_node:
            logging.info("adding rig node")
            char_name = RIG_HOLDER_PREFIX+self.character_name
            if not cmds.objExists(char_name):
                cmds.createNode("transform", n=char_name)
                cmds.parent(char_name, self.character_name)

    def create_lod_node(self, lod, obj_name):

        if not cmds.objExists(obj_name):
            parent_name = GEOMETRY_HOLDER_PREFIX+self.character_name
            name = LOD_HOLDER_PREFIX+lod
            cmds.createNode("transform", n=name, p=parent_name)

    def attach_mesh_to_lod(self, mesh_name, lod):

        parent_node = (
            GEOMETRY_HOLDER_PREFIX+self.character_name+"|"+LOD_HOLDER_PREFIX+lod
        )
        cmds.parent(
            self.get_mesh_node_fullpath_on_root(mesh_name=mesh_name), parent_node
        )

    def get_mesh_node_fullpath_on_root(self, mesh_name):
        return str(Maya.get_element("|"+mesh_name).fullPathName())

    def create_ctrl_attributes(self):

        gui_control_names = self.dna.get_raw_control_names()

        for name in gui_control_names:
            ctrl_and_attr_names = name.split(".")
            cmds.addAttr(
                ctrl_and_attr_names[0],
                longName=ctrl_and_attr_names[1],
                keyable=True,
                attributeType="float",
                minValue=0.0,
                maxValue=1.0,
            )

    def create_frm_attributes(self):

        frm_names = self.dna.get_animated_map_names()
        for name in frm_names:
            cmds.addAttr(
                FRM_MULTIPLIERS_NAME,
                longName=name.replace(".", "_"),
                keyable=True,
                attributeType="float",
                minValue=0.0,
                maxValue=1.0,
            )

    def create_ctrl_attributes_on_joint(self):

        if (
            self.config.options.add_ctrl_attributes_on_root_joint
            and self.config.options.add_joints
        ):
            logging.info("adding ctrl attributes on root joint...")
            names = self.dna.get_raw_control_names()
            self.create_attribute_on_joint(names=names)

    def create_animated_map_attributes(self):
        if (
            self.config.options.add_animated_map_attributes_on_root_joint
            and self.config.options.add_joints
        ):
            logging.info("adding animated map attributes on root joint...")
            names = self.dna.get_animated_map_names()
            self.create_attribute_on_joint(names=names)

    def create_attribute_on_joint(self, names):

        for name in names:
            cmds.addAttr(
                FACIAL_ROOT_JOINT,
                longName=name.replace(".", "_"),
                keyable=True,
                attributeType="float",
                minValue=0.0,
                maxValue=1.0,
            )

    def add_key_frames(self):

        if self.config.options.add_key_frames and self.config.options.add_joints:
            logging.info("setting keyframe on the root joint...")
            cmds.currentTime(0)
            cmds.select(FACIAL_ROOT_JOINT, replace=True)
            cmds.setKeyframe(inTangentType="linear", outTangentType="linear")

    def create_character_meshes(self):

        logging.info("building character meshes...")
        meshes = {}
        for lod, meshes_per_lod in enumerate(
            self.dna.get_meshes_by_lods(self.config.meshes)
        ):
            if self.config.create_character_node and meshes_per_lod:
                logging.info("building LOD for "+lod)
                obj_name = GEOMETRY_HOLDER_PREFIX+self.character_name+"|"+LOD_HOLDER_PREFIX+lod
                self.create_lod_node(lod=lod, obj_name=obj_name)

            meshes[lod] = self.create_meshes(
                lod=lod,
                meshes_per_lod=meshes_per_lod,
            )
        self.meshes = meshes

    def create_meshes(self, lod, meshes_per_lod):

        meshes= []
        for mesh_index in meshes_per_lod:
            builder = Mesh(
                character_config=self.config,
                dna=self.dna,
                mesh_index=mesh_index,
            )
            builder.build()

            mesh_name = self.dna.get_mesh_name(mesh_index=mesh_index)
            meshes.append(mesh_name)

            if self.config.create_display_layers:
                self.add_mesh_to_display_layer(mesh_name, lod)
            if self.config.create_character_node:
                self.attach_mesh_to_lod(mesh_name, lod)
            ShaderUtil.default_lambert_shader(
                mesh_name, self.character_name, self.config.create_character_node
            )
        return meshes

    def add_gui(self):

        if self.config.gui_options:
            logging.info("adding gui...")
            builder = Gui(self.config.gui_options)
            self.import_gui(
                gui_path=self.config.gui_options.gui_path, group_name=GUI_HOLDER
            )
            builder.build()
            self.create_ctrl_attributes()
            self.create_frm_attributes()

    def add_analog_gui(self,add_to_character_node = False):

        if self.config.analog_gui_options and self.config.options.add_joints:
            logging.info("adding analog gui...")
            builder = AnalogGui(self.config.analog_gui_options)
            self.import_gui(
                gui_path=self.config.analog_gui_options.gui_path,
                group_name=ANALOG_GUI_HOLDER,
                add_to_character_node=add_to_character_node,
            )
            builder.build()

    def import_gui(self, gui_path, group_name, add_to_character_node = False):

        cmds.file(gui_path, i=True, groupReference=True, groupName=group_name)

        if add_to_character_node:
            cmds.parent(group_name, RIG_HOLDER_PREFIX+self.character_name)

    def add_rig_logic_node(self):
        RigLogic.add_rig_logic(config=self.config, character_name=self.character_name)
        
    def run_additional_assembly_script(self):

        AdditionalAssemblyScript.run_additional_assembly_script(config=self.config)
