# using https://github.com/nerrixDE/DSBApi
# install with "pip install git+https://github.com/nerrixDE/DSBApi.git#egg=dsbapipy"

import dsbapi as dsb
import time
import datetime
import buyvape

days = ["Montag","Dienstag","Mittwoch","Donnerstag","Freitag", "Samstag","Sonntag"]
klasse = "11c"
ownFields = ['Stunde','Lehrer','Fach','Raum','Anmerkung','Typ']
dsbclient = dsb.DSBApi("243322", "HammerHai21", tablemapper=ownFields)
entries = dsb.DSBApi.fetch_entries(dsbclient)

while True:
    dayvar = entries[0]
    day = dayvar['day']
    for s in range(len(entries)):
        step = entries[s]
        teach = step['Lehrer']
        teach = teach[0:4]
        less = step['Stunde']
        entry = entries[s]
        buyvape.main(day,entry,teach,less)
    time.sleep(600)
