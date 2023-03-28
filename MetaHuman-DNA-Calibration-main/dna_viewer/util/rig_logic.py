import logging

from maya import mel
from maya.cmds import loadPlugin

from ..builder.rig_logic import RigLogic as RigLogicBuilder
from ..config.character import Character
from ..const.naming import RIG_LOGIC_PREFIX
from ..util.error import DNAViewerError


class RigLogic:

    @staticmethod
    def add_rig_logic(config, character_name) :
        if config.rig_logic_config:
            try:
                #loadPlugin(r"C:\Users\Eon-PC007\Documents\Megascans Library\support\plugins\maya\7.0\MSLiveLink\DHI\lib\Windows\python2\embeddedRL4.mll")
                loadPlugin("embeddedRL4.mll")
                config.rig_logic_config.with_name(RIG_LOGIC_PREFIX+character_name).with_dna_file_path(config.dna.path)
                mel_command = RigLogicBuilder(config.rig_logic_config).build_command()
                logging.info("mel command:"+ mel_command)
                mel.eval(mel_command)
            except :
                logging.error(
                    "The procedure needed for assembling the rig logic was not found, the plugin needed for this might not be loaded."
                )