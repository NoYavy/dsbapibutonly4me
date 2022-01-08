# using https://github.com/nerrixDE/DSBApi
# install with "pip install git+https://github.com/nerrixDE/DSBApi.git#egg=dsbapipy"

import dsbapi as dsb
import time
import datetime


days = ["Montag","Dienstag","Mittwoch","Donnerstag","Freitag", "Samstag","Sonntag"]
klasse = "11c"
ownFields = ['Stunde','Lehrer','Fach','Raum','Anmerkung','Typ']
dsbclient = dsb.DSBApi("243322", "HammerHai21", tablemapper=ownFields)
entries = dsb.DSBApi.fetch_entries(dsbclient)

while True:
    dayvar = entries[0]
    day = dayvar['day']
    for s in range(len(entries)):
        if day == "Montag":
            step = entries[s]
            teach = step['Lehrer']
            less = step['Stunde']
            if teach == "MesD":
                if less == "2":
                    print("alarm")
                    print(entries[s])
            if teach == "ObeI":
                if less == "3" or less == "4" or less == "3 - 4":
                    print("alarm")
                    print(entries[s])
            if teach == ""
        print(entries[s])
    time.sleep(600)
