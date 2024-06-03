from urllib import request
import requests

# https://api.warframestat.us/{platform}
state_api = "https://api.warframestat.us/"

def getJson(str):
    reply = requests.get(state_api + str + '/zh')
    reply.encoding = 'utf-8'
    return reply.text