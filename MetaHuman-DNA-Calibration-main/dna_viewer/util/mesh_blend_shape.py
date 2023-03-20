import logging

from maya import cmds
from maya.api.OpenMaya import MDagModifier, MFnDagNode, MFnMesh, MPoint

from ..config.mesh import Mesh
from ..const.naming import (
    BLEND_SHAPE_GROUP_PREFIX,
    BLEND_SHAPE_NAME_POSTFIX,
    BLEND_SHAPE_NAMING,
    DERIVED_MESH_NAME,
    MESH_NAME,
)
from ..const.printing import BLEND_SHAPE_PRINT_RANGE
from ..model.dna import DNA
from ..model.geometry import Point3
from ..model.mesh import Mesh as MayaMeshModel
from ..util.maya_util import Maya
from ..util.mesh_neutral import MeshNeutral


class MeshBlendShape:
    @staticmethod
    def create_all_derived_meshes(config,dna,data,fn_mesh,dag_modifier,add_mesh_name_to_blend_shape_channel_name):


        logging.info("building derived meshes...")

        group: str = cmds.group(
            empty=True,
            name= BLEND_SHAPE_GROUP_PREFIX+dna.get_mesh_name(config.mesh_index)
        )

        data.derived_mesh_names = []
        blend_shapes = dna.get_blend_shapes(config.mesh_index)
        for blend_shape_target_index, blend_shape in enumerate(blend_shapes):
            if (blend_shape_target_index + 1) % BLEND_SHAPE_PRINT_RANGE == 0:
                logging.info("\t"+str(blend_shape_target_index+1) +"/" +len(blend_shapes))
                                

            MeshBlendShape._create_derived_mesh(
                config,
                dna,
                data,
                blend_shape_target_index,
                blend_shape.channel,
                group,
                fn_mesh,
                dag_modifier,
                add_mesh_name_to_blend_shape_channel_name,
            )

        if len(blend_shapes) % BLEND_SHAPE_PRINT_RANGE != 0:
            logging.info("\t"+str(blend_shapes) +"/" +len(blend_shapes))

        cmds.setAttr(group+".visibility", 0)

    @staticmethod
    def _create_derived_mesh(config,dna,data, blend_shape_target_index,blend_shape_channel,group,fn_mesh,dag_modifier,add_mesh_name_to_blend_shape_channel_name):

        new_vert_layout = MeshNeutral.get_vertex_positions_from_dna_vertex_positions(
            config=config, data=data
        )

        zipped_deltas = dna.get_blend_shape_target_deltas_with_vertex_id(
            config.mesh_index, blend_shape_target_index
        )
        for zipped_delta in zipped_deltas:
            delta: Point3 = zipped_delta[1]
            new_vert_layout[zipped_delta[0]] += MPoint(
                config.linear_modifier * delta.x,
                config.linear_modifier * delta.y,
                config.linear_modifier * delta.z,
            )

        new_mesh = fn_mesh.create(
            new_vert_layout, data.polygon_faces, data.polygon_connects
        )
        derived_name = dna.get_blend_shape_name(blend_shape_channel)
        name = (
            dna.geometry.meshes[config.mesh_index].name+"__"+derived_name
            if add_mesh_name_to_blend_shape_channel_name
            else derived_name
        )
        dag_modifier.renameNode(new_mesh, name)
        dag_modifier.doIt()

        dag = MFnDagNode(Maya.get_element(group))
        dag.addChild(new_mesh)

        data.derived_mesh_names.append(name)

    @staticmethod
    def create_blend_shape_node(mesh_name, derived_mesh_names, rename = False):
        nodes = []
        for derived_mesh_name in derived_mesh_names:
            if rename:
                name = BLEND_SHAPE_NAMING.replace(MESH_NAME, mesh_name).replace(
                    DERIVED_MESH_NAME, derived_mesh_name
                )
            else:
                name = derived_mesh_name

            nodes.append(name)

        cmds.select(nodes, replace=True)

        cmds.select(mesh_name, add=True)
        cmds.blendShape(name=mesh_name+BLEND_SHAPE_NAME_POSTFIX)
        cmds.delete(BLEND_SHAPE_GROUP_PREFIX+mesh_name)

