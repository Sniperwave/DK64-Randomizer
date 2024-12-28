"""All code associated with cosmetic tweaks to text."""

import random
from randomizer.Patching.Patcher import LocalROM
from randomizer.Patching.Lib import writeText, grabText

boot_phrases = (
    "Removing Lanky Kong",
    "Telling 2dos to play DK64",
    "Locking K. Lumsy in a cage",
    "Stealing the Banana Hoard",
    "Finishing the game in a cave",
    "Becoming the peak of randomizers",
    "Giving kops better eyesight",
    "Patching in the glitches",
    "Enhancing Cfox Luck",
    "Finding Rareware GB in Galleon",
    "Resurrecting Chunky Kong",
    "Shouting out Grant Kirkhope",
    "Crediting L. Godfrey",
    "Removing Stop n Swop",
    "Assembling the scraps",
    "Blowing in the cartridge",
    "Backflipping in Chunky Phase",
    "Hiding 20 fairies",
    "Randomizing collision normals",
    "Removing hit detection",
    "Compressing K Rools Voice Lines",
    "Checking divide by 0 doesnt work",
    "Adding every move to Isles",
    "Segueing in dk64randomizer.com",
    "Removing lag. Or am I?",
    "Hiding a dirt patch under grass",
    "Giving Wrinkly the spoiler log",
    "Questioning sub 2:30 in LUA Rando",
    "Chasing Lanky in Fungi Forest",
    "Banning Potions from Candys Shop",
    "Finding someone who can help you",
    "Messing up your seed",
    "Crashing Krem Isle",
    "Increasing Robot Punch Resistance",
    "Caffeinating banana fairies",
    "Bothering Beavers",
    "Inflating Banana Balloons",
    "Counting to 16",
    "Removing Walls",
    "Taking it to the fridge",
    "Brewing potions",
    "Reticulating Splines",  # SimCity 2000
    "Ironing Donks",
    "Replacing mentions of Hero with Hoard",
    "Suggesting you also try BK Randomizer",
    "Scattering 3500 Bananas",
    "Stealing ideas from other randomizers",
    "Fixing Krushas Collision",
    "Falling on 75m",
    "Summoning Salt",
    "Combing Chunkys Afro",
    "Asking what you gonna do",
    "Thinking with portals",
    "Reminding you to hydrate",
    "Injecting lag",
    "Turning Sentient",
    "Performing for you",
    "Charging 2 coins per save",
    "Loading in Beavers",
    "Lifting Boulders with Relative Ease",
    "Doing Monkey Science Probably",
    "Telling Killi to eventually play DK64",
    "Crediting Grant Kirkhope",
    "Dropping Crayons",
    "Saying Hello when others wont",
    "Mangling Music",
    "Killing Speedrunning",
    "Enhancing Cfox Luck Voice Linesmizers",
    "Enforcing the law of the Jungle",
    "Saving 20 frames",
    "Reporting bugs. Unlike some",
    "Color-coding Krusha for convenience",
)

crown_heads = (
    # Object
    "Arena",
    "Beaver",
    "Bish Bash",
    "Forest",
    "Kamikaze",
    "Kritter",
    "Pinnacle",
    "Plinth",
    "Shockwave",
    "Bean",
    "Dogadon",
    "Banana",
    "Squawks",
    "Lanky",
    "Diddy",
    "Tiny",
    "Chunky",
    "DK",
    "Krusha",
    "Kosha",
    "Klaptrap",
    "Zinger",
    "Gnawty",
    "Kasplat",
    "Pufftup",
    "Shuri",
    "Krossbones",
    "Caves",
    "Castle",
    "Helm",
    "Japes",
    "Jungle",
    "Angry",
    "Aztec",
    "Frantic",
    "Factory",
    "Gloomy",
    "Galleon",
    "Crystal",
    "Creepy",
    "Hideout",
    "Cranky",
    "Funky",
    "Candy",
    "Kong",
    "Monkey",
    "Amazing",
    "Incredible",
    "Ultimate",
    "Wrinkly",
    "Heroic",
    "Final",
    "Fantastic",
    "Krazy",
    "Komplete",
    "Unhinted",
    "Unstable",
    "Extreme",
    "Royal",
    "Monster",
    "Primate",
    "Baboon",
    "Walnut",
    "Peanut",
    "Coconut",
    "Feather",
    "Grape",
    "Pineapple",
    "Barrel",
    "Monkeyport",
    "Kalamity",
    "Kaboom",
    "Magic",
    "Fairy",
    "Karnivorous",
    "Krispy",
    "Kooky",
    "Cookin",
    "Klutz",
    "Kingdom",
    "Super Duper",
    "Rainbow",
    "Bongo",
    "Guitar",
    "Trombone",
    "Saxophone",
    "Triangle",
    "Dixie",
    "Gorilla",
    "Chimpy",
    "Museum",
    "Ballroom",
    "Winch",
    "Shipyard",
    "Hillside",
    "Oasis",
    "Arcade",
    "Mushroom",
    "Igloo",
    "Stupid",
    "Spicy",
    "Dizzy",
    "Slot Car",
    "Minecart",
    "Rambi",
    "Enguarde",
    "Reptile",
    "Bramble",
    "Toxic",
    "Rabbit",
    "Beetle",
    "Vulture",
    "Boulder",
)

crown_tails = (
    # Synonym for brawl/similar
    "Ambush",
    "Brawl",
    "Fracas",
    "Karnage",
    "Kremlings",
    "Palaver",
    "Panic",
    "Showdown",
    "Slam",
    "Melee",
    "Tussle",
    "Altercation",
    "Wrangle",
    "Clash",
    "Free for All",
    "Skirmish",
    "Scrap",
    "Fight",
    "Rumpus",
    "Fray",
    "Wrestle",
    "Brouhaha",
    "Commotion",
    "Uproar",
    "Rough and Tumble",
    "Broil",
    "Argy Bargy",
    "Bother",
    "Mayhem",
    "Bonanza",
    "Battle",
    "Kerfuffle",
    "Rumble",
    "Fisticuffs",
    "Ruckus",
    "Scrimmage",
    "Strife",
    "Dog and Duck",
    "Joust",
    "Scuffle",
    "Hootenanny",
    "Blitz",
    "Tourney",
    "Explosion",
    "Contest",
    "Chaos",
    "Combat",
    "Knockdown",
    "Demolition",
    "Capture",
    "Storm",
    "Earthquake",
    "Charge",
    "Tremor",
    "Trample",
    "Gauntlet",
    "Challenge",
    "Blowout",
    "Riot",
    "Buffoonery",
    "Hijinxs",
    "Frenzy",
    "Rampage",
    "Antics",
    "Trouble",
    "Revenge",
    "Klamber",
    "Wreckage",
    "Quarrel",
    "Feud",
    "Thwack",
    "Wallop",
    "Donnybrook",
    "Tangle",
    "Crossfire",
    "Royale",
)


def getCrownNames() -> list:
    """Get crown names from head and tail pools."""
    # Get 10 names for heads just in case "Forest" and "Fracas" show up
    heads = random.sample(crown_heads, 10)
    tails = random.sample(crown_tails, 9)
    # Remove "Forest" if both "Forest" and "Fracas" show up
    if "Forest" in heads and "Fracas" in tails:
        heads.remove("Forest")
    # Only get 9 names, Forest Fracas can't be overwritten without having negative impacts
    names = []
    for x in range(9):
        head = heads[x]
        tail = tails[x]
        if head[0] == "K" and tail[0] == "C":
            split_tail = list(tail)
            split_tail[0] = "K"
            tail = "".join(split_tail)
        names.append(f"{head} {tail}!".upper())
    names.append("Forest Fracas!".upper())
    return names


def writeCrownNames():
    """Write Crown Names to ROM."""
    names = getCrownNames()
    old_text = grabText(35, True)
    for name_index, name in enumerate(names):
        old_text[0x1E + name_index] = ({"text": [name]},)
    writeText(35, old_text, True)


def writeBootMessages() -> None:
    """Write boot messages into ROM."""
    ROM_COPY = LocalROM()
    placed_messages = random.sample(boot_phrases, 4)
    for message_index, message in enumerate(placed_messages):
        ROM_COPY.seek(0x1FFD000 + (0x40 * message_index))
        ROM_COPY.writeBytes(message.upper().encode("ascii"))
