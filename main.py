# using https://github.com/nerrixDE/DSBApi
# install with "pip install git+https://github.com/nerrixDE/DSBApi.git#egg=dsbapipy"

import dsbapi as dsb
import time
import datetime
import buyvape


def main():
    days = ["Montag","Dienstag","Mittwoch","Donnerstag","Freitag", "Samstag","Sonntag"]
    klasse = "11c"
    ownFields = ['Stunde','Lehrer','Fach','Raum','Anmerkung','Typ']
    dsbclient = dsb.DSBApi("243322", "HammerHai21", tablemapper=ownFields)
    entries = dsb.DSBApi.fetch_entries(dsbclient)
    dayvar = entries[0]
    day = dayvar['day']
    finall = []
    print(len(entries))
    for s in range(len(entries)):
        step = entries[s]
        teach = step['Lehrer']
        teach = teach[:4]
        less = step['Stunde']
        entry = entries[s]
        typ = step['Typ']
        print(teach)
        print(less)
        if buyvape.main(typ,day,teach,less):
            finall.append(buyvape.main(typ,day,teach,less))
            finall.append(" ")
    try:
        return finall
    except:
        pass
