from PySide6.QtGui import QStandardItem


class MyQTreeItem(QStandardItem):

    def __init__(self, name: str, editable: bool = False):
        super().__init__(name)
        self.setEditable(editable)


class MyQTreeItemName(MyQTreeItem):

    def __init__(self, name: str):
        super().__init__(name, False)


class MyQTreeItemDataType(MyQTreeItem):

    def __init__(self, name: str):
        super().__init__(name, False)


class MyQTreeItemValue(MyQTreeItem):

    def __init__(self, name: str, editable: bool = False):
        super().__init__(name, editable)


class MyQTreeItemString(MyQTreeItemValue):
    def __init__(self, name: str):
        super().__init__(name, True)