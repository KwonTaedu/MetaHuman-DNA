from maya.api.OpenMaya import MDagModifier, MFnMesh, MObject

from ..config.mesh import Mesh as MeshConfig
from ..model.dna import DNA
from ..model.mesh import Mesh as MeshModel
from ..util.mesh_blend_shape import MeshBlendShape
print("test")
from ..util.mesh_neutral import MeshNeutral
from ..util.mesh_normals import MeshNormals
from ..util.mesh_skin import MeshSkin
 

class MayaMesh:

    def __init__(self, config, dna):
        self.config = config
        self.data = MeshModel()
        self.fn_mesh = None
        self.mesh_object = None
        self.dag_modifier = None
        self.dna = dna

    def create_neutral_mesh(self):
        MeshNeutral.prepare_mesh(self.config, self.dna, self.data)
        self.fn_mesh, self.mesh_object = MeshNeutral.create_mesh_object(
            self.config, self.data
        )
        self.dag_modifier = MeshNeutral.rename_mesh(
            self.config, self.dna, self.mesh_object
        )
        MeshNeutral.add_texture_coordinates(
            self.config, self.dna, self.data, self.fn_mesh
        )
        return self.mesh_object

    def add_blend_shapes(self, add_mesh_name_to_blend_shape_channel_name):

        if self.dna.has_blend_shapes(self.config.mesh_index):
            MeshBlendShape.create_all_derived_meshes(
                self.config,
                self.dna,
                self.data,
                self.fn_mesh,
                self.dag_modifier,
                add_mesh_name_to_blend_shape_channel_name,
            )
            MeshBlendShape.create_blend_shape_node(
                self.dna.get_mesh_name(self.config.mesh_index),
                self.data.derived_mesh_names,
            )

    def add_skin(self, joint_names, joint_ids):

        mesh_name = self.dna.get_mesh_name(self.config.mesh_index)

        MeshSkin.add_skin_cluster(
            self.dna, self.config.mesh_index, mesh_name, joint_names
        )
        MeshSkin.set_skin_weights(
            self.dna, self.config.mesh_index, mesh_name, joint_ids
        )

    def add_normals(self):

        MeshNormals.add_normals(self.config, self.dna, self.data, self.fn_mesh)
