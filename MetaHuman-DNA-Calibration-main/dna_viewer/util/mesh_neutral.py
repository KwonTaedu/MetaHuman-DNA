import logging

from maya import cmds
from maya.api.OpenMaya import MDagModifier, MFnMesh, MObject, MPoint

from ..config.mesh import Mesh as MeshConfig
from ..model.dna import DNA
from ..model.mesh import Mesh as MeshModel


class MeshNeutral:

    @staticmethod
    def get_vertex_positions_from_dna_vertex_positions(config, data):
        vertex_positions = []
        for position in data.dna_vertex_positions:
            vertex_positions.append(
                MPoint(
                    config.linear_modifier * position.x,
                    config.linear_modifier * position.y,
                    config.linear_modifier * position.z,
                )
            )
        return vertex_positions

    @staticmethod
    def prepare_mesh(config, dna, data):

        logging.info("==============================")
        logging.info("building mesh with mesh_index:"+config.mesh_index)

        data.dna_vertex_positions = dna.get_vertex_positions_for_mesh_index(
            config.mesh_index
        )
        data.dna_vertex_layout_positions = (
            dna.get_vertex_layout_positions_for_mesh_index(config.mesh_index)
        )

        (
            data.polygon_faces,
            data.polygon_connects,
        ) = dna.get_polygon_faces_and_connects(config.mesh_index)

    @staticmethod
    def create_mesh_object(config, data):
        fn_mesh = MFnMesh()

        mesh_object = fn_mesh.create(
            MeshNeutral.get_vertex_positions_from_dna_vertex_positions(config, data),
            data.polygon_faces,
            data.polygon_connects,
        )

        return fn_mesh, mesh_object

    @staticmethod
    def rename_mesh(config, dna, mesh_object):
        mesh_name = dna.get_mesh_name(config.mesh_index)
        logging.info("naming mesh to:"+ mesh_name)

        dag_modifier = MDagModifier()
        dag_modifier.renameNode(mesh_object, mesh_name)
        dag_modifier.doIt()
        return dag_modifier

    @staticmethod
    def get_texture_data(mesh_index, dna):

        texture_coordinates = dna.get_vertex_texture_coordinates_for_mesh(mesh_index)
        dna_faces = dna.get_faces(mesh_index)

        coordinate_indices = []
        for layout_id in range(len(dna.get_layouts_for_mesh_index(mesh_index))):
            coordinate_indices.append(
                dna.get_texture_coordinate_index(mesh_index, layout_id)
            )

        texture_coordinate_us = []
        texture_coordinate_vs = []
        texture_coordinate_indices = []

        index_counter = 0

        for vertices_layout_index_array in dna_faces:
            for vertex_layout_index_array in vertices_layout_index_array:
                texture_coordinate = texture_coordinates[
                    coordinate_indices[vertex_layout_index_array]
                ]
                texture_coordinate_us.append(texture_coordinate.u)
                texture_coordinate_vs.append(texture_coordinate.v)
                texture_coordinate_indices.append(index_counter)
                index_counter += 1

        return texture_coordinate_us, texture_coordinate_vs, texture_coordinate_indices

    @staticmethod
    def add_texture_coordinates(config, dna, data, fn_mesh):
        logging.info("adding texture coordinates...")
        (
            texture_coordinate_us,
            texture_coordinate_vs,
            texture_coordinate_indices,
        ) = MeshNeutral.get_texture_data(config.mesh_index, dna)

        fn_mesh.setUVs(texture_coordinate_us, texture_coordinate_vs)
        fn_mesh.assignUVs(data.polygon_faces, texture_coordinate_indices)

        mesh_name = dna.get_mesh_name(config.mesh_index)

        cmds.select(mesh_name, replace=True)
        cmds.polyMergeUV(mesh_name, distance=0.01, constructionHistory=False)
