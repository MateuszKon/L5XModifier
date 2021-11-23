from L5XeTree import L5XeTree as L5X

from PySide6.QtCore import Qt, QModelIndex, QPersistentModelIndex
from PySide6.QtGui import QStandardItem, QMouseEvent, QFontMetrics, QPainter
from PySide6.QtWidgets import QTreeWidgetItem, QTreeView, QStyledItemDelegate, QStyleOptionViewItem
import re


class myQtTree_Checkbox(QStandardItem):

    def __init__(self, visible, csv_header_text):
        # TODO: child class for each type of checkbox
        super().__init__()
        self.setSelectable(False)
        self.csv_header_text = csv_header_text
        if visible:
            self.setFlags(Qt.ItemIsEnabled | Qt.ItemFlag.ItemIsUserCheckable)
            self.setData(Qt.CheckState.Unchecked, Qt.ItemDataRole.CheckStateRole)

    def get_checkbox_header(self) -> str:
        # TODO: get_csv_header for Checkbox - might be done
        if self.checkState():  # or something like this
            # return class specific text which will be added to header
            # that way, caller will know, that header is needed to be done
            return self.csv_header_text
        else:
            return ""


class mQtTree_Checkbox_DT(myQtTree_Checkbox):

    def __init__(self, visible):
        csv_header_text = "DT"
        super().__init__(visible, csv_header_text)


class mQtTree_Checkbox_DSC(myQtTree_Checkbox):

    def __init__(self, visible):
        csv_header_text = "DSC"
        super().__init__(visible, csv_header_text)


class mQtTree_Checkbox_Val(myQtTree_Checkbox):

    def __init__(self, visible):
        csv_header_text = "Val"
        super().__init__(visible, csv_header_text)


class mQtTree_Checkbox_Scp(myQtTree_Checkbox):

    def __init__(self, visible):
        csv_header_text = "Scp"
        super().__init__(visible, csv_header_text)


class myQtItem_TemplateItem(QStandardItem):

    def __init__(self, root: L5X.L5XRoot, name: str,
                 DT_visible=True, Dsc_visible=True, Val_visible=True, Scp_visible=True):
        super().__init__(name)
        self.root = root
        self.DT = mQtTree_Checkbox_DT(DT_visible)
        self.Dsc = mQtTree_Checkbox_DSC(Dsc_visible)
        self.Val = mQtTree_Checkbox_Val(Val_visible)
        self.Scp = mQtTree_Checkbox_Scp(Scp_visible)

    def get_row(self):
        return [self, self.DT, self.Dsc, self.Val, self.Scp]

    def get_checkboxes(self):
        return [self.DT, self.Dsc, self.Val, self.Scp]

    def get_csv_header(self) -> (list, list):
        pass
        # TODO: get_csv_header for item - virtual fucntion
        # returns two lists: headers, template_rows
        # create all headers and template_row for this item and all checkboxes


class mQtItem_rung(myQtItem_TemplateItem):

    def __init__(self, root: L5X.L5XRoot, name: str, comment: str, rung_code: str):
        super().__init__(root, name, DT_visible=False, Val_visible=False, Scp_visible=False)
        self.setEditable(False)
        self.setSelectable(False)
        self.comment = comment
        self.code = rung_code
        self.used_tags = self.list_used_tags(self.code)
        self.code_format = self.create_code_format(self.code, self.used_tags)
        for tag in self.used_tags:
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

    @staticmethod
    def create_code_format(code: str, used_tags):
        for tag in used_tags:
            code = code.replace(tag, "{}", 1)
        return code

    def get_csv_header(self) -> (list, list):
        # TODO: get_csv_header for rung
        pass


class mQtItem_alphabetical_tag_virtual(myQtItem_TemplateItem):

    def __init__(self, root: L5X.L5XRoot, name: str, scope, data_type, value, description, tag: L5X.L5XTag, tag_path,
                 DT_visible=True, Dsc_visible=True, Val_visible=True, Scp_visible=True):
        self.scope = scope
        self.data_type = data_type
        self.value = value
        self.description = description
        self.tag = tag
        self.tag_path = tag_path
        self.selected = False
        self.tag_elements = list()
        super().__init__(root, name, DT_visible=DT_visible, Dsc_visible=Dsc_visible, Val_visible=Val_visible,
                         Scp_visible=Scp_visible)
        self.setSelectable(False)

    def tag_clicked(self, event: QMouseEvent, tree):
        # toggle wartość pod self.selected
        # zaznacz odpowiednio wszystkie elementy z drzewka appear order:
        #   1.
        #   2. Stworzyć nazwę taga (już jest pod self.tag_path)
        #   2. Przeanalizować wszystkie elementy drzewka appear order szukając
        self.selected = not self.selected
        all_tags = tree.get_appear_order_tags()
        for tag in all_tags:
            tag: mQtItem_tag_element
            element_name = (self.tag.name + "." + self.tag_path) if len(self.tag_path) else self.tag.name
            if re.match(element_name, tag.text()):
                splitted_tag_path = tag.split_tag_to_parts(element_name)
                selected_index = len(splitted_tag_path) - 1
                tag.alphabetical_selected[selected_index] = not tag.alphabetical_selected[selected_index]

    def update_tag_element(self):
        pass

    def get_csv_header(self) -> (list, list):
        # TODO: get_csv_header for tag
        # returns two lists: headers, template_rows
        # create all headers and template_row for this item and all checkboxes
        # create header for main item
        pass
        # create header for checkboxes
        template_values = [self.data_type, self.value, self.description, self.scope]
        for checkbox, template_value in zip(self.get_checkboxes(), template_values):
            pass


class mQtItem_alphabetical_tag(mQtItem_alphabetical_tag_virtual):

    def __init__(self, root: L5X.L5XRoot, tag_name: str, children_dictionary: dict):
        if root.tag(tag_name) is not None:
            scope = "Controller"
        elif root.any_program().tag(tag_name) is not None:
            scope = root.any_program().attrib["Name"]
        else:
            scope = None
        # set data_type and value of the tag or constant
        if scope is not None:
            tag = root.tag(tag_name, scope)
            data_type = tag.attrib["DataType"]
            if not len(children_dictionary):
                value = tag.get_value()
            else:
                value = None
            description = tag.description
        else:
            data_type = "Constant"
            value = tag_name
            tag = None
            description = None
        val_visible = value is not None
        super().__init__(root, tag_name, scope, data_type, value, description, tag, "", Val_visible=val_visible)
        for element in sorted(children_dictionary):
            element_obj = mQtItem_alphabetical_tag_element(root, element, self.data_type, self.scope,
                                                           children_dictionary[element], tag, element)
            self.tag_elements.append(element_obj)
            self.appendRow(element_obj.get_row())


class mQtItem_alphabetical_tag_element(mQtItem_alphabetical_tag_virtual):

    def __init__(self, root: L5X.L5XRoot, name: str, data_type: str, scope: str, children_dictionary: dict,
                 tag_element: L5X.L5XTag, element_tag_path: str):
        # set data_type and value of the tag or constant
        if scope is not None:
            if not len(children_dictionary):
                value = tag_element.get_value_element(element_tag_path)
            else:
                value = None
            description = tag_element.get_element_comment(element_tag_path) # Might be wrong
        else:
            value = name
            description = None
        val_visible = value is not None
        super().__init__(root, name, scope, data_type, value, description, tag_element, element_tag_path,
                         DT_visible=False, Val_visible=val_visible, Scp_visible=False)
        for element in sorted(children_dictionary):
            if "[" in element:
                child_element_tag_path = element_tag_path + element
            else:
                child_element_tag_path = element_tag_path + "." + element
            element_obj = mQtItem_alphabetical_tag_element(root, element, self.data_type, self.scope,
                                                           children_dictionary[element], tag_element,
                                                           child_element_tag_path)
            self.tag_elements.append(element_obj)
            self.appendRow(element_obj.get_row())


class mQtItem_tag_element(myQtItem_TemplateItem):

    def __init__(self, root: L5X.L5XRoot, name: str):
        # TODO FIX: if in first part of tag will be array index, it will split wrongly
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
        self.alphabetical_selected = list([False for x in range(len(self.splited_text))])
        self.whole_selected = False

    def tag_clicked(self, event: QMouseEvent, tree):
        fm = QFontMetrics(self.font())
        dot = fm.size(0, ".").width()
        left = tree.visualRect(self.index()).left()
        top = tree.visualRect(self.index()).top()
        selected = event.x() - left
        # TODO FIX: clicking area
        start_position = 10
        if event.button() == Qt.RightButton:
            self.whole_selected = False if self.whole_selected else True
        else:
            self.whole_selected = False
            for i, text in enumerate(self.splited_text):
                size = fm.size(0, text).width()
                if start_position <= selected <= start_position+size+dot:
                    if self.selected[i]:
                        self.selected[i] = False
                    else:
                        self.selected[i] = True
                    if text == "[":
                        self.selected[i + 1: i + 2] = [self.selected[i], self.selected[i]]
                    elif text == "]":
                        self.selected[i - 2: i - 1] = [self.selected[i], self.selected[i]]
                    break
                else:
                    start_position += dot + size + 3

    @staticmethod
    def split_tag_to_parts(string, join_index=False):
        first_splitted = string.split(".")
        splitted = list()
        pattern = r"(\[)([\w\.\[\]]+)(\])"
        for element in first_splitted:
            match = re.search(pattern, element)
            if match:
                splitted.append(element[:match.start()])
                if join_index:
                    splitted.append(match.group())
                else:
                    [splitted.append(match.group(i)) for i in range(1, 4)]
                if len(element[match.end():]):
                    splitted.append(element[match.end():])
            else:
                splitted.append(element)
        return splitted

    def update_tag_element(self):
        self.splited_text = self.split_tag_to_parts(self.text())
        self.selected = list([False for x in range(len(self.splited_text))])
        self.alphabetical_selected = list([False for x in range(len(self.splited_text))])
        self.whole_selected = False
