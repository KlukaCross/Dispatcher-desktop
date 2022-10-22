from PySide6 import QtWidgets, QtGui


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setObjectName("Dispatcher desktop")
        self.central_widget = QtWidgets.QWidget(self)
        self.central_widget.setObjectName("centralwidget")

        self.action_group = QtGui.QActionGroup(self)
        tasks_in_realtime_action = QtGui.QAction("Tasks in realtime", self)
        tasks_without_executor_action = QtGui.QAction("Tasks without executor", self)
        executors_action = QtGui.QAction("Executors", self)
        statistics_action = QtGui.QAction("Statistics", self)

        self.action_group.addAction(tasks_in_realtime_action)
        self.action_group.addAction(tasks_without_executor_action)
        self.action_group.addAction(executors_action)
        self.action_group.addAction(statistics_action)

        self.tool_bar = QtWidgets.QToolBar("Tools", self)
        self.tool_bar.addAction(tasks_in_realtime_action)
        self.tool_bar.addSeparator()
        self.tool_bar.addAction(tasks_without_executor_action)
        self.tool_bar.addSeparator()
        self.tool_bar.addAction(executors_action)
        self.tool_bar.addSeparator()
        self.tool_bar.addAction(statistics_action)