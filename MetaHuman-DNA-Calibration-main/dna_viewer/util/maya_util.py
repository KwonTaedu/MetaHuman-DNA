from maya.api.OpenMaya import MDagPath, MFnDagNode, MFnTransform, MGlobal, MVector

from ..const.space import OBJECT
from ..util.error import DNAViewerError


class Maya:
    @staticmethod
    def get_element(name):
        try:
            sellist = MGlobal.getSelectionListByName(name)
        except Exception as exception:
            raise DNAViewerError("not found!")
        try:
            return sellist.getDagPath(0)
        except Exception:
            return sellist.getDependNode(0)

    @staticmethod
    def get_transform(name):
        return MFnTransform(Maya.get_element(name))

    @staticmethod
    def get_translation(element, space = OBJECT):
        return MFnTransform(Maya.get_element(element)).translation(space)

    @staticmethod
    def set_translation(element, translation, space = OBJECT):
        element_obj = Maya.get_transform(element)
        element_obj.setTranslation(translation, space)
