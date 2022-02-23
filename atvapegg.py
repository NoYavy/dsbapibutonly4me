import requests
import json
import main as fu
import time
import dsbapi as dsb
import time
import datetime
import buyvape
import main as maniac

f = open('/home/noyavy/dsbapibutonly4me/used.txt', 'r')
safa = f.read()
f.close
hara = True
jon = '''
{
  "content": null,
  "embeds": [
    {
      "title": ":green_circle: News",
      "description": "h",
      "color": 4714574,
      "footer": {
        "text": "News"
      },
      "timestamp": "2020-06-14T15:12:00.000Z"
    }
  ],
  "avatar_url": "https://is5-ssl.mzstatic.com/image/thumb/Purple113/v4/a7/59/e1/a759e148-6e66-d438-0637-6a1b76ae255b/source/200x200bb.jpg"
}

'''
url = 'https://discord.com/api/webhooks/945314444282585099/GaFrg1A7-YfE1hz04L_90uuIv3tbgP5mnShcHBxdWO8FeFNX-osJeZUI7LKk9zMBlbAw'
sadge = maniac.main()
elim = sadge
sma = ''.join(sadge)
if safa == sma:
    hara = False
if hara:
    data = json.loads(jon)
    data['embeds'][0]['timestamp'] = datetime.datetime.utcnow().isoformat()
    data['embeds'][0]['description'] = sma
    x = requests.post(url, json = data)
f = open("/home/noyavy/dsbapibutonly4me/used.txt", "w")
f.write(sma)
f.close
