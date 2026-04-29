from jinja2 import Template
import os
import json

PART_DATA = {
    "cosmoteer.thruster_small_3way": {"command": -3, "cost": 1500, "mass": 1.9, },
    "cosmoteer.thruster_med": {"command": -2, "cost": 1500, "mass": 2.5, },
    "cosmoteer.thruster_small": {"command": -1, "cost": 500, "mass": 1.3, },
    "cosmoteer.thruster_large": {"command": -4, "cost": 4000, "mass": 5.0, },
    "cosmoteer.thruster_small_2way": {"command": -2, "cost": 1000, "mass": 1.6, },
    "cosmoteer.thruster_huge": {"command": -8, "cost": 10000, "mass": 11.0, },
    "cosmoteer.thruster_boost": {"command": -6, "cost": 6000, "mass": 8.9, },
    "cosmoteer.thruster_rocket_nozzle": {"command": -16, "cost": 15000, "mass": 14.4, },
    "cosmoteer.laser_blaster_small": {"command": -2, "cost": 2000, "mass": 2.5, },
    "cosmoteer.engine_room": {"command": -6, "cost": 12000, "mass": 9.0, },
    "cosmoteer.armor": {"command": 0, "cost": 200, "mass": 3.0, },
    "cosmoteer.laser_blaster_large": {"command": -4, "cost": 5000, "mass": 7.7, },
    "cosmoteer.armor_2x1": {"command": 0, "cost": 400, "mass": 6.0, },
    "cosmoteer.disruptor": {"command": -2, "cost": 3000, "mass": 3.5, },
    "cosmoteer.armor_1x3_wedge": {"command": 0, "cost": 300, "mass": 4.5, },
    "cosmoteer.armor_1x2_wedge": {"command": 0, "cost": 200, "mass": 3.0, },
    "cosmoteer.armor_wedge": {"command": 0, "cost": 100, "mass": 1.5, },
    "cosmoteer.ion_beam_emitter": {"command": 4, "cost": 10000, "mass": 8.0, },
    "cosmoteer.armor_tri": {"command": 0, "cost": 50, "mass": 0.8, },
    "cosmoteer.ion_beam_prism": {"command": -2, "cost": 5000, "mass": 7.7, },
    "cosmoteer.structure_wedge": {"command": 0, "cost": 25, "mass": 0.15, },
    "cosmoteer.structure": {"command": 0, "cost": 50, "mass": 0.3, },
    "cosmoteer.crew_quarters_large": {"command": 0, "cost": 15600, "mass": 12.0, },
    "cosmoteer.chaingun_magazine": {"command": 0, "cost": 1000, "mass": 2.0, },
    "cosmoteer.resonance_beam_turret": {"command": -8, "cost": 16000, "mass": 21.5, },
    "cosmoteer.structure_1x2_wedge": {"command": 0, "cost": 50, "mass": 0.3, },
    "cosmoteer.hyperdrive_large": {"command": 0, "cost": 34000, "mass": 16.0, },
    "cosmoteer.chaingun": {"command": -6, "cost": 24000, "mass": 39.8, },
    "cosmoteer.structure_1x3_wedge": {"command": 0, "cost": 75, "mass": 0.45, },
    "cosmoteer.crew_quarters_med": {"command": 0, "cost": 4200, "mass": 4.0, },
    "cosmoteer.structure_tri": {"command": 0, "cost": 25, "mass": 0.15, },
    "cosmoteer.armor_structure_hybrid_1x1": {"command": 0, "cost": 125, "mass": 1.5, },
    "cosmoteer.crew_quarters_small": {"command": 0, "cost": 1600, "mass": 2.0, },
    "cosmoteer.thermal_dilation_pump": {"command": -2, "cost": 5000, "mass": 4.0, },
    "cosmoteer.hyperdrive_med": {"command": 0, "cost": 20000, "mass": 9.0, },
    "cosmoteer.airlock": {"command": 0, "cost": 600, "mass": 1.0, },
    "cosmoteer.armor_structure_hybrid_1x2": {"command": 0, "cost": 250, "mass": 3.0, },
    "cosmoteer.conveyor": {"command": 0, "cost": 200, "mass": 1.0, },
    "cosmoteer.thermal_amplification_pump": {"command": -1, "cost": 4500, "mass": 3.0, },
    "cosmoteer.armor_structure_hybrid_1x3": {"command": 0, "cost": 375, "mass": 4.5, },
    "cosmoteer.radiator": {"command": -5, "cost": 10000, "mass": 3.0, },
    "cosmoteer.armor_structure_hybrid_tri": {"command": 0, "cost": 75, "mass": 0.8, },
    "cosmoteer.hyperdrive_small": {"command": 0, "cost": 10000, "mass": 4.0, },
    "cosmoteer.point_defense": {"command": -1, "cost": 1000, "mass": 1.2, },
    "cosmoteer.thruster_rocket_extender": {"command": 0, "cost": 6000, "mass": 6.0, },
    "cosmoteer.thruster_rocket_battery": {"command": 0, "cost": 1500, "mass": 2.0, },
    "cosmoteer.mining_laser_small": {"command": -3, "cost": 6000, "mass": 7.4, },
    "cosmoteer.control_room_large": {"command": 1000, "cost": 50000, "mass": 16.0, },
    "cosmoteer.control_room_med": {"command": 250, "cost": 25000, "mass": 9.0, },
    "cosmoteer.cannon_med": {"command": -2, "cost": 2000, "mass": 4.4, },
    "cosmoteer.control_room_small": {"command": 50, "cost": 10000, "mass": 4.0, },
    "cosmoteer.cannon_large": {"command": -4, "cost": 5000, "mass": 12.3, },
    "cosmoteer.reactor_small": {"command": 0, "cost": 25000, "mass": 4.0, },
    "cosmoteer.reactor_med": {"command": 0, "cost": 50000, "mass": 9.0, },
    "cosmoteer.cannon_deck": {"command": -8, "cost": 20000, "mass": 27.1, },
    "cosmoteer.railgun_launcher": {"command": -1, "cost": 7500, "mass": 36.0, },
    "cosmoteer.railgun_accelerator": {"command": -1, "cost": 7500, "mass": 36.0, },
    "cosmoteer.railgun_loader": {"command": -4, "cost": 12500, "mass": 24.0, },
    "cosmoteer.reactor_large": {"command": 0, "cost": 75000, "mass": 16.0, },
    "cosmoteer.missile_launcher": {"command": -5, "cost": 10000, "mass": 8.0, },
    "cosmoteer.heat_pipe_crossing": {"command": 0, "cost": 300, "mass": 1.0, },
    "cosmoteer.heat_pipe_adaptive": {"command": 0, "cost": 300, "mass": 1.0, },
    "cosmoteer.factory_he": {"command": -1, "cost": 15000, "mass": 9.0, },
    "cosmoteer.thermal_battery": {"command": 0, "cost": 2500, "mass": 4.0, },
    "cosmoteer.heat_pipe_adaptive_structure": {"command": 0, "cost": 300, "mass": 1.0, },
    "cosmoteer.power_storage": {"command": 0, "cost": 3000, "mass": 4.0, },
    "cosmoteer.heat_exchanger": {"command": 0, "cost": 500, "mass": 1.0, },
    "cosmoteer.shield_gen_small": {"command": -3, "cost": 5000, "mass": 6.0, },
    "cosmoteer.fire_extinguisher": {"command": 0, "cost": 300, "mass": 1.0, },
    "cosmoteer.factory_emp": {"command": -1, "cost": 20000, "mass": 12.0, },
    "cosmoteer.shield_gen_large": {"command": -6, "cost": 20000, "mass": 12.6, },
    "cosmoteer.storage_4x4": {"command": 0, "cost": 4800, "mass": 16.0, },
    "cosmoteer.factory_thermal": {"command": -1, "cost": 18000, "mass": 9.0, },
    "cosmoteer.storage_3x3": {"command": 0, "cost": 2700, "mass": 9.0, },
    "cosmoteer.factory_uranium": {"command": -1, "cost": 90000, "mass": 12.0, },
    "cosmoteer.storage_2x2": {"command": 0, "cost": 1200, "mass": 4.0, },
    "cosmoteer.factory_nuke": {"command": -1, "cost": 25000, "mass": 16.0, },
    "cosmoteer.storage_3x2": {"command": 0, "cost": 1800, "mass": 6.0, },
    "cosmoteer.storage_4x3": {"command": 0, "cost": 3600, "mass": 12.0, },
    "cosmoteer.roof_headlight": {"command": 0, "cost": 200, "mass": 1.0, },
    "cosmoteer.roof_light": {"command": 0, "cost": 200, "mass": 1.0, },
    "cosmoteer.explosive_charge": {"command": 0, "cost": 600, "mass": 1.0, },
    "cosmoteer.manipulator_beam_emitter": {"command": -4, "cost": 3000, "mass": 4.0, },
    "cosmoteer.factory_processor": {"command": -1, "cost": 80000, "mass": 9.0, },
    "cosmoteer.tractor_beam_emitter": {"command": -8, "cost": 40000, "mass": 32.1, },
    "cosmoteer.factory_mine": {"command": -1, "cost": 20000, "mass": 12.0, },
    "cosmoteer.factory_diamond": {"command": -1, "cost": 50000, "mass": 12.0, },
    "cosmoteer.factory_tristeel": {"command": -1, "cost": 65000, "mass": 16.0, },
    "cosmoteer.sensor_array": {"command": -8, "cost": 20000, "mass": 11.5, },
    "cosmoteer.factory_steel": {"command": -1, "cost": 30000, "mass": 16.0, },
    "cosmoteer.factory_coil2": {"command": -1, "cost": 50000, "mass": 12.0, },
    "cosmoteer.factory_coil": {"command": -1, "cost": 30000, "mass": 9.0, },
    "cosmoteer.factory_ammo": {"command": -1, "cost": 4000, "mass": 4.0, },
    "cosmoteer.hyperdrive_beacon": {"command": -12, "cost": 40000, "mass": 17.1, },
    "cosmoteer.flak_cannon_large": {"command": -6, "cost": 12000, "mass": 16.8, },
    "cosmoteer.corridor": {"command": 0, "cost": 100, "mass": 1.0, },
    "cosmoteer.door": {"command":0, "cost":100, "mass": 0},
}

SHIP_TYPES = {
    "Scouts": "Scout",
    "Patrolships": "Patrol Ship",
    "Corvettes": "Corvette",
    "Frigates": "Frigate",
    "Destroyers": "Destroyer",
    "Cruisers": "Cruiser",
    "Battleships": "Battleship",
    "Battlecruisers": "Battlecruiser",
    "Flagships": "Flagship",
    "Tradeships": "Trade Ship",
    "Crewtransports": "Crew Transport"
}
class dataformat():
    
    def __init__(self):
        self.cost = 0
        self.power = 0
        self.mass = 0
        self.command_total = 0
        self.command_used = 0
        self.crew = 0
        self.data = {
            "shipfile": "None",
            "shipfileinterior": "None",
            "shipfileblueprint": "None",
            "name": "None",
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
            "description": "None",
            "difficulty": "None"
        }

    def write_to_template(self, template_name):
        with open(template_name) as f:
            tmpl = Template(f.read(), variable_start_string='((', variable_end_string='))')
        
        with open(f'wikitext/{self.name}wikitext.txt', "w", encoding="utf-8") as f:
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

    def set_description(self, description_data):
        #done this way since some ships lack descriptions
        if description_data:
            self.data['description'] = "{{Quote|{" + description_data + "}}}"
        else:
            self.data['description'] = ""

    def set_filenames(self, name, faction, type, extension):
        self.name = name
        self.faction = faction
        self.data["name"] = name
        self.data["type"] = type
        self.data["faction"] = faction
        self.data["shipfile"] = f'Ship{faction}{type}{name}{extension}'
        self.data["shipfileinterior"] = f'Ship{faction}{type}{name}Interior{extension}'
        self.data["shipfileblueprint"] = f'Ship{faction}{type}{name}Blueprint{extension}'

    def set_tier(self, tier):
        self.data["tier"] = tier

    def set_difficulty(self, difficulty):
        self.data["difficulty"] = difficulty

    def ship_sum_parts(self, part_data):
        for i in part_data:
            part = i["ID"]
            if part in PART_DATA:
                stats = PART_DATA[part]
                self.command_used += stats["command"]
                self.cost += stats["cost"]
                self.mass += stats["mass"]
            if (part == "cosmoteer.crew_quarters_small"):
                self.crew += 2
            elif (part == "cosmoteer.crew_quarters_med"):
                self.crew += 6
            elif (part == "cosmoteer.crew_quarters_large"):
                self.crew += 24
            elif (part == "cosmoteer.control_room_small"):
                self.command_total += stats["command"]
            elif (part == "cosmoteer.control_room_med"):
                self.command_total += stats["command"]
            elif (part == "cosmoteer.control_room_large"):
                self.command_total += stats["command"]
            elif (part == "cosmoteer.reactor_small"):
                self.power += 1.5
            elif (part == "cosmoteer.reactor_med"):
                self.power += 4.5
            elif (part == "cosmoteer.reactor_large"):
                self.power += 13.5
            
        self.data["power"] = self.power
        self.data["command_total"] = self.command_total
        self.data['command_used'] = abs(self.command_used - self.command_total)
        self.data["cost"] = round(self.cost)
        self.data["mass"] = "{:.2f}".format(self.mass)
        self.data["crew"] = round(self.crew)

def process_rules():

    with open(f'png/{file}', "r") as f:
        #get rules file, split into lines for processing
        ship_dict = dict()
        rule_info = f.readlines()
        faction_short = (rule_info[0].replace("Faction = ", "")).capitalize().strip("\n")
        type_rule = rule_info[1]
        type = type_rule.strip("[]").capitalize().strip("\n")

        for i in rule_info[3:]:
            ship = i.replace("//", "").replace("\n", "").replace(":~/Tags", "=").replace(":~", "").replace(";", ",").replace(" ", "").replace("{", "").replace("}", "").replace("[", '"').replace("]", '"').replace("\t", "").replace('""', '"')
            if ship in SHIP_TYPES:
                classification = SHIP_TYPES[ship]
            elif len(ship) > 1 and ship != "Ships":
                ship_stats = eval(f"dict({ship})")
                ship_name = ship_stats["File"].replace(".ship.png", "")
                if "Difficulty" in ship_stats:
                    difficulty = ship_stats["Difficulty"]
                ship_dict[ship_name] = (ship_stats["Tier"], classification, difficulty) 

    return faction_short, type, ship_dict
        


def decide_faction_name(faction_short):
    if faction_short == "Io":
        return "Great House Io"
    elif faction_short == "Cabal":
        return "Cabal of Sol"
    else:
        return faction_short


if __name__ == "__main__":

    #fill these in before creating new ship documents
    extension = ".webp" #sometimes it's .png, make sure to check the wiki images
    faction_short = ""
    faction_long = ""
    
    rules_found = False

    if len(os.listdir("png")) == 0:
        raise FileNotFoundError("No files in /png folder to process")

    #Process rules file
    for file in os.listdir("png"):
        if ".rules" in file:
            faction_short, type, ship_dict = process_rules()
            rules_found = True
    
    if rules_found == False:
        raise FileNotFoundError(".rules file not found in /png")

    faction_long = decide_faction_name(faction_short)
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
            ship = dataformat()

            #get classification and tier
            tier, classification, difficulty = ship_dict[name]

            #set values associated with parts 
            ship.ship_sum_parts(part_data)

            #set other values. Filenames first
            ship.set_filenames(name, faction_short, type, extension)
            ship.set_faction(faction_long)
            ship.set_author(ship_data["Author"])
            ship.set_description(ship_data["Description"])

            ship.set_tier(tier)
            ship.set_class(classification)
            ship.set_difficulty(difficulty)


            #write to template files
            ship.write_to_template(template_name)
            