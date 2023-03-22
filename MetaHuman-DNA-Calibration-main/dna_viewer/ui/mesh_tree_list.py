from PySide2.QtCore import Qt
from PySide2.QtWidgets import (
    QGridLayout,
    QLabel,
    QTreeWidget,
    QTreeWidgetItem,
    QTreeWidgetItemIterator,
    QVBoxLayout,
    QWidget,
)

from ..model.definition import NamesAndIndices
from ..ui.elements import Elements


class MeshTreeList(QWidget):

    def __init__(self, elements):
        super(MeshTreeList,self).__init__()
        self.elements = elements

        label = QLabel("Meshes:")
        self.mesh_tree = self.create_mesh_tree()

        layout = QGridLayout()
        layout.addWidget(self.mesh_tree, 0, 0, 4, 1)
        layout.setContentsMargins(0, 0, 0, 0)

        layout_holder = QVBoxLayout()
        layout_holder.addWidget(label)
        layout_holder.addLayout(layout)
        layout_holder.setContentsMargins(0, 0, 0, 0)

        self.setLayout(layout_holder)

    def create_mesh_tree(self):

        mesh_tree = QTreeWidget()
        mesh_tree.setHeaderHidden(True)
        mesh_tree.itemChanged.connect(self.tree_item_changed)
        mesh_tree.setStyleSheet("background-color: #505050")
        return mesh_tree

    def fill_mesh_list(self, lod_count, meshes):
        self.mesh_tree.clear()

        for i in range(lod_count):
            parent = QTreeWidgetItem(self.mesh_tree)
            parent.setText(0, "LOD "+str(i))
            parent.setFlags(parent.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)

            meshes_in_lod = meshes.indices_for_lod[i]

            for mesh_index in meshes_in_lod:
                child = QTreeWidgetItem(parent)
                child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
                child.setText(0, str(meshes.names[mesh_index]))
                child.setCheckState(0, Qt.Unchecked)

            self.mesh_tree.setItemExpanded(parent, True)

    def get_selected_meshes(self):

        meshes = []

        iterator = QTreeWidgetItemIterator(
            self.mesh_tree, QTreeWidgetItemIterator.Checked
        )
        while iterator.value():
            item = iterator.value()
            mesh_name = item.text(0)
            mesh_index = self.elements.dna.get_mesh_id_from_mesh_name(mesh_name)
            if mesh_index is not None:
                meshes.append(mesh_index)

            iterator += 1

        return meshes

    def tree_item_changed(self):
        meshes = self.get_selected_meshes()

        if meshes:
            self.elements.skin_cb.setEnabled(self.elements.joints_cb.checkState())
            self.elements.blend_shapes_cb.setEnabled(True)
            self.elements.process_btn.setEnabled(True)
            self.elements.rig_logic_cb.setEnabled(False)

            total_meshes = len(self.elements.dna.get_mesh_names())
            if len(meshes) == total_meshes:
                self.elements.rig_logic_cb.setEnabled(
                    self.elements.joints_cb.checkState()
                    and self.elements.blend_shapes_cb.checkState()
                    and self.elements.skin_cb.checkState()
                    and self.elements.get_file_path(self.elements.select_gui_path)
                    is not None
                    and self.elements.get_file_path(
                        self.elements.select_analog_gui_path
                    )
                    is not None
                    and self.elements.get_file_path(self.elements.select_aas_path)
                    is not None
                )
        else:
            self.elements.skin_cb.setEnabled(False)
            self.elements.blend_shapes_cb.setEnabled(False)
            self.elements.process_btn.setEnabled(self.elements.joints_cb.checkState())
