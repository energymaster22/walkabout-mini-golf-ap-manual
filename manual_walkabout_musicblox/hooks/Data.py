import re
from .functions import get_courses
# called after the game.json file has been loaded
def after_load_game_file(game_table: dict) -> dict:
    return game_table
# called after the items.json file has been loaded, before any item loading or processing has occurred
# if you need access to the items after processing to add ids, etc., you should use the hooks in World.py
def after_load_item_file(item_table: list) -> list:
    return item_table

# NOTE: Progressive items are not currently supported in Manual. Once they are,
#       this hook will provide the ability to meaningfully change those.
def after_load_progressive_item_file(progressive_item_table: list) -> list:
    return progressive_item_table

# called after the locations.json file has been loaded, before any location loading or processing has occurred
# if you need access to the locations after processing to add ids, etc., you should use the hooks in World.py
def after_load_location_file(location_table: list) -> list:
    courses = get_courses()
    for course in courses:
        #Check if the course is enabled via the yaml, otherwise don't put it in the world. Replace True with the proper check when implemented into YAML
        if(True):
            name = course[1]
            abbreviation = course[0]
            branchCount = course[38]
            pendingJson = []
            pendingHardJson = []
            pendingBallJson = []

            strokeMinMax = 0
            strokeMinMaxHard = 0
            
            for i in range(18):
                if (strokeMinMax < course[i + 2]):
                    strokeMinMax = course[i + 2]
                if (strokeMinMaxHard < course[i + 20]):
                    strokeMinMaxHard = course[i + 20]
                #Add hole and lost ball checks
                pendingJson.append(
                    {
                        "name": f"{abbreviation}E Hole {i + 1}",
                        "region": f"{name}",
                        "category": [f"{name} Holes"],
                        "requires": f"|{name} Course| AND (({{YamlDisabled(linear_logic)}} AND |{abbreviation}E Progressive Stroke Limit:{course[i + 2]}|) OR ({{YamlEnabled(linear_logic)}} AND |{abbreviation}E Progressive Stroke Limit:{strokeMinMax}|))"
                    }
                )
                pendingHardJson.append(
                    {
                        "name": f"{abbreviation}H Hole {i + 1}",
                        "region": f"{name} Hard",
                        "category": [f"{name} Hard Holes"],
                        "requires": f"|{name} Course| AND (({{YamlDisabled(linear_logic)}} AND |{abbreviation}H Progressive Stroke Limit:{course[i + 2]}|) OR ({{YamlEnabled(linear_logic)}} AND |{abbreviation}H Progressive Stroke Limit:{strokeMinMaxHard}|))"
                    }
                )
                pendingBallJson.append(
                    {
                        "name": f"{abbreviation}E Ball {i + 1}",
                        "region": f"{name}",
                        "category": [f"{name} Lost Balls"],
                        "requires": f"|{name} Course|"
                    }
                )
            location_table.extend(pendingJson)
            location_table.extend(pendingHardJson)
            location_table.extend(pendingBallJson)

            pendingJson = []

            for i in range (branchCount):
                pass #Splice foxhunt clue branch into its components, then add foxhunt checks
            location_table.extend(pendingJson)
        else:
            pass
    return location_table

# called after the locations.json file has been loaded, before any location loading or processing has occurred
# if you need access to the locations after processing to add ids, etc., you should use the hooks in World.py
def after_load_region_file(region_table: dict) -> dict:
    return region_table

# called after the categories.json file has been loaded
def after_load_category_file(category_table: dict) -> dict:
    return category_table

# called after the meta.json file has been loaded and just before the properties of the apworld are defined. You can use this hook to change what is displayed on the webhost
# for more info check https://github.com/ArchipelagoMW/Archipelago/blob/main/docs/world%20api.md#webworld-class
def after_load_meta_file(meta_table: dict) -> dict:
    return meta_table

# called when an external tool (eg Univeral Tracker) ask for slot data to be read
# use this if you want to restore more data
# return True if you want to trigger a regeneration if you changed anything
def hook_interpret_slot_data(world, player: int, slot_data: dict[str, any]) -> bool:
    return False
