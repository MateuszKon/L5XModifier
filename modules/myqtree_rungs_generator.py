from PySide6.QtWidgets import QTreeView, QStyledItemDelegate, QStyleOptionViewItem, QStyle
from PySide6.QtGui import QMouseEvent, QTextDocument, QFont, QAbstractTextDocumentLayout, QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt, QRect, QModelIndex
from widgets.custom_QStandardItems import myQt_rung_generation


class myQTree_rungs_generator(QTreeView):

    def __init__(self, parent):
        super().__init__(parent=parent)
        self.appear_order_model = None
        self.alphabetical_order_model = None

    def mousePressEvent(self, event: QMouseEvent) -> None:
        index = self.indexAt(event.pos())
        model_pressed = self.model().itemFromIndex(index)
        if isinstance(model_pressed, myQt_rung_generation.mQtItem_tag_element):
            model_pressed.tag_clicked(event, self)
        elif isinstance(model_pressed, myQt_rung_generation.mQtItem_alphabetical_tag_virtual):
            model_pressed.tag_clicked(event, self)
        super().mousePressEvent(event)

    def set_appear_order_model(self, tree_model: QStandardItemModel):
        self.appear_order_model = tree_model

    def set_alphabetical_order_model(self, tree_model: QStandardItemModel):
        self.alphabetical_order_model = tree_model

    def get_appear_order_tags(self):
        rung_list = self.get_appear_order_rungs()
        tag_list = list()
        for rung in rung_list:
            tag_list += self.get_appear_order_rung_tags(rung)
        return tag_list
        tag_list = list()

    def get_appear_order_rungs(self):
        model: QStandardItemModel = self.appear_order_model
        rung_list = list()
        for i in range(model.rowCount()):
            index = model.index(i, 0)
            rung: QStandardItem = index.model().itemFromIndex(index)
            rung_list.append(rung)
        return rung_list

    @staticmethod
    def get_appear_order_rung_tags(rung):
        tag_list = list()
        for i in range(rung.rowCount()):
            tag: myQt_rung_generation.mQtItem_tag_element = rung.child(i, 0)
            tag_list.append(tag)
        return tag_list

    def get_alphabetical_order_tags(self):
        # GET ALL ITEMS (model.children? model.allrows?)
        model: QStandardItemModel = self.alphabetical_order_model
        tag_list = list()
        for i in range(model.rowCount()):
            index = model.index(i, 0)
            tag: myQt_rung_generation.mQtItem_alphabetical_tag = index.model().itemFromIndex(index)
            tag_list.append(tag)
        return tag_list

    def get_information_for_csv(self) -> (list, list):
        pass
        # TODO: taking all information from tree for exporting to csv file
        #  returns: headers (selected elements for change) and first_row (values from template)
        headers = list()
        template_row = list()
        # 1. Get selected elements from alphabetical order and appends to lists (headers and first_row)
        for tag in self.get_alphabetical_order_tags():
            header_list, template_list = tag.get_csv_header()
            if len(header):
                for header, template in zip(header_list, template_list):
                    headers.append(header)
                    template_row.append(template)
        # 2. Get selected elements from appear order and appends to lists, like above
        for rung in self.get_appear_order_rungs():
            # get_csv_header of rung (if is modified)
            for tag in self.get_appear_order_rung_tags(rung):
                pass
                # get_csv_header of tags
                # add rung name into header


class myQStyleDelegate(QStyledItemDelegate):

    def paint(self, painter, option, index) -> None:
        options = QStyleOptionViewItem(option)
        self.initStyleOption(options, index)
        model = index.model().itemFromIndex(index)

        # PAINTING APPEAR ORDER ELEMENT
        if isinstance(model, myQt_rung_generation.mQtItem_tag_element):
            if model.whole_selected:
                string = '<font color = "yellow">' + model.text() + '</font>'
                self.painting_with_painter(painter, option, string)
            else:
                string_list = list()
                parentheses_opened = 0
                for text, selected, alphabetical_selected in zip(model.splited_text, model.selected,
                                                                 model.alphabetical_selected):
                    if selected:
                        text_to_append = '<font color = "green">' + text + '</font>'
                    elif alphabetical_selected:
                        text_to_append = '<font color = "red">' + text + '</font>'
                    else:
                        text_to_append = text
                    if text == "[":
                        parentheses_opened += 1
                    if parentheses_opened:
                        string_list[-1] += text_to_append
                    else:
                        string_list.append(text_to_append)
                        # string_list.append('<font color = #1E90FF>' + text + '</font>')
                    if text == "]":
                        parentheses_opened -= 1
                string = '<font color = #dddddd>' + ".".join(string_list) + '</font>'
                self.painting_with_painter(painter, option, string)

        # PAINTING ALPHABETICAL ORDER ELEMENT
        elif isinstance(model, myQt_rung_generation.mQtItem_alphabetical_tag_virtual):
            if model.selected:
                string = '<font color = "red">' + model.text() + '</font>'
                self.painting_with_painter(painter, option, string)
            else:
                super().paint(painter, options, index)

        # PAINTING EVERYTHING ELSE
        else:
            super().paint(painter, options, index)

    def painting_with_painter(self, painter, option, string):
        options = QStyleOptionViewItem(option)
        style: QStyle = options.widget.style()
        painter.save()
        textRect = style.subElementRect(QStyle.SE_ItemViewItemText, options)
        style.drawControl(QStyle.CE_ItemViewItem, option, painter, option.widget)
        textRect.setTop(textRect.top() - 3)
        textRect.setLeft(textRect.left() - 1)
        painter.translate(textRect.topLeft())
        painter.setClipRect(textRect.translated(-textRect.topLeft()))
        ctx = QAbstractTextDocumentLayout.PaintContext()
        string_obj = QTextDocument()
        string_obj.setHtml(string)
        new_font = string_obj.defaultFont()
        new_font.setPointSize(10)
        string_obj.setDefaultFont(new_font)
        string_obj.documentLayout().draw(painter, ctx)
        painter.restore()
