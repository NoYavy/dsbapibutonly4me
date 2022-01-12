import dsbapi

ownFields = ['Stunde','Lehrer','Fach','Raum','Anmerkung','Typ']

dsbclient = dsbapi.DSBApi("243322", "HammerHai21", tablemapper=ownFields)
entries = dsbclient.fetch_entries()

for s in range(len(entries)):
    print(entries[s])
