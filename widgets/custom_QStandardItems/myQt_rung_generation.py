from L5XeTree import L5XeTree as L5X

from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItem
from PySide6.QtWidgets import QTreeWidgetItem
import re


class myQtTree_Checkbox(QStandardItem):

    def __init__(self, visible):
        super().__init__()
        if visible:
            self.setFlags(Qt.ItemIsEnabled | Qt.ItemFlag.ItemIsUserCheckable)
            self.setData(Qt.CheckState.Unchecked, Qt.ItemDataRole.CheckStateRole)


class myQtItem_TemplateItem(QStandardItem):

    def __init__(self, root: L5X.L5XRoot, name: str,
                 TN_visible=True, DT_visible=True, Dsc_visible=True, Val_visible=True, Scp_visible=True):
        super().__init__(name)
        self.root = root
        self.TN = myQtTree_Checkbox(TN_visible)
        self.DT = myQtTree_Checkbox(DT_visible)
        self.Dsc = myQtTree_Checkbox(Dsc_visible)
        self.Val = myQtTree_Checkbox(Val_visible)
        self.Scp = myQtTree_Checkbox(Scp_visible)

    def get_row(self):
        return [self, self.TN, self.DT, self.Dsc, self.Val, self.Scp]


class mQtItem_rung(myQtItem_TemplateItem):

    def __init__(self, root: L5X.L5XRoot, name: str, comment: str, rung_code: str):
        super().__init__(root, name, TN_visible=False, DT_visible=False, Scp_visible=False)
        self.comment = comment
        self.code = rung_code
        for tag in self.list_used_tags(self.code):
            self.appendRow(mQtItem_tag_element(root, tag).get_row())

    @staticmethod
    def list_used_tags(code):
        pattern = r"\w+\(([\w.,\[\]\?]+)\)"
        matches = re.findall(pattern, code)
        used_tags = list()
        for match in matches:
            tags = match.split(",")
            for tag in tags:
                used_tags.append(tag)
        return used_tags


class mQtItem_tag(myQtItem_TemplateItem):
    pass


class mQtItem_tag_element(myQtItem_TemplateItem):

    def __init__(self, root: L5X.L5XRoot, name: str):
        super().__init__(root, name)
