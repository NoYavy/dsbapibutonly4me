from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import main as fu
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
    dayvar = entries[0]
    day = dayvar['day']
    finall = []
    for s in range(len(entries)):
        step = entries[s]
        teach = step['Lehrer']
        teach = teach[:4]
        less = step['Stunde']
        entry = entries[s]
        typ = step['Typ']
        if buyvape.main(typ,day,teach,less):
            finall.append(buyvape.main(typ,day,teach,less))
            finall.append(" ")
    return finall

f = open('used.txt', 'r')
safa = f.read()
f.close
hara = True
sadge = main()
sad=''.join(sadge)
sma = sad
# if safa == sma:
#     hara = False
# if hara:
telegram_send.send(messages=[sma])
f = open("used.txt", "w")
f.write(sma)
f.close
