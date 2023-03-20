import logging
import traceback
from typing import List, Optional

from ..builder.character import Character, CharacterBuildResult # import 
from ..config.scene import Scene as SceneConfig
from ..model.dna import DNA
from ..util.conversion import Conversion
from ..util.error import DNAViewerError
from ..util.scene_builder import SceneBuilder


class SceneError(DNAViewerError):
    def __init__(self, message):
        super().__init__("Scene creation failed! Reason: "+message)


class SceneResult:
    character_results = []


class Scene:


    def __init__(self, config = None):
        self.config = config or SceneConfig()
        self.dna = None

    def build(self):

        logging.info("Started building scene")
        try:
            result = SceneResult()
            if self.config.create_new_scene:
                SceneBuilder.new_scene()
            for character_config in self.config.characters:
                self.dna = character_config.dna
                self.set_units()
                if any(
                    character_config.create_display_layers
                    for character_config in self.config.characters
                ):
                    self.add_display_layers()
                self.build_scene(result)
            self.save_scene()
            return result
        except SceneError as e:
            traceback.print_exc()
            raise e
        except Exception as e:
            traceback.print_exc()
            logging.error("Unhandled exception, "+e)
            raise SceneError(str(e)) from e

    def save_scene(self):
        if self.config.save_options:
            SceneBuilder.save_scene(self.config.save_options)

    def set_units(self):
        SceneBuilder.set_units(self.dna, self.config.units)

    def add_display_layers(self):

        display_layers_needed = self.get_display_layers()
        SceneBuilder.add_display_layers(display_layers_needed)

    def get_display_layers(self):
        meshes = []
        for char_config in self.config.characters:
            for idx, meshes_per_lod in enumerate(
                self.dna.get_meshes_by_lods(char_config.meshes)
            ):
                if meshes_per_lod:
                    meshes.append(idx)
        return list(set(meshes))

    def build_scene(self, build_result):
        linear_modifier = Conversion.calculate_linear_modifier(
            self.config.units.linear_unit
        )
        angle_modifier = Conversion.calculate_angle_modifier(
            self.config.units.angle_unit
        )

        results: List[CharacterBuildResult] = []
        for character_config in self.config.characters:
            character_config.with_linear_modifier(linear_modifier).with_angle_modifier(
                angle_modifier
            )
            results.append(Character(self.dna, character_config).build())

        build_result.character_results = results
