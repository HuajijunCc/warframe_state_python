#sys import
import sys
import json
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QListWidget, QListWidgetItem

#dir import
import wsDataCenter
from widgets.widgets import FissureLabel


def saveFile(text):


    file_path = "fissure.json"
    with open(file_path, "w", encoding='utf-8') as file:
        json.dump(text, file, ensure_ascii=False, indent=4)
        print(file_path)


if __name__ == "__main__":
    app = QApplication([])
    window = QMainWindow()
    window.resize(400, 600)
    window.show()

    fissure_list = QListWidget(window)
    window.setCentralWidget(fissure_list)

    reply_text = wsDataCenter.getAllData("pc")
    
    data = json.loads(reply_text)

    fissures = data['fissures']

    for obj in fissures:
        label = FissureLabel(None) 
        label.setAllData(obj['tier'], obj['node'], obj['eta'])

        item = QListWidgetItem(fissure_list)
        item.setData(Qt.ItemDataRole.SizeHintRole, QSize(100, 60))
        fissure_list.addItem(item)
        fissure_list.setItemWidget(item, label)

    sys.exit(app.exec())