from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import main as main
import time
import telegram_send


def suckmyanus():
    sadge = main.main()
    sad=""
    for e in sadge:
        sad = sad+ e
    print(type(sad))
    return sad

while True:
    f = open('used.txt', 'r')
    safa = f.read()
    hara = True
    sma = suckmyanus()
    if safa == sma:
        hara = False
    if hara:
        telegram_send.send(messages=[sma])
    f = open("used.txt", "w")
    f.write(sma)
    f.close
    time.sleep(60)
