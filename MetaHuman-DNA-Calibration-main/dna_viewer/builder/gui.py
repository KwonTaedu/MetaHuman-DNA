import logging

from maya import cmds
from maya.api.OpenMaya import MVector

from ..config.gui import Gui as GuiConfig
from ..const.naming import GUI_HOLDER
from ..const.space import OBJECT

from ..util.maya_util import Maya #


class Gui:
    def __init__(self, options = None) :
        self.options = options or GuiConfig()

    def build(self):
        self.position_gui(GUI_HOLDER)

    def position_gui(self, group_name):
        if not cmds.objExists(self.options.eye_gui_name) or not cmds.objExists(self.options.left_eye_joint_name):
            return

        gui_y = Maya.get_transform(self.options.eye_gui_name).translation(OBJECT).y
        eyes_y = (
            Maya.get_transform(self.options.left_eye_joint_name).translation(OBJECT).y
        )
        delta_y = eyes_y - gui_y

        if isinstance(self.options.gui_translate_x, str):
            try:
                self.options.gui_translate_x = float(self.options.gui_translate_x)
            except ValueError:
                return

        Maya.get_transform(group_name).translateBy(
            MVector(self.options.gui_translate_x, delta_y, 0), OBJECT
        )
