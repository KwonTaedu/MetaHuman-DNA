import logging

from maya import cmds
from maya.api.OpenMaya import MVector

from ..config.gui import Gui as GuiConfig
from ..const.naming import GUI_HOLDER
from ..const.space import OBJECT
from ..util.error import DNAViewerError
from ..util.maya_util import Maya


class Gui:
    def __init__(self, options = None) :
        self.options = options or GuiConfig()

    def build(self):

        if self.options.gui_path is None:
            raise DNAViewerError("Unable to import gui, must provide gui path...")
        self.position_gui(GUI_HOLDER)

    def position_gui(self, group_name):
        if not cmds.objExists(self.options.eye_gui_name) or not cmds.objExists(self.options.left_eye_joint_name):
            logging.warning(
                "could not find nodes needed for positioning the gui, leaving it at its default position..."
            )
            return

        gui_y = Maya.get_transform(self.options.eye_gui_name).translation(OBJECT).y
        eyes_y = (
            Maya.get_transform(self.options.left_eye_joint_name).translation(OBJECT).y
        )
        delta_y = eyes_y - gui_y

        if isinstance(self.options.gui_translate_x, str):
            try:
                logging.warning(
                    "gui_translate_x should be a float, trying to cast the value to float..."
                )
                self.options.gui_translate_x = float(self.options.gui_translate_x)
            except ValueError:
                logging.error("could not cast string value to float")
                return

        Maya.get_transform(group_name).translateBy(
            MVector(self.options.gui_translate_x, delta_y, 0), OBJECT
        )
