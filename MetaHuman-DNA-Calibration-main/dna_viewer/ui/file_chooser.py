from PySide2.QtCore import Qt
from PySide2.QtWidgets import (
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QWidget,
)


class FileChooser(QWidget):

    def __init__(
        self,
        label_text,
        parent= None,
        placeholder= "",
        dialog_caption = "Select a file",
        dialog_filter= "All files (*.*)",
        button_text = "...",
        dir_selector = False,
        on_changed = None,
    ):
        super(FileChooser,self).__init__(parent=parent)

        self._dialog_caption = dialog_caption
        self._dialog_filter = dialog_filter
        self._dir_selector = dir_selector

        layout = QHBoxLayout()
        layout.setMargin(0)

        fc_label = QLabel(label_text)
        fc_label.setMinimumHeight(32)

        self.fc_text_field = QLineEdit()
        self.fc_text_field.setAlignment(Qt.AlignLeft)
        self.fc_text_field.setPlaceholderText(placeholder)
        self.fc_text_field.textChanged.connect(on_changed)

        fc_btn = QPushButton(button_text)

        layout.addWidget(fc_label)
        layout.addWidget(self.fc_text_field)
        layout.addWidget(fc_btn)

        fc_btn.clicked.connect(
            self.open_dialog,
        )

        self.setLayout(layout)

    def get_file_path(self):
        return str(self.fc_text_field.text())

    def open_dialog(self):
        if self._dir_selector:
            file_name, _ = QFileDialog.getExistingDirectory(
                self,
                self._dialog_caption,
                "",
                QFileDialog.Option.ShowDirsOnly,
            )
            if file_name:
                self.fc_text_field.setText(file_name)
        else:
            file_name, _ = QFileDialog.getOpenFileName(
                self, self._dialog_caption, "", self._dialog_filter
            )
            if file_name:
                self.fc_text_field.setText(file_name)
