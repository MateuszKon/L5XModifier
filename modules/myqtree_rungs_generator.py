from PySide6.QtWidgets import QTreeView, QStyledItemDelegate, QStyleOptionViewItem, QStyle
from PySide6.QtGui import QMouseEvent, QTextDocument, QFont, QAbstractTextDocumentLayout
from PySide6.QtCore import QRect
from widgets.custom_QStandardItems import myQt_rung_generation


class myQTree_rungs_generator(QTreeView):

    def mousePressEvent(self, event: QMouseEvent) -> None:

        index = self.indexAt(event.pos())
        model_pressed = self.model().itemFromIndex(index)
        if isinstance(model_pressed, myQt_rung_generation.mQtItem_tag_element):
            model_pressed.tag_clicked(event, self)
        super().mousePressEvent(event)


class myQStyleDelegate(QStyledItemDelegate):

    def paint(self, painter, option, index) -> None:
        options = QStyleOptionViewItem(option)

        self.initStyleOption(options, index)
        model = index.model().itemFromIndex(index)
        if isinstance(model, myQt_rung_generation.mQtItem_tag_element):
            if len(model.selected) != 0:
                style: QStyle = options.widget.style()
                painter.save()
                string_list = list()
                parentesies_opened = 0
                for text, selected in zip(model.splited_text, model.selected):
                    if selected:
                        if parentesies_opened:
                            string_list[-1] += ('<font color = "green">' + text + '</font>')
                        else:
                            string_list.append('<font color = "green">' + text + '</font>')
                            # string_list.append('<font color = #1E90FF>' + text + '</font>')
                    else:
                        string_list.append(text)
                    if text == "[":
                        parentesies_opened += 1
                    elif text == "]":
                        parentesies_opened -= 1

                string = '<font color = #dddddd>' + ".".join(string_list) + '</font>'
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

                # painter.translate(options.rect.left(), options.rect.top())
                # clip = QRect(0, 0, options.rect.width(), options.rect.height())
                # string_obj = QTextDocument()
                # string_obj.setHtml(string)
                # string_obj.drawContents(painter, clip)
                # model.setText(string_obj.toHtml())

                painter.restore()
                # super().paint(painter, options, index)

            else:
                super().paint(painter, options, index)
        else:
            super().paint(painter, options, index)

