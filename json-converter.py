import json
import pprint

with open('5e-SRD-Monsters.json', 'r') as file:
    data = json.load(file)

for item in data:
    if "special_abilities" in item.keys():
        for i in item["special_abilities"]:
            if i["name"] == "Spellcasting":
                print(item["name"])
                print(pprint.pformat(i))
            elif i["name"] == "Innate Spellcasting":
                print(item["name"])
                print(pprint.pformat(i))

