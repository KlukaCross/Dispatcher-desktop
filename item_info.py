from PySide6 import QtWidgets, QtCore


class ItemType:
    TASK = 1
    EXECUTOR = 2


class ItemInfo(QtWidgets.QWidget):
    def __init__(self, data: dict, item_type: ItemType):
        super(ItemInfo, self).__init__()

        grid = QtWidgets.QGridLayout()
        self.setLayout(grid)

        self.fill_list(data)
        save_button = QtWidgets.QPushButton("save")
        save_button.connect(self.save)

        self.data = data
        self.item_type = item_type

    def fill_list(self, data: dict):
        count = 0
        for key in data:
            self.layout().addWidget(QtWidgets.QLabel(key), count, 0)
            line_edit = QtWidgets.QLineEdit(str(data[key]))
            line_edit.triggered.connect()
            self.layout().addWidget(line_edit, count, 1)
            count += 1

    @QtCore.Slot()
    def change_param(self):
        pass

    @QtCore.Slot()
    def save(self):
        # сохранять можем только задачи?
        pass