import logging

from ..builder.scene import Scene as SceneBuilder
from ..config.character import BuildOptions, Character
from ..config.scene import Scene as SceneConfig
from ..config.units import AngleUnit, LinearUnit
from ..model.dna import DNA
from ..util.error import DNAViewerError


def get_mesh_names(dna):
    return dna.get_mesh_names()


def get_mesh_lods(dna):
    result = []

    for lod in range(dna.get_lod_count()):
        mesh_indices = []
        for mesh_index in dna.get_mesh_indices_for_lod(lod):
            mesh_indices.append(mesh_index)
        result.append(mesh_indices)

    return result


def create_build_options(
    add_joints = False,
    add_blend_shapes = False,
    add_skin = False,
    add_ctrl_attributes_on_root_joint = False,
    add_animated_map_attributes_on_root_joint = False,
    add_mesh_name_to_blend_shape_channel_name = False,
    add_key_frames = False):

    return BuildOptions(
        add_joints=add_joints,
        add_blend_shapes=add_blend_shapes,
        add_skin=add_skin,
        add_ctrl_attributes_on_root_joint=add_ctrl_attributes_on_root_joint,
        add_animated_map_attributes_on_root_joint=add_animated_map_attributes_on_root_joint,
        add_mesh_name_to_blend_shape_channel_name=add_mesh_name_to_blend_shape_channel_name,
        add_key_frames=add_key_frames,
    )


def build_meshes(dna, options = None, group_by_lod = False, mesh_list = None, lod_list = None, create_new_scene = False):
    options = options or BuildOptions()

    meshes= []
    meshes_by_lod = get_mesh_lods(dna)

    if lod_list:
        for lod in lod_list:
            meshes.extend(meshes_by_lod[lod])

    if mesh_list:
        meshes.extend(mesh_list)

    if mesh_list is None and lod_list is None:
        meshes = [mesh_index for meshes in meshes_by_lod for mesh_index in meshes]

    character_config = (
        Character()
        .with_dna(dna=dna)
        .with_character_node(value=group_by_lod)
        .with_meshes(meshes=meshes)
    )
    character_config.options = options

    config = (
        SceneConfig()
        .with_character(character=character_config)
        .with_create_new_scene(create_new_scene)
        .with_linear_unit(unit=LinearUnit.cm)
        .with_angle_unit(unit=AngleUnit.degree)
    )
    scene_build_result = SceneBuilder(config).build()

    result = []
    for character_result in scene_build_result.character_results:
        for nodes_by_lod in character_result.nodes.values():
            for node in nodes_by_lod:
                result.append(node)
    return result


def get_mesh_indices_containing_string(mesh_name_part, lod, dna):

    if not 0 <= lod < dna.get_lod_count():
        raise DNAViewerError("Lod "+lod+" does not exist")

    result = []
    for mesh_index in dna.get_mesh_indices_for_lod(lod):
        if mesh_name_part.lower() in dna.get_mesh_name(mesh_index).lower():
            result.append(mesh_index)

    if not result:
        raise DNAViewerError("No results for"+mesh_name_part)

    return result


def get_mesh_index(mesh_name, lod, dna):
    try:
        results = get_mesh_indices_containing_string(mesh_name, lod, dna)
        if results:
            logging.warning(
                "Multiple meshes found, first result is returned, you should probably try a more specific mesh name"
            )
        return results[0]
    except DNAViewerError as e:
        logging.error(e)
    return None
