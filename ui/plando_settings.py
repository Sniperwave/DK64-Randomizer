"""Methods to handle plando settings importing and exporting."""

from randomizer.Enums.Kongs import Kongs
from randomizer.Enums.Locations import Locations
from randomizer.Enums.Levels import Levels
from randomizer.Enums.Minigames import Minigames
from randomizer.Enums.Plandomizer import PlandoItems
from randomizer.Lists.CustomLocations import CustomLocations
from randomizer.Lists.FairyLocations import fairy_locations
from randomizer.Lists.KasplatLocations import KasplatLocationList
from randomizer.Lists.Location import LocationListOriginal as LocationList
from randomizer.Lists.Plandomizer import KasplatLocationEnumList

import js
import json
from ui.bindings import bind
from ui.download import download_json_file
from ui.generate_buttons import export_settings_string, import_settings_string
from ui.plando_validation import (
    full_validate_no_reward_with_random_location,
    lock_key_8_in_helm,
    populate_plando_options,
    reset_plando_options_no_prompt,
    validate_custom_arena_locations,
    validate_custom_crate_locations,
    validate_custom_fairy_locations,
    validate_custom_kasplat_locations,
    validate_custom_locations_no_duplicates,
    validate_custom_patch_locations,
    validate_helm_order_no_duplicates,
    validate_hint_count,
    validate_hint_text,
    validate_item_limits,
    validate_krool_order_no_duplicates,
    validate_level_order_no_duplicates,
    validate_no_crate_items_with_shuffled_crates,
    validate_no_crown_items_with_shuffled_crowns,
    validate_no_dirt_items_with_shuffled_patches,
    validate_no_fairy_items_with_shuffled_fairies,
    validate_no_kasplat_items_with_location_shuffle,
    validate_shuffle_shops_no_conflict,
    validate_smaller_shops_no_conflict,
    validate_starting_kong_count,
    level_options,
    kong_options,
)
from ui.rando_options import (
    plando_disable_camera_shockwave,
    plando_disable_keys,
    plando_disable_kong_items,
    plando_hide_helm_options,
    plando_hide_krool_options,
    plando_toggle_custom_arena_locations,
    plando_toggle_custom_crate_locations,
    plando_toggle_custom_fairy_locations,
    plando_toggle_custom_kasplat_locations,
    plando_toggle_custom_locations_tab,
    plando_toggle_custom_patch_locations,
)


# Assemble sets of custom locations, for validation.
customLocationSet = set()
for level, locations in CustomLocations.items():
    for location in locations:
        fullLoc = f"{level.name}: {location.name}"
        customLocationSet.add(fullLoc)
customFairyLocationSet = set()
for level, locations in fairy_locations.items():
    for location in locations:
        fullLoc = f"{level.name}: {location.name}"
        customFairyLocationSet.add(fullLoc)
customKasplatLocationSet = set()
for _, locations in KasplatLocationList.items():
    for location in locations:
        customKasplatLocationSet.add(location.name)


@bind("click", "export_plando_string")
def export_plando_string(evt):
    """Generate the plando json string."""
    # Serialize the form into json
    form = js.jquery("#form").serializeArray()

    # Plandomizer data is processed separately.
    plando_form_data = populate_plando_options(form)
    js.plando_string.value = json.dumps(plando_form_data)


async def import_plando_options(jsonString):
    """Import plando settings from a provided JSON file."""
    fileContents = json.loads(jsonString)

    # Inform the user their current settings will be erased.
    if not js.window.confirm("This will replace your current plandomizer settings. Continue?"):
        return

    # First, ensure this is an actual valid plando file.
    validate_plando_file(fileContents)

    # Reset all of the plando options to their defaults.
    reset_plando_options_no_prompt()

    # We need to record all hints and shop costs so we can validate them later.
    hintList = []
    shopCostList = []

    if "Settings String" in fileContents.keys():
        js.settings_string.value = fileContents["Settings String"]
        import_settings_string(None)

    # Set all of the options specified in the plando file.
    for option, value in fileContents.items():
        # Ignore settings strings here, we're always processing that first.
        if option == "Settings String":
            continue
        # Process item locations.
        if option == "locations":
            for location, item in value.items():
                # These items represent custom Kasplat locations and are
                # handled later.
                if location not in KasplatLocationEnumList:
                    js.document.getElementById(f"plando_{location}_item").value = item
        # Process shop costs.
        elif option == "prices":
            for location, price in value.items():
                shopElem = js.document.getElementById(f"plando_{location}_shop_cost")
                shopCostList.append(shopElem)
                shopElem.value = price
        # Process minigame selections.
        elif option == "plando_bonus_barrels":
            for location, minigame in value.items():
                js.document.getElementById(f"plando_{location}_minigame").value = minigame
        # Process custom locations.
        elif option in ["plando_place_arenas", "plando_place_crates", "plando_place_fairies", "plando_place_kasplats", "plando_place_patches"]:
            js.document.getElementById(option).checked = value
        elif option == "plando_battle_arenas":
            for enumLocation, customLocation in value.items():
                locValue = "" if customLocation == "Randomize" else customLocation
                js.document.getElementById(f"plando_{enumLocation}_location").value = locValue
                if enumLocation in fileContents["locations"]:
                    reward = fileContents["locations"][enumLocation]
                    js.document.getElementById(f"plando_{enumLocation}_location_reward").value = reward
        elif option == "plando_dirt_patches":
            for i, dirtPatch in enumerate(value):
                locationValue = "" if dirtPatch["location"] == "Randomize" else f'{dirtPatch["level"]};{dirtPatch["location"]}'
                js.document.getElementById(f"plando_patch_{i}_location").value = locationValue
                reward = "" if dirtPatch["reward"] == "Randomize" else dirtPatch["reward"]
                js.document.getElementById(f"plando_patch_{i}_location_reward").value = reward
        elif option == "plando_fairies":
            for i, fairy in enumerate(value):
                locationValue = "" if fairy["location"] == "Randomize" else f'{fairy["level"]};{fairy["location"]}'
                js.document.getElementById(f"plando_fairy_{i}_location").value = locationValue
                reward = "" if fairy["reward"] == "Randomize" else fairy["reward"]
                js.document.getElementById(f"plando_fairy_{i}_location_reward").value = reward
        elif option == "plando_kasplats":
            for enumLocation, customLocation in value.items():
                locValue = "" if customLocation == "Randomize" else customLocation
                js.document.getElementById(f"plando_{enumLocation}_location").value = locValue
                if enumLocation in fileContents["locations"]:
                    reward = fileContents["locations"][enumLocation]
                    js.document.getElementById(f"plando_{enumLocation}_location_reward").value = reward
        elif option == "plando_melon_crates":
            for i, crate in enumerate(value):
                locationValue = "" if crate["location"] == "Randomize" else f'{crate["level"]};{crate["location"]}'
                js.document.getElementById(f"plando_crate_{i}_location").value = locationValue
                reward = "" if crate["reward"] == "Randomize" else crate["reward"]
                js.document.getElementById(f"plando_crate_{i}_location_reward").value = reward
        # Process hints.
        elif option == "hints":
            for location, hint in value.items():
                hintElem = js.document.getElementById(f"plando_{location}_hint")
                hintList.append(hintElem)
                hintElem.value = hint
        # Process this one multi-select.
        elif option == "plando_starting_kongs_selected":
            starting_kongs = set()
            for kong in value:
                starting_kongs.add("" if kong == "Randomize" else kong)
            kongs_element = js.document.getElementById("plando_starting_kongs_selected")
            for i in range(6):
                starting_option = kongs_element.options.item(i)
                starting_option.selected = starting_option.value in starting_kongs
        # Process all other options.
        else:
            final_value = "" if value == "Randomize" else value
            js.document.getElementById(option).value = final_value

    # Run validation functions.
    for hintLocation in hintList:
        validate_hint_text(hintLocation)
    # for shopLocation in shopCostList:
    #     validate_shop_costs(shopLocation)
    plando_disable_camera_shockwave(None)
    plando_disable_keys(None)
    plando_disable_kong_items(None)
    plando_hide_helm_options(None)
    plando_hide_krool_options(None)
    plando_toggle_custom_arena_locations(None)
    plando_toggle_custom_crate_locations(None)
    plando_toggle_custom_fairy_locations(None)
    plando_toggle_custom_kasplat_locations(None)
    plando_toggle_custom_patch_locations(None)
    plando_toggle_custom_locations_tab(None)
    lock_key_8_in_helm(None)
    validate_custom_arena_locations(None)
    validate_custom_crate_locations(None)
    validate_custom_fairy_locations(None)
    validate_custom_kasplat_locations(None)
    validate_custom_patch_locations(None)
    validate_custom_locations_no_duplicates(None)
    validate_hint_count(None)
    validate_smaller_shops_no_conflict(None)
    validate_shuffle_shops_no_conflict(None)
    validate_starting_kong_count(None)
    validate_level_order_no_duplicates(None)
    validate_krool_order_no_duplicates(None)
    validate_helm_order_no_duplicates(None)
    validate_no_crate_items_with_shuffled_crates(None)
    validate_no_crown_items_with_shuffled_crowns(None)
    validate_no_dirt_items_with_shuffled_patches(None)
    validate_no_fairy_items_with_shuffled_fairies(None)
    validate_no_kasplat_items_with_location_shuffle(None)
    full_validate_no_reward_with_random_location()
    validate_item_limits(None)
    js.savesettings()


def raise_plando_validation_error(err_string: str) -> None:
    """Raise an error and display a message about an invalid plando file."""
    plando_errors_element = js.document.getElementById("plando_import_errors")
    plando_errors_element.innerText = err_string
    plando_errors_element.style = ""
    raise ValueError(err_string)


def validate_plando_option_value(file_obj: dict, option: str, enum_type: type, field_type: str = "option") -> None:
    """Evaluate a given plando option to see if its value is valid.

    Args:
        file_obj (dict) - The object where the option can be found. Usually
            this is the entire plando file dictionary, but it may be a subset
            of it (i.e. only locations, or shop prices).
        option (str) - The name of the option being tested.
        enum_type (type) - The type of enum that we should attempt to convert
            the value to.
        field_type (str) - The type of field that has an invalid option. Only
            for error reporting purposes. E.g. "location", "minigame", "hint".
    """
    try:
        if option not in file_obj:
            return
        if file_obj[option] == "Randomize":
            return
        _ = enum_type[file_obj[option]]
    except KeyError:
        errString = f'The plandomizer file is invalid: {field_type} "{option}" has invalid value "{file_obj[option]}".'
        raise_plando_validation_error(errString)


def validate_plando_location(location_name: str) -> None:
    """Validate that a given plando location is valid."""
    try:
        _ = Locations[location_name]
    except KeyError:
        errString = f'The plandomizer file is invalid: "{location_name}" is not a valid location.'
        raise_plando_validation_error(errString)


def validate_custom_location(cust_location: dict, cust_set: set, loc_type: str) -> None:
    """Validate that a given custom location is valid.

    Args:
        cust_location (dict) - The object containing custom location data.
        cust_set (set) - The specific set where this location should be found.
        loc_type (str) - The kind of custom location, e.g. "dirt patch". Only
            used for logging errors.
    """
    for field in ["level", "location", "reward"]:
        if field not in cust_location:
            errString = f'The plandomizer file is invalid: a custom {loc_type} location is missing data field "{field}".'
            raise_plando_validation_error(errString)
    location = f'{cust_location["level"]}: {cust_location["location"]}'
    if location != "Randomize: Randomize" and location not in cust_set:
        errString = f'The plandomizer file is invalid: "{location}" is not a valid {loc_type} location.'
        raise_plando_validation_error(errString)
    reward = cust_location["reward"]
    if reward != "Randomize":
        try:
            _ = PlandoItems[reward]
        except KeyError:
            errString = f'The plandomizer file is invalid: custom {loc_type} location "{location}" has invalid reward "{reward}".'
            raise_plando_validation_error(errString)


def validate_custom_enum_location(enum_location: str, location_str: str, cust_set: set, loc_type: str) -> None:
    """Validate that a given enum-based custom location is valid.

    Args:
        enum_location (str) - The string name of the Location enum that this
            custom location is being assigned to.
        location_str (str) - The string representing the custom location.
        cust_set (set) - The specific set where this location should be found.
        loc_type (str) - The kind of custom location, e.g. "dirt patch". Only
            used for logging errors.
    """
    try:
        _ = Locations[enum_location]
    except KeyError:
        errString = f'The plandomizer file is invalid: "{enum_location}" is not a valid {loc_type} enum value.'
        raise_plando_validation_error(errString)
    if location_str not in cust_set:
        errString = f'The plandomizer file is invalid: "{location_str}" is not a valid {loc_type} location.'
        raise_plando_validation_error(errString)


def validate_fairy_position(fairy: dict, index: int) -> None:
    """Ensure fairies are assigned to the correct level."""
    fairyLevelIndexMap = {
        Levels.JungleJapes: 2,
        Levels.AngryAztec: 4,
        Levels.FranticFactory: 6,
        Levels.GloomyGalleon: 8,
        Levels.FungiForest: 10,
        Levels.CrystalCaves: 12,
        Levels.CreepyCastle: 14,
        Levels.DKIsles: 18,
        Levels.HideoutHelm: 20,
    }
    if fairy["level"] == "Randomize":
        return
    for level, i in fairyLevelIndexMap.items():
        if index < i:
            if fairy["level"] != level.name:
                errString = f'The plandomizer file is invalid: fairy {index+1} needs to be assigned to {level.name}, but is assigned to {fairy["level"]}.'
                raise_plando_validation_error(errString)
            return


def validate_plando_file(file_obj: dict) -> None:
    """Validate the contents of a given plando file."""
    # Hide the div for import errors.
    plando_errors_element = js.document.getElementById("plando_import_errors")
    plando_errors_element.style.display = "none"

    # validate_plando_option_value(file_obj, "plando_spawn_location", Locations)
    for starting_kong in file_obj["plando_starting_kongs_selected"]:
        if starting_kong != "Randomize":
            try:
                _ = Kongs[starting_kong]
            except KeyError as err:
                errString = f'The plandomizer file is invalid: option "plando_starting_kongs_selected" has invalid value "{starting_kong}".'
                raise_plando_validation_error(errString)
    # if file_obj["plando_101"] not in [True, False]:
    #     raise_plando_validation_error("plando_101", file_obj["plando_101"])
    for option in level_options:
        validate_plando_option_value(file_obj, option, Levels)
    for option in kong_options:
        validate_plando_option_value(file_obj, option, Kongs)

    # Inspect all item locations.
    for location in file_obj["locations"].keys():
        validate_plando_location(location)
        validate_plando_option_value(file_obj["locations"], location, PlandoItems, "location")
    # Inspect all minigames.
    for minigame in file_obj["plando_bonus_barrels"].keys():
        validate_plando_location(minigame)
        validate_plando_option_value(file_obj["plando_bonus_barrels"], minigame, Minigames, "minigame")
    # Inspect all shop prices.
    # for shop in file_obj["prices"].keys():
    #     validate_plando_location(shop)
    #     price = file_obj["prices"][shop]
    #     if not isinstance(price, int):
    #         errString = f'The plandomizer file is invalid: shop "{shop}" has invalid price "{price}".'
    #         raise_plando_validation_error(errString)
    # Inspect all custom locations.
    for patch in file_obj["plando_dirt_patches"]:
        validate_custom_location(patch, customLocationSet, "dirt patch")
    for crate in file_obj["plando_melon_crates"]:
        validate_custom_location(crate, customLocationSet, "melon crate")
    for i, fairy in enumerate(file_obj["plando_fairies"]):
        validate_custom_location(fairy, customFairyLocationSet, "fairy")
        validate_fairy_position(fairy, i)
    for arena, location in file_obj["plando_battle_arenas"].items():
        if location == "Randomize":
            continue
        try:
            level = LocationList[Locations[arena]].level.name
        except KeyError:
            errString = f'The plandomizer file is invalid: "{arena}" is not a valid battle arena enum value.'
            raise_plando_validation_error(errString)
        fullLocation = f"{level}: {location}"
        validate_custom_enum_location(arena, fullLocation, customLocationSet, "battle arena")
    for kasplat, location in file_obj["plando_kasplats"].items():
        if location == "Randomize":
            continue
        validate_custom_enum_location(kasplat, location, customKasplatLocationSet, "Kasplat")
    # Inspect all hints.
    for hint_location in file_obj["hints"].keys():
        validate_plando_location(hint_location)
        hint = file_obj["hints"][hint_location]
        if type(hint) is not str:
            errString = f'The plandomizer file is invalid: hint location "{hint_location}" has invalid hint "{hint}".'
            raise_plando_validation_error(errString)


@bind("click", "export_plando_settings")
def export_plando_options(evt):
    """Export the current plando settings to a JSON file."""
    form = js.jquery("#form").serializeArray()
    plandoData = populate_plando_options(form, True)
    export_settings_string(None)
    plandoData["Settings String"] = js.settings_string.value
    download_json_file(plandoData, "plando_settings.json")
