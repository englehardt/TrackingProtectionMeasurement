import json

with open('./shavar-prod-lists/disconnect-entitylist.json', 'r') as f:
    dc = json.load(f)

out = dict()
collapsed = set()
for org in dc.keys():
    for url in dc[org]['properties']:
        out[url] = dc[org]['resources']
with open('./disconnect_entity.json', 'w') as f:
    json.dump(out, f)
