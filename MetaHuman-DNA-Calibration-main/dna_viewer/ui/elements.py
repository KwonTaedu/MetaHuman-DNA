import os 

from maya import cmds
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QCheckBox, QProgressBar, QPushButton, QWidget
from ..config.character import BuildOptions
from ..model.dna import DNA
from ..ui.file_chooser import FileChooser

class Elements:
    def __init__(self,main_widget = None,select_dna_path=None,load_dna_btn=None,mesh_tree_list=None,joints_cb=None,normals_cb = None,
                 blend_shapes_cb = None, skin_cb=None, rig_logic_cb = None, select_gui_path = None,select_analog_gui_path = None,
                 select_aas_path = None,process_btn = None, progress_bar= None,dna =None
                 ):
        
        self.main_widget = main_widget
        self.select_dna_path = select_dna_path
        self.load_dna_btn = load_dna_btn
        self.mesh_tree_list = mesh_tree_list
        self.joints_cb = joints_cb
        self.normals_cb = normals_cb
        self.blend_shapes_cb = blend_shapes_cb
        self.skin_cb = skin_cb
        self.rig_logic_cb = rig_logic_cb
        self.select_gui_path = select_gui_path
        self.select_analog_gui_path = select_analog_gui_path
        self.select_aas_path = select_aas_path
        self.process_btn = process_btn
        self.progress_bar = progress_bar
        self.dna = dna

    @staticmethod
    def create_new_scene():
        cmds.file(new=True, force=True)

    @staticmethod
    def get_file_path(input):
        path = input.get_file_path()
        if path and os.path.exists(path):
            return path
        return None

    def get_dna_path(self):
        return Elements.get_file_path(self.select_dna_path)

    def get_gui_path(self):
        return Elements.get_file_path(self.select_gui_path)

    def get_analog_gui_path(self):
        return Elements.get_file_path(self.select_analog_gui_path)

    def get_aas_path(self):
        return Elements.get_file_path(self.select_aas_path)

    def get_build_options(self):

        return BuildOptions(
            add_joints=Elements.is_checked(self.joints_cb),
            add_normals=Elements.is_checked(self.normals_cb),
            add_blend_shapes=Elements.is_checked(self.blend_shapes_cb),
            add_skin=Elements.is_checked(self.skin_cb),
        )

    @staticmethod
    def is_checked(checkbox):
        return (
            checkbox is not None
            and bool(checkbox.isEnabled())
            and checkbox.checkState() == Qt.CheckState.Checked
        )
