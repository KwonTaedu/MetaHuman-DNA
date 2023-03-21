from ..config.rig_logic import RigLogic as RigLogicConfig
from ..util.error import DNAViewerError


class RigLogic:
    def __init__(self, config = None):
        self.config = config or RigLogicConfig()

    def build_command(self):

        if self.config.name is None:
            raise DNAViewerError("Must provide a node name for the rig logic")

        if self.config.dna_file_path is None:
            raise DNAViewerError("Must provide a DNA file path")

        string_to_be_executed = self.config.command
        string_to_be_executed += " -n '"+self.config.name+"'"
        string_to_be_executed += ' -dfp "'+self.config.dna_file_path+'"'
        string_to_be_executed += ' -cn "'+self.config.control_naming+'"'
        string_to_be_executed += ' -jn "'+self.config.joint_naming+'"'
        string_to_be_executed += ' -bsn "'+self.config.blend_shape_naming+'"'
        string_to_be_executed += ' -amn "'+self.config.animated_map_naming+'"; '
        return string_to_be_executed
