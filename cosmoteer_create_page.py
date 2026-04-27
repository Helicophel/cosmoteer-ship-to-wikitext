from jinja2 import Template
import os
import json



class dataformat():
    
    def __init__(self, name, faction="None", type="None"):
        self.name = name
        self.data = {
            "shipfile": f'Ship{faction}{type}{name}.webp',
            "shipfileinterior": f'Ship{faction}{type}{name}Interior.webp',
            "shipfileblueprint": f'Ship{faction}{type}{name}Blueprint.webp',
            "author": "None",
            "faction": "None",
            "class": "None",
            "tier": "None",
            "type": "None",
            "cost": "None",
            "mass": "None",
            "efficiency": "None",
            "crew": "None",
            "crew_suggest": "None",
            "power": "None",
            "power_suggested": "None",
            "command_used": "None",
            "command_total": "None",
            "quote": "None"
        }

    def write_to_template(self, template_name):
        with open(template_name) as f:
            tmpl = Template(f.read(), variable_start_string='((', variable_end_string='))')
        
        with open(f'{self.name}wikitext.txt', "w") as f:
            file_data = tmpl.render(self.data)
            f.write(file_data)

    def set_author(self, author):
        self.data["author"] = author

    def set_faction(self, faction_name):
        self.data['faction'] = faction_name

    def set_type(self, ship_type):
        self.data['type'] = ship_type

    def set_class(self, ship_class):
        self.data['class'] = ship_class


if __name__ == "__main__":

    faction_long = "Cabal of Sol"
    faction_short = "Cabal"
    type = "Civilian"
    template_name = "template.txt"
    classification = "Trade"
    
    for json_file in os.listdir("json"):

        if "-data" in json_file:

            with open(f'json/{json_file}', 'r') as f:
                ship_data = json.load(f)

            name = json_file.split(".")[0]

            ship = dataformat(name, faction_short, type)

            ship.set_faction(faction_long)
            ship.set_author(ship_data["Author"])
            ship.set_type(type)
            ship.set_class(classification)

            ship.write_to_template(template_name)
            
            print(name)

