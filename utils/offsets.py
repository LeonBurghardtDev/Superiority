import requests
import json

print(requests.get("https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json").json())
