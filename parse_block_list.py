import json
import sys

include_content = len(sys.argv) > 1 and sys.argv[1] == 'content'

with open('./shavar-prod-lists/disconnect-blacklist.json', 'r') as f:
    dc = json.load(f)

count = 0
collapsed = set()
for cat in dc['categories'].keys():
    if not include_content and cat.lower() == 'content':
        print("Skipping %s" % cat)
        continue
    count = 0
    for item in dc['categories'][cat]:
        if len(item) > 1:
            print(item)
        for org, urls in item.items():
            for url, domains in urls.items():
                for domain in domains:
                    collapsed.add(domain)
                    count += 1
    print("Added %i domains for category %s" % (count, cat))

print("Total number of domains in list: %i" % len(collapsed))
outname = './disconnect_domains_content.json' if include_content else './disconnect_domains.json'
with open(outname, 'w') as f:
    json.dump(list(collapsed), f)
