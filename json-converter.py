import json
import pprint

with open('5e-SRD-Monsters.json', 'r') as file:
    data = json.load(file)

spellcasters = []

for item in data:
    if "special_abilities" in item.keys():
        for i in item["special_abilities"]:
            if i["name"] == "Spellcasting":
                monster = {"name": '', "spells": {}}
                print(item["name"])
                monster["name"] = item["name"]
                print(pprint.pformat(i))
                monster["spells"] = i
                spellcasters.append(monster)
            elif i["name"] == "Innate Spellcasting":
                monster = {"name": '', "spells": {}}
                print(item["name"])
                monster["name"] = item["name"]
                print(pprint.pformat(i))
                monster["spells"] = i
                spellcasters.append(monster)

with open('monster_spellcasters.json', 'w') as file:
    json.dump(spellcasters, file)