# -*- coding: utf-8 -*-

class AnalogGui:
    def __init__(self,gui_path = None,facial_root_joint_name = "FACIAL_C_FacialRoot",left_eye_joint_name = "FACIAL_L_Eye",right_eye_joint_name = "FACIAL_R_Eye",central_driver_name ="LOC_C_eyeDriver" ,
                 left_eye_driver_name = "LOC_L_eyeDriver",
                 right_eye_driver_name ="LOC_R_eyeDriver" ,left_eye_aim_up_name = "LOC_L_eyeAimUp",right_eye_aim_up_name = "LOC_R_eyeAimUp",central_aim = "GRP_C_eyesAim",le_aim = "GRP_L_eyeAim",re_aim = "GRP_R_eyeAim"
                 ):
        self.gui_path = gui_path

        self.facial_root_joint_name = facial_root_joint_name
        self.left_eye_joint_name = left_eye_joint_name 
        self.right_eye_joint_name = right_eye_joint_name 

        self.central_driver_name = central_driver_name 
        self.left_eye_driver_name = left_eye_driver_name 
        self.right_eye_driver_name = right_eye_driver_name 

        self.left_eye_aim_up_name = left_eye_aim_up_name
        self.right_eye_aim_up_name = right_eye_aim_up_name 
        self.central_aim = central_aim 

        self.le_aim = le_aim 
        self.re_aim = re_aim 


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
