import logging

from maya import cmds

from ..const.naming import SKIN_CLUSTER_AFFIX
from ..const.printing import SKIN_WEIGHT_PRINT_RANGE
from ..model.dna import DNA


class MeshSkin:

    @staticmethod
    def prepare_joints(dna, mesh_index):

        joints = dna.read_all_neutral_joints()
        joints_temp = []
        joint_indices = dna.get_all_skin_weights_joint_indices_for_mesh(mesh_index)

        joint_ids = []
        if any(joint_indices):
            for row in joint_indices:
                for column in row:
                    joints_temp.append(column)

            joint_ids = list(set(joints_temp))
            joint_ids.sort()
        else:
            lod = dna.get_lowest_lod_containing_meshes([mesh_index])
            if lod:
                joint_ids = dna.get_joint_indices_for_lod(lod)

        joint_names = []
        for joint_id in joint_ids:
            joint_names.append(joints[joint_id].name)
        return joint_ids, joint_names

    @staticmethod
    def add_skin_cluster(dna, mesh_index, mesh_name, joint_names):

        logging.info("adding skin cluster...")
        maximum_influences = dna.get_maximum_influence_per_vertex(mesh_index)

        cmds.select(joint_names[0], replace=True)

        cmds.select(mesh_name, add=True)
        skin_cluster = cmds.skinCluster(
            toSelectedBones=True,
            name=mesh_name+"_"+SKIN_CLUSTER_AFFIX,
            maximumInfluences=maximum_influences,
            skinMethod=0,
            obeyMaxInfluences=True,
        )
        if joint_names:
            cmds.skinCluster(
                skin_cluster, edit=True, addInfluence=joint_names[1:], weight=0
            )

    @staticmethod
    def set_skin_weights(dna, mesh_index, mesh_name, joint_ids):

        logging.info("setting skin weights...")
        skin_weights = dna.get_skin_weight_matrix_for_mesh(mesh_index)

        # import skin weights
        temp_str = mesh_name+"_"+SKIN_CLUSTER_AFFIX+".wl["
        for vertex_id, skin_weight in enumerate(skin_weights):
            if not (vertex_id + 1) % SKIN_WEIGHT_PRINT_RANGE:
                #logging.info(str(int(vertex_id) + 1)+" / "+str(len(skin_weights)))
                pass
            vertex_infos = skin_weight

            # set all skin weights to zero
            vertex_string = temp_str+str(vertex_id)+"].w["
            cmds.setAttr(vertex_string+"0]", 0.0)

            # import skin weights
            for vertex_info in vertex_infos:
                cmds.setAttr(
                    vertex_string+str(joint_ids.index(vertex_info[0]))+"]",
                    float(vertex_info[1]),
                )
        if len(skin_weights) % SKIN_WEIGHT_PRINT_RANGE != 0:
            #logging.info(str(int(skin_weights))+" / "+str(len(skin_weights)))
            pass