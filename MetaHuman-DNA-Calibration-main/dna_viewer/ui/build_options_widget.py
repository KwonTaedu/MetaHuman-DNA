from PySide2.QtWidgets import QCheckBox, QHBoxLayout, QLabel, QWidget

from ..ui.elements import Elements


class Checkbox:
    unchecked = 0
    checked = 2


class BuildOptionsWidget(QWidget):

    def __init__(self, elements, on_generic_changed):
        super(BuildOptionsWidget,self).__init__()

        self.elements = elements

        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.on_generic_changed = on_generic_changed

        build_options_label = QLabel("Build options:")
        self.layout.addWidget(build_options_label)

        self.elements.joints_cb = self.create_checkbox("joints", self.on_joints_changed)
        self.elements.blend_shapes_cb = self.create_checkbox(
            "blend shapes", self.on_generic_changed
        )
        self.elements.skin_cb = self.create_checkbox("skin", self.on_generic_changed)
        self.elements.rig_logic_cb = self.create_checkbox("rig logic")

        self.setLayout(self.layout)

    def create_checkbox(
        self,
        label,
        on_changed = None,
        checked = False,
        enabled = False):

        checkbox = QCheckBox(label, self)
        checkbox.setChecked(checked)
        checkbox.setEnabled(enabled)
        if on_changed:
            checkbox.stateChanged.connect(on_changed)
        self.layout.addWidget(checkbox)
        return checkbox

    def on_joints_changed(self, state):

        if state == Checkbox.checked.value:
            self.elements.process_btn.setEnabled(True)
            if self.elements.mesh_tree_list.get_selected_meshes():
                self.elements.skin_cb.setEnabled(True)
        else:
            self.elements.skin_cb.setEnabled(False)
            if not self.elements.mesh_tree_list.get_selected_meshes():
                self.elements.process_btn.setEnabled(False)
        self.on_generic_changed(state)
