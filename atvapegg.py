#from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import telegram_send
import time
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
    if len(entries) < 1:
        entries = entries[0]
    dayvar = entries[0]
    day = dayvar['day']
    print(entries)
    finall = []
    for s in range(len(entries)):
        step = entries[s]
        teacha = step['Lehrer']
        teach = teacha[:4]
        less = step['Stunde']
        entry = entries[s]
        tap = step['Typ']
        fach = step['Fach']
        if tap == "Vertretung":
            etea = teacha[5:]
            lass = fach[:3]
            eles = fach[4:]
            fach = lass
        else:
            etea = ""
            eles = ""
        print(etea)
        if buyvape.main(tap,day,teach,less,fach,etea,eles) and buyvape.main(tap,day,teach,less,fach,etea,eles) not in finall:
            finall.append(buyvape.main(tap,day,teach,less,fach,etea,eles))
            finall.append("\n")
    print(finall)
    return finall

f = open('used.txt', 'r')
safa = f.read()
f.close
hara = True
sadge = main()
elim = sadge
sma = ''.join(sadge)
if safa == sma:
    hara = False
if hara:
    telegram_send.send(messages=[sma])
f = open("used.txt", "w")
f.write(sma)
f.close
