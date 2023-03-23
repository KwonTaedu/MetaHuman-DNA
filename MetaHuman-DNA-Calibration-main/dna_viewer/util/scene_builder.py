import logging
from os import makedirs
import os

from maya import cmds

from ..config.scene import SaveOptions

from ..config.units import Unit,LinearUnit,AngleUnit
from ..model.dna import DNA


class SceneBuilder:

    LOD_PREFIX = "LOD_"

    @staticmethod
    def add_display_layers(display_layers_needed):
        for lod in display_layers_needed:
            if not cmds.objExists(SceneBuilder.LOD_PREFIX+lod):
                cmds.createDisplayLayer(name=SceneBuilder.LOD_PREFIX+lod)

    @staticmethod
    def save_scene(save_options):

        path = save_options.get_path()
        logging.info("Saving scene to:" +path)
        makedirs(os.path.dirname(path), exist_ok=True)
        cmds.file(rename=path)
        if save_options.extension == "ma":
            cmds.file(save=True, type="mayaAscii")
        elif save_options.extension == "mb":
            cmds.file(save=True, type="mayaBinary")
        else:
            cmds.file(save=True)

    @staticmethod
    def set_units(dna, units):

        linear_unit = units.linear_unit if units.linear_unit else dna.get_linear_unit()
        angle_unit = units.angle_unit if units.angle_unit else dna.get_angle_unit()
        cmds.currentUnit(linear=LinearUnit.name[linear_unit], angle=AngleUnit.name[angle_unit])
        # cmds.currentUnit(linear=LinearUnit.name[linear_unit], angle=angle_unit.name)

    @staticmethod
    def new_scene():
        cmds.file(force=True, new=True)
