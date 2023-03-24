# -*- coding: utf-8 -*-

import os

from ..config.aas import AdditionalAssemblyScript
from ..config.analog_gui import AnalogGui
from ..config.gui import Gui
from ..config.rig_logic import RigLogic
from ..model.dna import DNA

class SpaceModifiers():
    def __init__(self,linear_modifier=None, angle_modifier=None):
        self.linear_modifier = linear_modifier
        self.angle_modifier = angle_modifier


class BuildOptions():
    def __init__(self, add_joints=False, add_normals=False, add_blend_shapes=False, add_skin=False,
                 add_ctrl_attributes_on_root_joint=False, add_animated_map_attributes_on_root_joint=False,
                 add_key_frames=False, add_mesh_name_to_blend_shape_channel_name=False):
        self.add_joints = add_joints
        self.add_normals = add_normals
        self.add_blend_shapes = add_blend_shapes
        self.add_skin = add_skin
        self.add_ctrl_attributes_on_root_joint = add_ctrl_attributes_on_root_joint
        self.add_animated_map_attributes_on_root_joint = add_animated_map_attributes_on_root_joint
        self.add_key_frames = add_key_frames
        self.add_mesh_name_to_blend_shape_channel_name = add_mesh_name_to_blend_shape_channel_name

class Character():
    def __init__(self, dna=None, options=None, modifiers=None, meshes=None, rig_logic_config=None,
                 gui_options=None, analog_gui_options=None, create_character_node=True, create_display_layers=True,
                 aas=None):
         
        self.dna = dna 
        self.options = options if options else BuildOptions()
        self.modifiers = modifiers if modifiers else SpaceModifiers()
        self.meshes = meshes if meshes else []
        self.rig_logic_config = rig_logic_config 
        self.gui_options = gui_options 
        self.analog_gui_options = analog_gui_options 
        self.create_character_node = create_character_node 
        self.create_display_layers = create_display_layers
        self.aas = aas
    
    def with_dna(self,dna):
        self.dna = dna
        return self
    
    def with_character_node(self, value):
        self.create_character_node = value
        return self
    
    def with_add_meshes_to_display_layers(self, value):
        self.create_display_layers = value
        return self

    def with_joints(self):
        self.options.add_joints = True
        return self

    def with_gui_path(self, gui_path):
        self.gui_options = Gui(gui_path=gui_path)
        return self
    #
    def with_gui(self, gui):
        self.gui_options = gui
        return self

    def with_analog_gui(self, analog_gui_config):
        self.analog_gui_options = analog_gui_config
        return self

    def with_analog_gui_path(self, analog_gui_path):
        self.analog_gui_options = AnalogGui(gui_path=analog_gui_path)
        return self

    def with_blend_shapes(self):

        self.options.add_blend_shapes = True
        return self

    def with_skin(self):
        self.options.add_skin = True
        return self

    def with_normals(self):

        self.options.add_normals = True
        return self

    def with_meshes(self, meshes):

        self.meshes = meshes
        self.meshes.sort()
        return self

    def with_linear_modifier(self, modifier):
        self.modifiers.linear_modifier = modifier
        return self

    def with_angle_modifier(self, modifier):

        self.modifiers.angle_modifier = modifier
        return self

    def with_rig_logic(self, rig_logic_node_config):

        self.rig_logic_config = rig_logic_node_config or RigLogic()
        return self

    def with_additional_assembly_script(self, aas_config):

        if aas_config.path is None:
            return self

        if aas_config.module_name is None:
            aas_config.module_name = os.path.basename(aas_config.path.split(".")[0])

        self.aas = aas_config
        return self

    def with_ctrl_attributes_on_root_joint(self):
        self.options.add_ctrl_attributes_on_root_joint = True
        return self

    def with_animated_map_attributes_on_root_joint(self):
        self.options.add_animated_map_attributes_on_root_joint = True
        return self

    def with_key_frames(self):
        self.options.add_key_frames = True
        return self
