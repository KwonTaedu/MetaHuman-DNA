import logging

from maya.api.OpenMaya import MObject

from ..config.character import Character as CharacterConfig
from ..model.dna import DNA
from ..util.character_creator import CharacterCreator #
from ..util.error import DNAViewerError


class CharacterBuildResult:
    def __init__(self,nodes = None):
        self.nodes = nodes if nodes else {}

    @staticmethod
    def create(nodes = None):
        nodes if nodes else {}
        result = CharacterBuildResult()
        result.nodes = nodes
        return result


class Character:
    def __init__(self, dna, config = None):
        self.dna = dna
        self.config = config or CharacterConfig()

    def build(self):

        if self.config.dna is None:
            raise DNAViewerError("must provide DNA path")

        creator = CharacterCreator(config=self.config, dna=self.dna)

        logging.info("******************************")
        logging.info(creator.character_name)
        logging.info("******************************")

        creator.create_character_node()
        creator.add_joints_to_character()
        creator.create_ctrl_attributes_on_joint()
        creator.create_animated_map_attributes()
        creator.add_key_frames()
        creator.create_geometry_node()
        creator.create_rig_node()
        creator.create_character_meshes()

        creator.add_gui()
        creator.add_analog_gui()
        creator.add_rig_logic_node()
        creator.run_additional_assembly_script()

        logging.info("built successfully!")
        return CharacterBuildResult.create(nodes=creator.meshes)
