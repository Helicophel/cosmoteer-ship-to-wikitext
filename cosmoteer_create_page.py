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

    def set_crew(self, part_data):
        sum = 0
        self.data['crew'] = sum


if __name__ == "__main__":

    #fill these in before creating new ships
    faction_long = ""
    faction_short = ""
    type = ""
    classification = ""

    #template name
    template_name = "template.txt"
    
    for json_file in os.listdir("json"):
        #only open one file per ship
        if "data" in json_file:

            #open ship data
            with open(f'json/{json_file}', 'r') as f:
                ship_data = json.load(f)
            
            #open ship part data
            json_file_parts = json_file.replace("data", "parts")
            with open(f'json/{json_file_parts}', 'r') as f:
                part_data = json.load(f)

            #get ship name from filename
            name = json_file.split(".")[0]

            #create dataformat class of ship
            ship = dataformat(name, faction_short, type)

            #set values associated with parts 
            #incomplete
            #ship.set_crew(part_data)

            #set other values
            ship.set_faction(faction_long)
            ship.set_author(ship_data["Author"])
            ship.set_class(classification)

            #write to template files
            ship.write_to_template(template_name)
            
            print(name)

