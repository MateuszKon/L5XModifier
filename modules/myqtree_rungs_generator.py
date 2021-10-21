from PySide6.QtWidgets import QTreeView
from PySide6.QtGui import QMouseEvent
from widgets.custom_QStandardItems import myQt_rung_generation


class myQTree_rungs_generator(QTreeView):

    def mousePressEvent(self, event: QMouseEvent) -> None:

        index = self.indexAt(event.pos())
        model_pressed = self.model().itemFromIndex(index)
        if isinstance(model_pressed, myQt_rung_generation.mQtItem_tag_element):
            model_pressed.tag_clicked(event, self)
        super().mousePressEvent(event)
