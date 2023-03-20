from ..const.gui import EYE_GUI, EYE_JOINT, GUI_TRANSLATE_X

class Gui:
    def __init__(self,gui_path = None):
        self.gui_path = gui_path
        self.left_eye_joint_name = EYE_JOINT
        self.eye_gui_name = EYE_GUI
        self.gui_translate_x = GUI_TRANSLATE_X

    def with_gui_path(self, gui_path):
        self.gui_path = gui_path
        return self

    def with_left_eye_joint_name(self, name):
        self.left_eye_joint_name = name
        return self

    def with_eye_gui_name_name(self, name):
        self.eye_gui_name = name
        return self

    def with_gui_translate_x(self, value):
        self.gui_translate_x = value
        return self