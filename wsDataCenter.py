import requests
import json

# https://api.warframestat.us/{platform}
state_api = "https://api.warframestat.us/"

def getAllData(str):
    reply = requests.get(state_api + str + '/zh')
    reply.encoding = 'utf-8'
    return reply.text

# [
#     {
#         "id": "66589471179db9eed24c3bbd",
#         "activation": "2024-05-30T15:00:01.751Z",
#         "startString": "-1h 47m 8s",
#         "expiry": "2024-05-30T16:56:25.935Z",
#         "active": true,
#         "node": "Taveuni (Kuva \u8981\u585e)",
#         "missionType": "\u751f\u5b58",
#         "missionKey": "Survival",
#         "enemy": "Grineer",
#         "enemyKey": "Grineer",
#         "nodeKey": "Taveuni (Kuva Fortress)",
#         "tier": "\u5b89\u9b42",
#         "tierNum": 5,
#         "expired": false,
#         "eta": "9m 15s",
#         "isStorm": false,
#         "isHard": true
#     },
# ]
def getFissureData(data: list[dict[str,str]]):
        for obj in data:
            type = obj['missionKey']
            enemy = obj['enemyKey']
            isHard = obj['isHard']
            # if type == 'Survival' and enemy == 'Orokin' and isHard:
            print(obj['node'] + ' ' + obj['tier'] + ': ' + obj['eta'])