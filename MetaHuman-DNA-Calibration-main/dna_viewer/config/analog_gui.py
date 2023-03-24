# -*- coding: utf-8 -*-

class AnalogGui:
    def __init__(self,gui_path = None,facial_root_joint_name = None,left_eye_joint_name = None,right_eye_joint_name = None,central_driver_name =None ,
                 left_eye_driver_name = None,
                 right_eye_driver_name =None ,left_eye_aim_up_name = None,right_eye_aim_up_name = None,central_aim = None,le_aim = None,re_aim = None
                 ):
        self.gui_path = gui_path if gui_path else None
        self.facial_root_joint_name = facial_root_joint_name if facial_root_joint_name else "FACIAL_C_FacialRoot"
        self.left_eye_joint_name = left_eye_joint_name if left_eye_joint_name else "FACIAL_L_Eye"
        self.right_eye_joint_name = right_eye_joint_name if right_eye_joint_name else "FACIAL_R_Eye"
        self.central_driver_name = central_driver_name if central_driver_name else "LOC_C_eyeDriver"
        self.left_eye_driver_name = left_eye_driver_name if left_eye_driver_name else "LOC_L_eyeDriver"
        self.right_eye_driver_name = right_eye_driver_name if right_eye_driver_name else "LOC_R_eyeDriver"
        self.left_eye_aim_up_name = left_eye_aim_up_name if left_eye_aim_up_name else "LOC_L_eyeAimUp"
        self.right_eye_aim_up_name = right_eye_aim_up_name if right_eye_aim_up_name else "LOC_R_eyeAimUp"
        self.central_aim = central_aim if central_aim else "GRP_C_eyesAim"
        self.le_aim = le_aim if le_aim else "GRP_L_eyeAim"
        self.re_aim = re_aim if re_aim else "GRP_R_eyeAim"


    def with_gui_path(self, gui_path):
        # type : (str) -> None

        self.gui_path = gui_path
        return self # "AnalogGui"

    def with_facial_root_joint_name(self, joint_name):
        # type : (str) -> None

        self.facial_root_joint_name = joint_name
        return self

    def with_left_eye_joint_name(self, joint_name):
       # type : (str) -> None

        self.left_eye_joint_name = joint_name
        return self

    def with_right_eye_joint_name(self, joint_name):
        # type : (str) -> None

        self.right_eye_joint_name = joint_name
        return self

    def with_central_driver_name(self, driver_name):
        # type : (str) -> None

        self.central_driver_name = driver_name
        return self

    def with_left_eye_driver_name(self, driver_name):
        # type : (str) -> None

        self.left_eye_driver_name = driver_name
        return self

    def with_right_eye_driver_name(self, driver_name):
        # type : (str) -> None

        self.right_eye_driver_name = driver_name
        return self

    def with_left_eye_aim_up_name(self, name):
        # type : (str) -> None

        self.left_eye_aim_up_name = name
        return self

    def with_right_eye_aim_up_name(self, name):
        # type : (str) -> None

        self.right_eye_aim_up_name = name
        return self

    def with_central_aim(self, name):
        # type : (str) -> None

        self.central_aim = name
        return self

    def with_left_eye_aim(self, name):
        # type : (str) -> None

        self.le_aim = name
        return self

    def with_right_eye_aim(self, name):
        # type : (str) -> None

        self.re_aim = name
        return self
