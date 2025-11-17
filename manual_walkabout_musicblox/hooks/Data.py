import re
import json
from .functions import get_courses
from .functions import check_course_active
# called after the game.json file has been loaded
def after_load_game_file(game_table: dict) -> dict:
    return game_table
# called after the items.json file has been loaded, before any item loading or processing has occurred
# if you need access to the items after processing to add ids, etc., you should use the hooks in World.py
def after_load_item_file(item_table: list) -> list:
    courses = get_courses()
    for course in courses:
        #Check if the course is enabled via the yaml, otherwise don't put it in the world.
        if(check_course_active()):
            name = course[1].strip()
            abbreviation = course[0].strip()
            pendingJson = []
            pendingHardJson = []
            pendingLimitJson = []
            pendingLimitHardJson = []
            pendingClubJson = []
            pendingBallJson = []
            pendingScoreJson = []
            pendingHardScoreJson = []

            pendingJson.append(
                {
                    "count": 1,
                    "name": f"{name} Course",
                    "category": [
                    f"{abbreviation}",
                    f"{name}",
                    "Courses"
                    ],
                    "progression": True
                }
            )
            pendingBallJson.append(
                 {
                    "count": "18",
                    "name": f"{abbreviation}E Lost Ball",
                    "category": [
                    f"{abbreviation}",
                    "Lost Balls"
                    ],
                    "progression": True
                },
            )
            pendingLimitJson.append(
                {
                    "count": "15",
                    "name": f"{abbreviation}E Progressive Stroke Limit",
                    "category": [
                    f"{abbreviation}",
                    f"{name}"
                    ],
                    "progression": True
                }
            )
            pendingHardJson.append(
                 {
                    "count": 1,
                    "name": f"{name} Hard Course",
                    "category": [
                    f"{abbreviation}",
                    f"{name}",
                    "Courses"
                    ],
                    "progression": True
                }
            )
            pendingLimitHardJson.append(
                {
                    "count": "15",
                    "name": f"{abbreviation}H Progressive Stroke Limit",
                    "category": [
                    f"{abbreviation}",
                    f"{name}"
                    ],
                    "progression": True
                }
            )
            pendingClubJson.append(
                {
                    "count": 1,
                    "name": f"{abbreviation}H Club",
                    "category": [
                    f"{abbreviation}"
                    ],
                    "filler": True
                },
            )
            pendingScoreJson.append(
                {
                    "count": 1,
                    "name": f"{abbreviation}E Scorecard",
                    "category": [
                    f"{abbreviation}"
                    "Scorecards"
                    ],
                    "progression": True
                }
            )
            pendingHardScoreJson.append(
                {
                    "count": 1,
                    "name": f"{abbreviation}H Scorecard",
                    "category": [
                    f"{abbreviation}",
                    "Scorecards"
                    ],
                    "progression": True
                }
            )
            
            item_table.extend(pendingJson)
            item_table.extend(pendingHardJson)
            item_table.extend(pendingLimitJson)
            item_table.extend(pendingLimitHardJson)
            item_table.extend(pendingClubJson)
            item_table.extend(pendingBallJson)
            item_table.extend(pendingScoreJson)
            item_table.extend(pendingHardScoreJson)

        else:
            pass
    return item_table

# NOTE: Progressive items are not currently supported in Manual. Once they are,
#       this hook will provide the ability to meaningfully change those.
def after_load_progressive_item_file(progressive_item_table: list) -> list:
    return progressive_item_table

# called after the locations.json file has been loaded, before any location loading or processing has occurred
# if you need access to the locations after processing to add ids, etc., you should use the hooks in World.py
def after_load_location_file(location_table: list) -> list:
    courses = get_courses()
    victoryCourseList = ""
    pendingVictoryJson = []
    for course in courses:
        #Check if the course is enabled via the yaml, otherwise don't put it in the world.
        if(check_course_active()):
            name = course[1].strip()
            abbreviation = course[0].strip()
            branchCount = int(course[38])
            pendingJson = []
            pendingHardJson = []
            pendingCompleteJson = []
            pendingHardCompleteJson = []
            pendingBallJson = []

            strokeMinMax = 0
            strokeMinMaxHard = 0

            victoryCourseList = victoryCourseList + f"|{abbreviation}E Scorecard| AND |{abbreviation}H Scorecard| AND "
            
            for i in range(18):
                if (int(strokeMinMax) < int(course[i + 2])):
                    strokeMinMax = course[i + 2]
                if (int(strokeMinMaxHard) < int(course[i + 20])):
                    strokeMinMaxHard = course[i + 20]
                #Add hole and lost ball checks
                pendingJson.append(
                    {
                        "name": f"{abbreviation}E Hole {i + 1}",
                        "region": f"{name}",
                        "category": [f"{abbreviation}", f"{name} Holes"],
                        "requires": f"|{name} Course| AND (({{YamlDisabled(linear_logic)}} AND |{abbreviation}E Progressive Stroke Limit:{course[i + 2]}|) OR ({{YamlEnabled(linear_logic)}} AND |{abbreviation}E Progressive Stroke Limit:{strokeMinMax}|))"
                    }
                )
                pendingHardJson.append(
                    {
                        "name": f"{abbreviation}H Hole {i + 1}",
                        "region": f"{name} Hard",
                        "category": [f"{abbreviation}", f"{name} Hard Holes"],
                        "requires": f"|{name} Course| AND (({{YamlDisabled(linear_logic)}} AND |{abbreviation}H Progressive Stroke Limit:{course[i + 2]}|) OR ({{YamlEnabled(linear_logic)}} AND |{abbreviation}H Progressive Stroke Limit:{strokeMinMaxHard}|))"
                    }
                )
                pendingBallJson.append(
                    {
                        "name": f"{abbreviation}E Ball {i + 1}",
                        "region": f"{name}",
                        "category": [f"{abbreviation}", f"{name} Lost Balls"],
                        "requires": f"|{name} Course|"
                    }
                )
            pendingCompleteJson.append(
                {
                    "name": f"{abbreviation}E Complete",
                    "category": [
                    f"{abbreviation}",
                    "Course Completion"
                    ],
                    "requires": [f"{abbreviation}E Progressive Stroke Limit:5"],
                    "place_item": [
                    f"{abbreviation}E Scorecard"
                    ]
                },
            )
            pendingHardCompleteJson.append(
                {
                    "name": f"{abbreviation}H Complete",
                    "category": [
                    f"{abbreviation}",
                    "Course Completion"
                    ],
                    "requires": [f"{abbreviation}H Progressive Stroke Limit:5"],
                    "place_item": [
                    f"{abbreviation}H Scorecard"
                    ]
                },
            )
            location_table.extend(pendingJson)
            location_table.extend(pendingHardJson)
            location_table.extend(pendingBallJson)
            location_table.extend(pendingCompleteJson)
            location_table.extend(pendingHardCompleteJson)

            pendingJson = []

            for i in range (branchCount): #Splice foxhunt clue branch into its components, then add foxhunt checks
                branch = re.split('(\d+)', course[i + 39])
                for j in range (int(branch[1])):
                    pendingJson.append(
                        {
                            "name": f"{(abbreviation + "H Clue " + str(j + 1)) if branch[0] == "SF" else branch[0] if int(branch[1]) == 1 else (branch[0] + " Clue " + str(j + 1))}",
                            "region": f"{name} Hard",
                            "category": [f"{abbreviation}", f"{name} Hard Foxhunt Clues"],
                            "requires": f"|{name} Course| AND |{abbreviation}E Lost Ball:10|"
                        }
                    )
                
            location_table.extend(pendingJson)
        else:
            pass

    pendingVictoryJson.append( 
        {
            "victory": True,
            "name": "All Courses Complete",
            "category": [
            "Goal"
            ],
            "requires": f"{(victoryCourseList[:-5] if len(victoryCourseList) > 4 else "")}"
        }
    )

    location_table.extend(pendingVictoryJson)

    return location_table

# called after the locations.json file has been loaded, before any location loading or processing has occurred
# if you need access to the locations after processing to add ids, etc., you should use the hooks in World.py
def after_load_region_file(region_table: dict) -> dict:
    courses = get_courses()
    courseList = []
    for course in courses:
        #Check if the course is enabled via the yaml, otherwise don't put it in the world. Replace True with the proper check when implemented into YAML
        if(True):
            name = course[1].strip()
            abbreviation = course[0].strip()

            courseList.append(name)
            
            pendingJson = []
            pendingHardJson = []

            region_table[f"{name}"] = {
                "connects_to": [f"{name} Hard"],
                "requires": f"|{name} Course|"
            }
            region_table[f"{name} Hard"] = {
                "connects_to": [],
                "requires": f"|{name} Course| AND |{abbreviation}E Lost Ball:10|"
            }            
        else:
            pass
    region_table["The Shack"] = {
        "starting": True,
        "connects_to": courseList,
        "requires": []
    }
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
