from PySide2.QtWidgets import QFrame, QMessageBox, QSizePolicy, QSpacerItem, QWidget


class QHLine(QFrame):
    def __init__(self):
        super(QHLine,self).__init__()
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)


class QVSpacer(QSpacerItem):
    def __init__(self):
        super(QVSpacer,self).__init__(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)


class MessageDialog(QMessageBox):
    def __init__(self,title,message,icon = QMessageBox.Information, parent = QWidget):
        super(MessageDialog,self).__init__(parent)

        self.setIcon(icon)
        self.setWindowTitle(title)
        self.setText(message)
        self.show()