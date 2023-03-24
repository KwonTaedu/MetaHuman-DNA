import os

from ..config.character import Character
from .units import AngleUnit, LinearUnit, Unit


class SaveOptions:
    def __init__(self,name=None, extension=None, destination_path = None):
        self.name = name
        self.extension = extension
        self.destination_path = destination_path if destination_path else str(os.getcwd())

    def get_path(self):
        return self.destination_path+"/"+self.name+"."+self.extension

class Scene:
    def __init__(self,dna_path=None, characters= None, units = None,create_new_scene = True,save_options = None):
        self.dna_path = dna_path
        self.characters = characters if characters else []
        self.units = units if units else Unit()
        self.create_new_scene = create_new_scene
        self.save_options = save_options

    def with_character(self, character):

        self.characters.append(character)
        return self

    def with_linear_unit(self, unit):

        self.units.linear_unit = unit
        return self

    def with_angle_unit(self, unit) :
        self.units.angle_unit = unit
        return self

    def with_create_new_scene(self, create_new_scene):
        self.create_new_scene = create_new_scene
        return self

    def with_scene_file_path(
        self,
        name = "untitled_scene",
        extension = "mb",
        destination_path = None,
    ):

        if destination_path is None:
            destination_path = str(os.getcwd())

        self.save_options = SaveOptions(
            name=name, extension=extension, destination_path=destination_path
        )
        return self
