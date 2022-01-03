# using https://github.com/nerrixDE/DSBApi
# install with "pip install dsbapipy" or "pip install git+https://github.com/nerrixDE/DSBApi.git#egg=dsbapipy"

import dsbapi

dsbclient = dsbapipy.DSBApi("243322", "HammerHai21")
entries = dsbclient.fetch_entries()

for s in range(len(entries)):
  for i in range(len(entries[s])):
    print(entries[s][i]["date"])