from PySide6.QtCore import Qt
from PySide6.QtGui import QPaintEvent, QResizeEvent
from PySide6.QtWidgets import QWidget, QLabel, QGridLayout, QHBoxLayout, QSizePolicy

'''
    #纪元 结点
    # 剩余时间
'''
class FissureLabel(QWidget):
    def __init__(self, parent: QWidget | None): 
        super().__init__(parent)

        self.tier = "纪元"
        self.node = "结点"
        self.eta = "0m 0s"

        self.tier_label = QLabel(self)
        self.node_label = QLabel(self)
        self.eta_label = QLabel(self)

        grid_layout = QGridLayout(self)
        grid_layout.setSpacing(0)
        grid_layout.setContentsMargins(0, 0, 0, 0)
        grid_layout.addWidget(self.tier_label, 0, 0)
        grid_layout.addWidget(self.node_label, 0, 1)
        grid_layout.addWidget(self.eta_label, 1, 0, 1, 2)

        self.setLayout(grid_layout)

        # for label in self.findChildren(QLabel):
        #     if type(label) == QLabel:
        #         label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def paintEvent(self, event: QPaintEvent) -> None:
        # print(self.tier_label.geometry())
        # print(self.node_label.geometry())
        # print(self.eta_label.geometry())
        return super().paintEvent(event)

    # def resizeEvent(self, event: QResizeEvent):
    # #     self.tier_label.setGeometry(self.rect())
    #     # self.layout().
    #     return super().resizeEvent(event)

    def setTier(self, tier: str):
        self.tier = tier
        self.tier_label.setText(tier)

    def setNode(self, node: str):
        self.node = node
        self.node_label.setText(node)

    def setEta(self, eta: str):
        self.eta = eta
        self.eta_label.setText(eta)

    def setAllData(self, *data: str):
        self.tier = data[0]
        self.node = data[1]
        self.node = data[2]
        self.tier_label.setText(data[0])
        self.node_label.setText(data[1])
        self.eta_label.setText(data[2])