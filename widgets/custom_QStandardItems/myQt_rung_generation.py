from L5XeTree import L5XeTree as L5X

from PySide6.QtCore import Qt, QModelIndex, QPersistentModelIndex
from PySide6.QtGui import QStandardItem, QMouseEvent, QFontMetrics, QPainter
from PySide6.QtWidgets import QTreeWidgetItem, QTreeView, QStyledItemDelegate, QStyleOptionViewItem
import re


class myQtTree_Checkbox(QStandardItem):

    def __init__(self, visible):
        super().__init__()
        self.setSelectable(False)
        if visible:
            self.setFlags(Qt.ItemIsEnabled | Qt.ItemFlag.ItemIsUserCheckable)
            self.setData(Qt.CheckState.Unchecked, Qt.ItemDataRole.CheckStateRole)


class myQtItem_TemplateItem(QStandardItem):

    def __init__(self, root: L5X.L5XRoot, name: str,
                 DT_visible=True, Dsc_visible=True, Val_visible=True, Scp_visible=True):
        super().__init__(name)
        self.root = root
        self.DT = myQtTree_Checkbox(DT_visible)
        self.Dsc = myQtTree_Checkbox(Dsc_visible)
        self.Val = myQtTree_Checkbox(Val_visible)
        self.Scp = myQtTree_Checkbox(Scp_visible)

    def get_row(self):
        return [self, self.DT, self.Dsc, self.Val, self.Scp]


class mQtItem_rung(myQtItem_TemplateItem):

    def __init__(self, root: L5X.L5XRoot, name: str, comment: str, rung_code: str):
        super().__init__(root, name, DT_visible=False, Val_visible=False, Scp_visible=False)
        self.setEditable(False)
        self.setSelectable(False)
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
        # TODO Displaying tag with [1] generates [.1.].
        # split name into tag structure elements
        splitted = name.split(".")
        tag_name = splitted[0]
        # check if there is specific element of the tag, or whole tag
        if len(splitted) > 1:
            self.tag_element = True
        else:
            self.tag_element = False
        # set scope of tag (if tag exist, otherwise it is constant)
        if root.tag(tag_name) is not None:
            self.scope = "Controller"
        elif root.any_program().tag(tag_name) is not None:
            self.scope = root.any_program().attrib["Name"]
        else:
            self.scope = None
        # set data_type and value of the tag or constant
        if self.scope is not None:
            tag = root.tag(tag_name, self.scope)
            self.data_type = tag.attrib["DataType"]
            if self.tag_element:
                self.value = tag.get_value_element(".".join(splitted[1:]))
            else:
                self.value = tag.get_value()
        else:
            self.data_type = "Constant"
            self.value = name
        is_tag = not self.tag_element
        super().__init__(root, name, DT_visible=is_tag, Scp_visible=is_tag)
        self.setSelectable(False)
        self.splited_text = self.split_tag_to_parts(self.text())
        self.selected = list([False for x in range(len(self.splited_text))])

    def tag_clicked(self, event: QMouseEvent, tree):
        # TODO: handling right and left mouse click
        fm = QFontMetrics(self.font())
        dot = fm.size(0, ".").width()
        left = tree.visualRect(self.index()).left()
        top = tree.visualRect(self.index()).top()
        selected = event.x() - left
        # TODO: Fix clicking area
        start_position = 10
        for i, text in enumerate(self.splited_text):
            size = fm.size(0, text).width()
            if start_position <= selected <= start_position+size+dot:
                if self.selected[i]:
                    self.selected[i] = False
                else:
                    self.selected[i] = True
                if text == "[":
                    self.selected[i + 1: i + 2] = self.selected[i]
                elif text == "]":
                    self.selected[i - 2: i - 1] = self.selected[i]
                break
            else:
                start_position += dot + size + 3

    @staticmethod
    def split_tag_to_parts(string):
        first_splitted = string.split(".")
        splitted = list()
        pattern = r"(\[)([\w\.\[\]]+)(\])"
        for element in first_splitted:
            match = re.search(pattern, element)
            if match:
                splitted.append(element[:match.start()])
                [splitted.append(match.group(i)) for i in range(1, 4)]
                splitted.append(element[match.end():])
            else:
                splitted.append(element)
        return splitted
