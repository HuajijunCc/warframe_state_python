import sys
import json
from tokenize import String
import wsDataCenter
from io import StringIO
# import json
from PySide6.QtWidgets import QApplication, QWidget

def saveFile(text):
    # if(type(text) == list):
        for obj in text:
            # if(type(obj) == dict):
                type = obj['missionKey']
                enemy = obj['enemyKey']
                isHard = obj['isHard']
                if type == 'Survival' and enemy == 'Orokin' and isHard:
                    print(obj['node'] + ' ' + obj['tier'] + ': ' + obj['eta'])
                    # print(obj[''])

    # file_path = "fissure.json"
    # with open(file_path, "w", encoding='gbk') as file:
        # json.dump(text, file, ensure_ascii=False, indent=4)
        # print(file_path)


if __name__ == "__main__":
    app = QApplication([])
    window = QWidget()
    window.show()

    reply_text = wsDataCenter.getJson("pc")
    
    data = json.loads(reply_text)

    fissures = data['fissures']
    # print(fissures)
    saveFile(fissures)
    

    sys.exit(app.exec())