# using https://github.com/nerrixDE/DSBApi
# install with "pip install dsbapipy" or "pip install git+https://github.com/nerrixDE/DSBApi.git#egg=dsbapipy"

import dsbapi as dsb


ownFields = ['lesson','teacher','subject','room','type']
dsbclient = dsb.DSBApi("243322", "HammerHai21", tablemapper=ownFields)
entries = dsb.DSBApi.fetch_entries(dsbclient)

for s in range(len(entries)):
    print(entries[s])
