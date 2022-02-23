# using https://github.com/nerrixDE/DSBApi
# install with "pip install git+https://github.com/nerrixDE/DSBApi.git#egg=dsbapipy"
import json
import dsbapi as dsb
import datetime
import requests
import buyvape
import configparser

jon = '''

'''
url = 'https://discord.com/api/webhooks/945314444282585099/GaFrg1A7-YfE1hz04L_90uuIv3tbgP5mnShcHBxdWO8FeFNX' \
      '-osJeZUI7LKk9zMBlbAw '
message = "t"
f = open('used.txt', 'r')
u = f.read()
f.close()
if u == message:
    used = True
# needed fields
days = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
dayindex = daylist.index(days)
klasse = "11c"
ownFields = ['Stunde', 'Lehrer', 'Fach', 'Raum', 'Anmerkung', 'Typ']

dsbclient = dsb.DSBApi("243322", "HammerHai21", tablemapper=ownFields)
entries = dsb.DSBApi.fetch_entries(dsbclient)
print(len(entries))
dayvar = entries[0]
day = dayvar['day']
finall = []
print(entries)
for s in range(len(entries)):
    step = entries[s]
    teacha = step['Lehrer']
    teach = teacha[:4]
    less = step['Stunde']
    entry = entries[s]
    tap = step['Typ']
    fach = step['Fach']

data = json.loads(jon)
data['embeds'][0]['timestamp'] = datetime.datetime.utcnow().isoformat()
data['embeds'][0]['description'] = message
x = requests.post(url, json=data)
