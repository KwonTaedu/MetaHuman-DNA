import logging

from maya import cmds, mel
from maya.api.OpenMaya import MFnMesh, MGlobal
from maya.api.OpenMayaAnim import MFnSkinCluster

from ..util.error import DNAViewerError
from ..util.maya_util import Maya


class MayaSkinWeights:
    def __init__(self,no_of_influences,skinning_method,joints,vertices_info):
        self.no_of_influences = no_of_influences
        self.skinning_method = skinning_method
        self.joints = joints
        self.vertices_info = vertices_info


    @staticmethod
    def create(skin_cluster: MFnSkinCluster, mesh_name):

        skin_weights = MayaSkinWeights()

        skin_weights.no_of_influences = cmds.skinCluster(
            skin_cluster.name(), q=True, mi=True
        )

        skin_weights.skinning_method = cmds.skinCluster(
            skin_cluster.name(), q=True, sm=True
        )

        skin_weights.joints = MayaSkinWeights.get_skin_cluster_influence(skin_cluster)

        skin_weights.vertices_info = MayaSkinWeights.get_skin_weights_for_mesh_name(
            skin_cluster, mesh_name
        )

        return skin_weights

    @staticmethod
    def get_skin_cluster_influence(skin_cluster: MFnSkinCluster):

        influences = cmds.skinCluster(skin_cluster.name(), q=True, inf=True)
        if influences and not isinstance(influences[0], str):
            influences = [obj.name() for obj in influences]
        return influences

    @staticmethod
    def get_skin_weights_for_mesh_name(skin_cluster: MFnSkinCluster,mesh_name: str):
        mesh = Maya.get_element(mesh_name)
        components = MGlobal.getSelectionListByName(mesh_name+".vtx[*]").getComponent(0)[1]
        weights_data, chunk = skin_cluster.getWeights(mesh, components)
        iterator = [
            weights_data[i : i + chunk] for i in range(0, len(weights_data), chunk)
        ]

        vertices_info = []
        for weights in iterator:
            vertex_weights = []
            vertices_info.append(vertex_weights)

            for i, weight in enumerate(weights):
                if weight:
                    vertex_weights.append(i)
                    vertex_weights.append(weight)
        return vertices_info


class SkinWeightsMaya:

    def get_skin_weights_data(self, mesh_name):

        skin_cluster = None
        skin_cluster_name = mel.eval("findRelatedSkinCluster" +mesh_name)
        if skin_cluster_name:
            skin_cluster = MFnSkinCluster(Maya.get_element(skin_cluster_name))
            mesh_node = MFnMesh(Maya.get_element(mesh_name))
        if not skin_cluster:
            raise DNAViewerError("Unable to find skin for given mesh:"+ mesh_name)
        return mesh_node, skin_cluster

    def get_skin_weights_from_scene(self, mesh_name):
        _, skin_cluster = self.get_skin_weights_data(mesh_name)

        skin_weights = MayaSkinWeights.create(skin_cluster, mesh_name)

        return skin_weights

    def get_file_joint_mappings(self, skin_weights, skin_cluster):
        file_joint_mapping = []
        for joint_name in skin_weights.joints:
            file_joint_mapping.append(
                skin_cluster.indexForInfluenceObject(Maya.get_element(joint_name))
            )
        return file_joint_mapping

    def set_skin_weights_to_scene(self, mesh_name, skin_weights):

        mesh_node, skin_cluster = self.get_skin_weights_data(mesh_name)

        file_joint_mapping = self.get_file_joint_mappings(skin_weights, skin_cluster)

        self.import_skin_weights(
            skin_cluster, mesh_node, skin_weights, file_joint_mapping
        )

        logging.info("Set skin weights ended.")

    def import_skin_weights(self, skin_cluster, mesh_node,skin_weights, file_joint_mapping,):

        
        temp_str = skin_cluster.name()+".wl["
        for vtx_id in range(cmds.polyEvaluate(mesh_node.name(), vertex=True)):
            vtx_info = skin_weights.vertices_info[vtx_id]

            vtx_str = temp_str+str(vtx_id)+"].w["

            cmds.setAttr(vtx_str+"0]", 0.0)

            for i in range(0, len(vtx_info), 2):
                cmds.setAttr(
                    vtx_str+str(file_joint_mapping[int(vtx_info[i])])+"]",
                    vtx_info[i + 1],
                )
