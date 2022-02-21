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
import main as maniac
import aaron as a

f = open('used.txt', 'r')
safa = f.read()
f.close
hara = True
sadge = maniac.main()
elim = sadge
sma = ''.join(sadge)
if safa == sma:
    hara = False
if hara:
    telegram_send.send(messages=[sma])
    a.main(sma)
f = open("used.txt", "w")
f.write(sma)
f.close
