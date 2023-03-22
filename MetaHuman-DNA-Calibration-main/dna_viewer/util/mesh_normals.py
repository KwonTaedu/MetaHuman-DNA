from maya import cmds, mel
from maya.api.OpenMaya import MFnMesh, MSpace, MVector

from ..config.mesh import Mesh as MeshConfig
from ..model.dna import DNA
from ..model.mesh import Mesh as MeshModel
from ..util.maya_util import Maya


class MeshNormals:

    @staticmethod
    def add_normals(config,dna,data,fn_mesh,space = MSpace.kObject):

        data.vertex_normals = dna.get_vertex_normals_for_mesh(config.mesh_index)
        data.dna_vertex_layout_normals = []
        for layout in dna.get_layouts_for_mesh_index(config.mesh_index):
            data.dna_vertex_layout_normals.append(
                dna.get_normal_for_mesh_index_and_layout(config.mesh_index, layout)
            )
        
        normal_array = []
        face_array = []
        vertex_array = []

        dna_faces = dna.get_faces(config.mesh_index)
        for face_id, vertices_layout_index_array in enumerate(dna_faces):
            for vertex_layout_index in vertices_layout_index_array:
                vertex_normal_raw = data.dna_vertex_layout_normals[vertex_layout_index]
                vertex_normal = MVector(
                    vertex_normal_raw.x, vertex_normal_raw.y, vertex_normal_raw.z
                )
                normal_array.append(vertex_normal)
                face_array.append(face_id)
                vertex_id = data.dna_vertex_layout_positions[vertex_layout_index]
                vertex_array.append(vertex_id)

        fn_mesh.setFaceVertexNormals(normal_array, face_array, vertex_array, space)

        mesh_node = MFnMesh(Maya.get_element(dna.get_mesh_name(config.mesh_index)))
        mesh_node.unlockVertexNormals(range(len(data.dna_vertex_positions)))
        cmds.polySoftEdge(mesh_node.name(), a=180, ch=False)
        mel.eval("BakeAllNonDefHistory;")
