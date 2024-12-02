# Object classes from AP that represent different types of options that you can create
from Options import FreeText, NumericOption, Toggle, DefaultOnToggle, OptionSet, Choice, TextChoice, Range, NamedRange, OptionList, Visibility

# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value



####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#

class LinearLogic(DefaultOnToggle):
    """Disable to play with non-linear logic."""
    display_name = "LinearLogic"

class Courses(OptionSet):
    """
    List which courses you own/want to play.
    
    Enter the course acronym for each coarse. (ex:TT=Tourist Trap)
    """
    display_name = "Courses"
    default = ["TT", "CB"]
    valid_keys = ["TT", "CB", "SS", "AM", "OG", "TS", "BB", "QV", "GB", "SL", "SW", "ED", "LB", "20", "MY", 
                  "AT", "UT", "ZZ", "JC", "LL", "AL", "WW", "MW", "AW", "IL", "VN", "WG", "MG", "8B", "HH"]



# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict) -> dict:
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: dict) -> dict:
    options.update({
        'linear_logic': LinearLogic,
        'courses': Courses
    })
    return options