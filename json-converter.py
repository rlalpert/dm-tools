import json
import pprint

with open('5e-SRD-Monsters.json', 'r') as file:
    data = json.load(file)

for item in data:
    if "special_abilities" in item.keys():
        print(item["name"])
        for i in item["special_abilities"]:
            print(pprint.pformat(i))
