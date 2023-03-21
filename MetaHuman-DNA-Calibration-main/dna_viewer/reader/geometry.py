import logging

#from dna import BinaryStreamReader

from ..const.printing import BLEND_SHAPE_PRINT_RANGE
from ..model.geometry import UV, BlendShape, Layout, Mesh, Point3


class Geometry:

    def __init__(self, stream_reader, mesh_index):
        self.reader = stream_reader
        self.mesh = None
        self.mesh_index = mesh_index

    def read(self):

        self.mesh = Mesh()

        self.add_mesh_name()
        self.add_topology()
        self.add_skin_weights()
        return self.mesh

    def add_mesh_name(self):
        self.mesh.name = self.reader.getMeshName(self.mesh_index)

    def add_skin_weights(self):

        self.mesh.skin_weights.maximum_influence_per_vertex = (
            self.reader.getMaximumInfluencePerVertex(self.mesh_index)
        )
        for vertex_index in range(self.reader.getVertexPositionCount(self.mesh_index)):
            self.mesh.skin_weights.values.append(
                self.reader.getSkinWeightsValues(self.mesh_index, vertex_index)
            )
            self.mesh.skin_weights.joint_indices.append(
                self.reader.getSkinWeightsJointIndices(self.mesh_index, vertex_index)
            )

    def add_topology(self):
        self.add_positions()
        self.add_texture_coordinates()
        self.add_normals()
        self.add_layouts()
        self.add_face_vertex_layouts()

    def add_face_vertex_layouts(self):

        for face_index in range(self.reader.getFaceCount(self.mesh_index)):
            self.mesh.topology.face_vertex_layouts.append(
                self.reader.getFaceVertexLayoutIndices(self.mesh_index, face_index)
            )

    def add_layouts(self):

        for layout_index in range(self.reader.getVertexLayoutCount(self.mesh_index)):
            position_id, texture_coordinate_id, normal_id = self.reader.getVertexLayout(
                self.mesh_index, layout_index
            )
            self.mesh.topology.layouts.append(
                Layout(
                    position_index=position_id,
                    texture_coordinate_index=texture_coordinate_id,
                    normal_index=normal_id,
                )
            )

    def add_normals(self):
        for normal_index in range(self.reader.getVertexNormalCount(self.mesh_index)):
            x, y, z = self.reader.getVertexNormal(self.mesh_index, normal_index)
            self.mesh.topology.normals.append(Point3(x=x, y=y, z=z))

    def add_texture_coordinates(self):
        for texture_coordinate_index in range(
            self.reader.getVertexTextureCoordinateCount(self.mesh_index)
        ):
            u, v = self.reader.getVertexTextureCoordinate(
                self.mesh_index, texture_coordinate_index
            )
            self.mesh.topology.texture_coordinates.append(UV(u=u, v=v))

    def add_positions(self):
        for vertex_index in range(self.reader.getVertexPositionCount(self.mesh_index)):
            x, y, z = self.reader.getVertexPosition(self.mesh_index, vertex_index)
            self.mesh.topology.positions.append(Point3(x=x, y=y, z=z))

    def read_target_deltas(self, blend_shape_target_index):

        result = {}

        vertices = self.reader.getBlendShapeTargetVertexIndices(
            self.mesh_index, blend_shape_target_index
        )

        blend_shape_target_delta_count = self.reader.getBlendShapeTargetDeltaCount(
            self.mesh_index, blend_shape_target_index
        )
        for delta_index in range(blend_shape_target_delta_count):
            x, y, z = self.reader.getBlendShapeTargetDelta(
                self.mesh_index, blend_shape_target_index, delta_index
            )
            result[vertices[delta_index]] = Point3(x=x, y=y, z=z)

        return result

    def read_blend_shapes(self, mesh, mesh_index):

        blend_shape_target_count = self.reader.getBlendShapeTargetCount(mesh_index)
        for blend_shape_target_index in range(blend_shape_target_count):
            if (blend_shape_target_index + 1) % BLEND_SHAPE_PRINT_RANGE == 0:
                logging.info(
                    "\t"+str(blend_shape_target_index + 1)+"/"+blend_shape_target_count
                )

            mesh.blend_shapes.append(
                BlendShape(
                    channel=self.reader.getBlendShapeChannelIndex(
                        mesh_index, blend_shape_target_index
                    ),
                    deltas=self.read_target_deltas(blend_shape_target_index),
                )
            )

        if blend_shape_target_count % BLEND_SHAPE_PRINT_RANGE != 0:
            logging.info("\t"+str(blend_shape_target_count)+"/"+blend_shape_target_count)
