from ..builder.scene import Scene, SceneResult
from ..config.aas import AdditionalAssemblyScript
from ..config.character import Character
from ..config.gui import Gui
from ..config.rig_logic import RigLogic
from ..config.units import AngleUnit, LinearUnit
from ..const.naming import BLEND_SHAPE_NAME_POSTFIX
from ..model.dna import DNA


def assemble_rig(
    dna,
    analog_gui_path,
    gui_path = None,
    gui = None,
    aas_path = None,
    aas_fn = "run_after_assemble",
    aas_params= None,
    with_attributes_on_root_joint = False,
    with_key_frames = False,
    add_mesh_name_to_blend_shape_channel_name = True):


    meshes = list(range(dna.get_mesh_count()))

    rig_logic = RigLogic()
    if add_mesh_name_to_blend_shape_channel_name:
        rig_logic.with_blend_shape_naming(
            "<objName>"+str(BLEND_SHAPE_NAME_POSTFIX)+".<objName>__<attrName>"
        )

    character_config = (
        Character()
        .with_dna(dna)
        .with_character_node(False)
        .with_meshes(meshes)
        .with_analog_gui_path(analog_gui_path)
        .with_additional_assembly_script(
            AdditionalAssemblyScript(
                path=aas_path,
                method=aas_fn,
                parameter=aas_params if aas_params else {},
            )
        )
        .with_joints()
        .with_normals()
        .with_blend_shapes()
        .with_skin()
        .with_rig_logic(rig_logic)
        .with_add_meshes_to_display_layers(False)
    )

    if gui_path:
        character_config.with_gui_path(gui_path)

    if gui:
        character_config.with_gui(gui)

    if with_attributes_on_root_joint:
        character_config.with_ctrl_attributes_on_root_joint().with_animated_map_attributes_on_root_joint()

    if with_key_frames:
        character_config.with_key_frames()

    character_config.options.add_mesh_name_to_blend_shape_channel_name = (
        add_mesh_name_to_blend_shape_channel_name
    )

    scene_builder = Scene()
    scene_builder.config.with_character(character_config)
    scene_builder.config.with_linear_unit(unit=LinearUnit.cm).with_angle_unit(
        unit=AngleUnit.degree
    )
    return scene_builder.build()
