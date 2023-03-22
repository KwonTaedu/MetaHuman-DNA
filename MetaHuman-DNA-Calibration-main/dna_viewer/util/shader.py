import logging

from maya import cmds, mel

from ..util.error import DNAViewerError


class Shader:
    @staticmethod
    def default_lambert_shader(mesh_name, character_name = None, create_character_node = False):
        try:
            if create_character_node:
                names = cmds.ls(("*|"+mesh_name), l=True)
                name = [
                    item for item in names if item.startswith("|"+str(character_name))
                ][0]
                cmds.select(name, r=True)
            else:
                cmds.select(mesh_name, r=True)

            mel.eval("sets -e -forceElement initialShadingGroup")

        except Exception as e:
            logging.error(
                "Couldn't set lambert shader for mesh"+mesh_name+". Reason: "+e
            )
            raise DNAViewerError(e)
