from PySide6 import QtWidgets, QtGui, QtCore
from item_info import ItemInfo

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setObjectName("Dispatcher desktop")
        self.central_widget = QtWidgets.QListWidget()
        self.central_widget.itemActivated.connect(self.open_item_info)

        self.setCentralWidget(self.central_widget)

        self.action_group = QtGui.QActionGroup(self)
        tasks_in_realtime_action = QtGui.QAction("Tasks in realtime")
        tasks_in_realtime_action.triggered.connect(self.show_realtime_tasks)
        tasks_without_executor_action = QtGui.QAction("Tasks without executor")
        tasks_without_executor_action.triggered.connect(self.show_without_executors_tasks)
        executors_action = QtGui.QAction("Executors")
        executors_action.triggered.connect(self.show_executors)
        statistics_action = QtGui.QAction("Statistics")
        statistics_action.triggered.connect(self.show_statistics)
        slider = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)

        self.action_group.addAction(tasks_in_realtime_action)
        self.action_group.addAction(tasks_without_executor_action)
        self.action_group.addAction(executors_action)
        self.action_group.addAction(statistics_action)

        self.tool_bar = self.addToolBar("Tools")
        self.tool_bar.setMovable(False)
        self.tool_bar.addWidget(QtWidgets.QLabel(self))
        self.tool_bar.addSeparator()
        self.tool_bar.addWidget(slider)
        self.tool_bar.addAction(tasks_in_realtime_action)
        self.tool_bar.addSeparator()
        self.tool_bar.addAction(tasks_without_executor_action)
        self.tool_bar.addSeparator()
        self.tool_bar.addAction(executors_action)
        self.tool_bar.addSeparator()
        self.tool_bar.addAction(statistics_action)

        self.now_item_info = None
    @QtCore.Slot()
    def show_realtime_tasks(self):
        self.central_widget.clear()
        self.create_item("task1", {"start_time": 1, "end_time": 2})
        self.create_item("task2", {"start_time": 1, "end_time": 2})
        self.create_item("task3", {"start_time": 1, "end_time": 2})
        self.create_item("task4", {"start_time": 1, "end_time": 2})
        self.create_item("task5", {"start_time": 1, "end_time": 2})
        self.create_item("task6", {"start_time": 1, "end_time": 2})
        self.create_item("task7", {"start_time": 1, "end_time": 2})
        self.create_item("task8", {"start_time": 1, "end_time": 2})

    @QtCore.Slot()
    def show_without_executors_tasks(self):
        self.central_widget.clear()
        self.create_item("task1", {"start_time": 1, "end_time": 2})
        self.create_item("task2", {"start_time": 1, "end_time": 2})
        self.create_item("task3", {"start_time": 1, "end_time": 2})
        self.create_item("task4", {"start_time": 1, "end_time": 2})

    @QtCore.Slot()
    def show_executors(self):
        self.central_widget.clear()
        self.create_item("executor1", {"start_time": 1, "end_time": 2})
        self.create_item("executor2", {"start_time": 1, "end_time": 2})
        self.create_item("executor3", {"start_time": 1, "end_time": 2})
        self.create_item("executor4", {"start_time": 1, "end_time": 2})
        self.create_item("executor5", {"start_time": 1, "end_time": 2})

    @QtCore.Slot()
    def show_statistics(self):
        print("Statistics")

    @QtCore.Slot()
    def show_interval_tasks(self):
        self.central_widget.clear()
        self.create_item("task11", {"start_time": 1, "end_time": 2})
        self.create_item("task12", {"start_time": 1, "end_time": 2})
        self.create_item("task13", {"start_time": 1, "end_time": 2})
        self.create_item("task14", {"start_time": 1, "end_time": 2})
        self.create_item("task15", {"start_time": 1, "end_time": 2})
        self.create_item("task16", {"start_time": 1, "end_time": 2})

    def create_item(self, id_task, data):
        item = QtWidgets.QListWidgetItem(id_task)
        item.setData(1, data)
        self.central_widget.addItem(item)

    @QtCore.Slot()
    def open_item_info(self, item):
        if self.now_item_info and self.now_item_info.isVisible():
            return
        self.now_item_info = ItemInfo(item.data(1))
        self.now_item_info.show()
