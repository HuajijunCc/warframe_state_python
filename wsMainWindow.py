#sys import
from sqlite3 import connect
import string
import sys
import json
from typing import Self
from PySide6.QtCore import Qt, QSize, QTimer
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QListWidget, QListWidgetItem

#dir import
import wsDataCenter
from widgets.widgets import FissureLabel

class wsMainWindow(QMainWindow):
    def __init__(self): #constructor for mainwindow, init ui and setup the tiemr for updating ui async
        super().__init__()
        self.pc_text = str()

        self.fissure_list = QListWidget(self)
        self.setCentralWidget(self.fissure_list)
        
        # create tiemr for update ui
        self.timer = QTimer(self)
        self.timer.setInterval(1000 * 60)
        self.timer.timeout.connect(self.updateUI)

    def startUpdateUITimer(self):
        self.timer.start()

    def fissureList(self):
        return self.fissure_list

    def updateUI(self):
        tmp_text = wsDataCenter.getAllData("pc")

        if(self.pc_text == "" or self.pc_text != tmp_text):
            self.pc_text = tmp_text
            
        data = json.loads(self.pc_text)
        fissures = data['fissures']

        self.fissure_list.clear()

        for obj in fissures:
            label = FissureLabel(None) 
            label.setAllData(obj['tier'], obj['node'], obj['eta'])

            item = QListWidgetItem(self.fissure_list)
            item.setData(Qt.ItemDataRole.SizeHintRole, QSize(100, 60))
            self.fissure_list.addItem(item)
            self.fissure_list.setItemWidget(item, label)

def saveFile(text):
    file_path = "fissure.json"
    with open(file_path, "w", encoding='utf-8') as file:
        json.dump(text, file, ensure_ascii=False, indent=4)
        print(file_path)

if __name__ == "__main__":
    app = QApplication([])
    window = wsMainWindow()
    window.resize(400, 600)
    window.show()
    window.updateUI()
    window.startUpdateUITimer()
    sys.exit(app.exec())