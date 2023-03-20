import logging

from ..builder.maya_mesh import MayaMesh as MayaMeshBuilder #
from ..config.character import BuildOptions, Character, SpaceModifiers
from ..config.mesh import Mesh as MeshConfig #
from ..model.dna import DNA
from ..util.mesh_skin import MeshSkin #
from ..util.reference import get_geometry_reader #


class Mesh:
    def __init__(self,character_config,dna, mesh_index):
        self.mesh_index = mesh_index
        self.joint_ids = []
        self.joint_names = []

        self.options = character_config.options
        self.modifiers = character_config.modifiers
        self.config = MeshConfig(
            mesh_index=self.mesh_index,
            linear_modifier=self.modifiers.linear_modifier,
        )
        self.dna = dna
        self.mesh = MayaMeshBuilder(self.config, self.dna)

    def build(self):
        self.create_neutral_mesh()
        self.add_normals()
        self.add_blend_shapes()
        self.add_skin()

    def create_neutral_mesh(self):
        self.mesh.create_neutral_mesh()

    def add_normals(self) :

        if self.options.add_normals:
            logging.info("adding normals...")
            self.mesh.add_normals()

    def add_blend_shapes(self) :
        if self.options.add_blend_shapes:
            logging.info("reading blend shapes...")
            geometry_reader = get_geometry_reader(self.mesh_index, self.dna.path)
            geometry_reader.read_blend_shapes(
                self.dna.get_mesh_data(self.mesh_index), self.mesh_index
            )
            logging.info("adding blend shapes...")
            self.mesh.add_blend_shapes(
                self.options.add_mesh_name_to_blend_shape_channel_name
            )

    def add_skin(self):
        if self.options.add_skin and self.options.add_joints:
            self.joint_ids, self.joint_names = MeshSkin.prepare_joints(
                self.dna,
                self.mesh_index,
            )
            self.mesh.add_skin(self.joint_names, self.joint_ids)
