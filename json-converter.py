import json
import pprint

with open('5e-SRD-Monsters.json', 'r') as file:
    data = json.load(file)

spellcasters = []

def format_spells(input_str):
    """
    takes a description string of spells and returns a description of the spellcaster and a list of  in the following format:
    desc = "description"
    spells_by_level = [ {"cantrips (at will)": ['sacred flame', 'spare the dying', 'thaumaturgy']},
      {" 1st level (4 slots)": ['command', 'detect evil and good', 'detect magic']},
      {"2nd level (3 slots)": ['lesser restoration', 'zone of truth']}
    ]
    return desc, spells_by_level
    """
    desc, *spell_lines = input_str.split("\n")
    spell_lines = filter(None, spell_lines)
    spells_by_level = []

    for line in spell_lines:
        level, raw_spell_list = line.split(":")
        # get rid of bullet points at the front and any whitespace
        level = level[2:].strip()
        spell_list = raw_spell_list.split(",")
        # clean up whitespeace
        spell_list = [spell.strip() for spell in spell_list]
        spells_by_level.append({level: spell_list})

    return desc, spells_by_level

for item in data:
    if "special_abilities" in item.keys():
        for i in item["special_abilities"]:
            if i["name"] == "Spellcasting":
                monster = {"name": '', "desc": '', "spells_by_level": []}
                monster["name"] = item["name"]
                try: 
                    desc, spells_by_level = format_spells(i["desc"])
                    monster["desc"] = desc
                    monster["spells_by_level"] = spells_by_level
                    spellcasters.append(monster)
                except:
                    monster["desc"] = i["desc"]
                    spellcasters.append(monster)
                # print(i["desc"])
            elif i["name"] == "Innate Spellcasting":
                monster = {"name": '', "desc": '', "spells_by_level": []}
                monster["name"] = item["name"]
                try:
                    desc, spells_by_level = format_spells(i["desc"])
                    monster["desc"] = desc
                    monster["spells_by_level"] = spells_by_level
                    spellcasters.append(monster)
                except:
                    monster["desc"] = i["desc"]
                    spellcasters.append(monster)
                # print(i["desc"])

with open('monster_spellcasters.json', 'w') as file:
    json.dump(spellcasters, file, sort_keys=True, indent=4)