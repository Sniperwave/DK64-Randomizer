"""Data of the song breakdowns in ROM."""
from randomizer.Enums.SongType import SongType
from randomizer.Enums.SongGroups import SongGroup
from randomizer.Enums.Songs import Songs


class Song:
    """Class used for managing song objects."""

    def __init__(self, name, type=SongType.System, memory=None, location_tags=[], mood_tags=[], song_length=0):
        """Init SONG objects.

        Args:
            name (str): Name of the song.
            type (enum, optional): Songtype enum of the item. Defaults to SongType.System.
        """
        self.name = name
        self.output_name = name
        self.type = type
        self.memory = memory
        self.default_memory = memory
        self.channel = (memory >> 3) & 0xF
        self.location_tags = location_tags.copy()
        self.mood_tags = mood_tags.copy()
        self.song_length = song_length
        self.shuffled = False

    def Reset(self):
        """Reset song object so that output_name is reset between generations."""
        self.output_name = self.name
        self.memory = self.default_memory
        self.shuffled = False


class SongExclusionItem:
    """Song Exclusion multiselector information."""

    def __init__(self, name, shift, tooltip=""):
        """Initialize with given data."""
        self.name = name
        self.shift = shift
        self.tooltip = tooltip


SongList = {
    # DK Isles BGM
    Songs.TrainingGrounds: Song("Training Grounds", type=SongType.BGM, memory=0x101, location_tags=[SongGroup.Exteriors], mood_tags=[SongGroup.Calm]),
    Songs.Isles: Song("DK Isles", type=SongType.BGM, memory=0x101, location_tags=[SongGroup.Exteriors], mood_tags=[SongGroup.Happy, SongGroup.Calm]),
    Songs.IslesKremIsle: Song("DK Isles (K Rool's Ship)", type=SongType.BGM, memory=0x109, location_tags=[SongGroup.Exteriors], mood_tags=[SongGroup.Gloomy, SongGroup.Calm]),
    Songs.IslesKLumsy: Song("DK Isles (K-Lumsy's Prison)", type=SongType.BGM, memory=0x101, location_tags=[SongGroup.Interiors, SongGroup.Exteriors], mood_tags=[SongGroup.Gloomy, SongGroup.Calm]),
    Songs.IslesBFI: Song("DK Isles (Banana Fairy Island)", type=SongType.BGM, memory=0x101, location_tags=[SongGroup.Interiors, SongGroup.Exteriors], mood_tags=[SongGroup.Happy, SongGroup.Calm]),
    Songs.IslesSnideRoom: Song("DK Isles (Snide's Room)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Interiors], mood_tags=[SongGroup.Happy, SongGroup.Gloomy]),
    Songs.JapesLobby: Song("Jungle Japes (Lobby)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.LobbyShop], mood_tags=[SongGroup.Happy, SongGroup.Calm]),
    Songs.AztecLobby: Song("Angry Aztec (Lobby)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.LobbyShop], mood_tags=[SongGroup.Gloomy, SongGroup.Calm]),
    Songs.FactoryLobby: Song("Frantic Factory (Lobby)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.LobbyShop], mood_tags=[SongGroup.Gloomy, SongGroup.Calm]),
    Songs.GalleonLobby: Song("Gloomy Galleon (Lobby)", type=SongType.BGM, memory=0x101, location_tags=[SongGroup.LobbyShop], mood_tags=[SongGroup.Gloomy, SongGroup.Calm]),
    Songs.ForestLobby: Song("Fungi Forest (Lobby)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.LobbyShop], mood_tags=[SongGroup.Happy, SongGroup.Calm]),
    Songs.CavesLobby: Song("Crystal Caves (Lobby)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.LobbyShop], mood_tags=[SongGroup.Gloomy, SongGroup.Calm]),
    Songs.CastleLobby: Song("Creepy Castle (Lobby)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.LobbyShop], mood_tags=[SongGroup.Gloomy, SongGroup.Calm]),
    Songs.HelmLobby: Song("Hideout Helm (Lobby)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.LobbyShop], mood_tags=[SongGroup.Gloomy, SongGroup.Calm]),
    # Jungle Japes BGM
    Songs.JapesMain: Song("Jungle Japes", type=SongType.BGM, memory=0x101, location_tags=[SongGroup.Exteriors], mood_tags=[SongGroup.Happy]),
    Songs.JapesStart: Song("Jungle Japes (Starting Area)", type=SongType.BGM, memory=0x101, location_tags=[SongGroup.Exteriors], mood_tags=[SongGroup.Happy]),
    Songs.JapesTunnels: Song("Jungle Japes (Tunnels)", type=SongType.BGM, memory=0x18A, location_tags=[SongGroup.Interiors], mood_tags=[SongGroup.Gloomy, SongGroup.Calm]),
    Songs.JapesStorm: Song("Jungle Japes (Cranky's Area)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Exteriors], mood_tags=[SongGroup.Gloomy, SongGroup.Calm]),
    Songs.JapesCaves: Song("Jungle Japes (Caves/Underground)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Interiors], mood_tags=[SongGroup.Gloomy, SongGroup.Calm]),
    Songs.JapesBlast: Song("Jungle Japes (Baboon Blast)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Exteriors], mood_tags=[SongGroup.Calm]),
    Songs.JapesCart: Song("Jungle Japes (Minecart)", type=SongType.BGM, memory=0x188, location_tags=[SongGroup.Minigames], mood_tags=[SongGroup.Happy]),
    Songs.JapesDillo: Song("Jungle Japes (Army Dillo)", type=SongType.BGM, memory=0x189, location_tags=[SongGroup.Fight], mood_tags=[SongGroup.Gloomy]),
    # Angry Aztec BGM
    Songs.AztecMain: Song("Angry Aztec", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Exteriors], mood_tags=[SongGroup.Calm]),
    Songs.AztecTunnels: Song("Angry Aztec (Tunnels)", type=SongType.BGM, memory=0x192, location_tags=[SongGroup.Interiors], mood_tags=[SongGroup.Gloomy, SongGroup.Calm]),
    Songs.AztecTemple: Song("Angry Aztec (Temple)", type=SongType.BGM, memory=0x101, location_tags=[SongGroup.Interiors], mood_tags=[SongGroup.Gloomy, SongGroup.Calm]),
    Songs.Aztec5DT: Song("Angry Aztec (5DT)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Interiors], mood_tags=[SongGroup.Gloomy]),
    Songs.AztecBlast: Song("Angry Aztec (Baboon Blast)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Exteriors], mood_tags=[SongGroup.Calm]),
    Songs.AztecBeetle: Song("Angry Aztec (Beetle Slide)", type=SongType.BGM, memory=0x109, location_tags=[SongGroup.Minigames], mood_tags=[SongGroup.Happy, SongGroup.Calm]),
    Songs.AztecChunkyKlaptraps: Song("Angry Aztec (Chunky Klaptraps)", type=SongType.BGM, memory=0x188, location_tags=[SongGroup.Minigames], mood_tags=[SongGroup.Happy]),
    Songs.AztecDogadon: Song("Angry Aztec (Dogadon)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Fight], mood_tags=[SongGroup.Gloomy]),
    # Frantic Factory BGM
    Songs.FactoryMain: Song("Frantic Factory", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Exteriors], mood_tags=[SongGroup.Calm]),
    Songs.FactoryProduction: Song("Frantic Factory (Production Room)", type=SongType.BGM, memory=0x18A, location_tags=[SongGroup.Exteriors], mood_tags=[SongGroup.Gloomy, SongGroup.Calm]),
    Songs.FactoryResearchAndDevelopment: Song("Frantic Factory (R&D)", type=SongType.BGM, memory=0x18A, location_tags=[SongGroup.Interiors], mood_tags=[SongGroup.Gloomy]),
    Songs.FactoryCrusher: Song("Frantic Factory (Crusher Room)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Interiors], mood_tags=[SongGroup.Gloomy]),
    Songs.FactoryCarRace: Song("Frantic Factory (Car Race)", type=SongType.BGM, memory=0x188, location_tags=[SongGroup.Minigames], mood_tags=[SongGroup.Gloomy]),
    Songs.FactoryJack: Song("Frantic Factory (Mad Jack)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Fight], mood_tags=[SongGroup.Gloomy]),
    # Gloomy Galleon BGM
    Songs.GalleonTunnels: Song("Gloomy Galleon (Tunnels)", type=SongType.BGM, memory=0x18B, location_tags=[SongGroup.Interiors], mood_tags=[SongGroup.Gloomy, SongGroup.Calm]),
    Songs.GalleonOutside: Song("Gloomy Galleon (Outside)", type=SongType.BGM, memory=0x101, location_tags=[SongGroup.Exteriors], mood_tags=[SongGroup.Gloomy, SongGroup.Calm]),
    Songs.GalleonLighthouse: Song("Gloomy Galleon (Lighthouse)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Interiors], mood_tags=[SongGroup.Gloomy]),
    Songs.GalleonMechFish: Song("Gloomy Galleon (Mechanical Fish)", type=SongType.BGM, memory=0x101, location_tags=[SongGroup.Interiors], mood_tags=[SongGroup.Happy, SongGroup.Gloomy]),
    Songs.Galleon2DS: Song("Gloomy Galleon (2DS)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Interiors], mood_tags=[SongGroup.Gloomy, SongGroup.Calm]),
    Songs.Galleon5DS: Song("Gloomy Galleon (5DS/Submarine)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Interiors], mood_tags=[SongGroup.Gloomy, SongGroup.Calm]),
    Songs.GalleonMermaid: Song("Gloomy Galleon (Mermaid Palace)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Interiors], mood_tags=[SongGroup.Happy, SongGroup.Calm]),
    Songs.GalleonChest: Song("Gloomy Galleon (Pearls Chest)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Interiors], mood_tags=[SongGroup.Happy, SongGroup.Calm]),
    Songs.GalleonBlast: Song("Gloomy Galleon (Baboon Blast)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Interiors], mood_tags=[SongGroup.Gloomy, SongGroup.Calm]),
    Songs.GalleonSealRace: Song("Gloomy Galleon (Seal Race)", type=SongType.BGM, memory=0x188, location_tags=[SongGroup.Minigames], mood_tags=[SongGroup.Happy]),
    Songs.GalleonPufftoss: Song("Gloomy Galleon (Pufftoss)", type=SongType.BGM, memory=0x108, location_tags=[SongGroup.Fight], mood_tags=[SongGroup.Happy]),
    # Fungi Forest BGM
    Songs.ForestDay: Song("Fungi Forest (Day)", type=SongType.BGM, memory=0x101, location_tags=[SongGroup.Exteriors], mood_tags=[SongGroup.Happy, SongGroup.Calm]),
    Songs.ForestNight: Song("Fungi Forest (Night)", type=SongType.BGM, memory=0x188, location_tags=[SongGroup.Exteriors], mood_tags=[SongGroup.Gloomy, SongGroup.Calm]),
    Songs.ForestBarn: Song("Fungi Forest (Barn)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Interiors], mood_tags=[SongGroup.Gloomy, SongGroup.Calm]),
    Songs.ForestMill: Song("Fungi Forest (Mill)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Interiors], mood_tags=[SongGroup.Gloomy, SongGroup.Calm]),
    Songs.ForestAnthill: Song("Fungi Forest (Anthill)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Minigames], mood_tags=[SongGroup.Happy]),
    Songs.ForestMushroom: Song("Fungi Forest (Giant Mushroom)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Interiors], mood_tags=[SongGroup.Gloomy, SongGroup.Calm]),
    Songs.ForestMushroomRooms: Song("Fungi Forest (Mushroom Top Rooms)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Interiors], mood_tags=[SongGroup.Gloomy, SongGroup.Calm]),
    Songs.ForestWinch: Song("Fungi Forest (Winch)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Interiors], mood_tags=[SongGroup.Gloomy]),
    Songs.ForestSpider: Song("Fungi Forest (Spider)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Fight], mood_tags=[SongGroup.Happy, SongGroup.Gloomy]),
    Songs.ForestBlast: Song("Fungi Forest (Baboon Blast)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Exteriors], mood_tags=[SongGroup.Gloomy, SongGroup.Calm]),
    Songs.ForestRabbitRace: Song("Fungi Forest (Rabbit Race)", type=SongType.BGM, memory=0x188, location_tags=[SongGroup.Minigames], mood_tags=[SongGroup.Happy]),
    Songs.ForestCart: Song("Fungi Forest (Minecart)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Minigames], mood_tags=[SongGroup.Gloomy, SongGroup.Calm]),
    Songs.ForestDogadon: Song("Fungi Forest (Dogadon)", type=SongType.BGM, memory=0x188, location_tags=[SongGroup.Fight], mood_tags=[SongGroup.Happy]),
    # Crystal Caves BGM
    Songs.Caves: Song("Crystal Caves", type=SongType.BGM, memory=0x101, location_tags=[SongGroup.Exteriors], mood_tags=[SongGroup.Gloomy, SongGroup.Calm]),
    Songs.CavesIgloos: Song("Crystal Caves (Igloos)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Interiors], mood_tags=[SongGroup.Gloomy, SongGroup.Calm]),
    Songs.CavesCabins: Song("Crystal Caves (Cabins)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Interiors], mood_tags=[SongGroup.Gloomy, SongGroup.Calm]),
    Songs.CavesRotatingRoom: Song("Crystal Caves (Rotating Room)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Interiors], mood_tags=[SongGroup.Happy, SongGroup.Calm]),
    Songs.CavesTantrum: Song("Crystal Caves (Giant Kosha Tantrum)", type=SongType.BGM, memory=0x193, location_tags=[SongGroup.Interiors], mood_tags=[SongGroup.Gloomy]),
    Songs.CavesBlast: Song("Crystal Caves (Baboon Blast)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Exteriors], mood_tags=[SongGroup.Gloomy, SongGroup.Calm]),
    Songs.CavesIceCastle: Song("Crystal Caves (Tile Flipping)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Minigames], mood_tags=[SongGroup.Happy]),
    Songs.CavesBeetleRace: Song("Crystal Caves (Beetle Race)", type=SongType.BGM, memory=0x108, location_tags=[SongGroup.Minigames], mood_tags=[SongGroup.Happy]),
    Songs.CavesDillo: Song("Crystal Caves (Army Dillo)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Fight], mood_tags=[SongGroup.Happy, SongGroup.Gloomy]),
    # Creepy Castle BGM
    Songs.Castle: Song("Creepy Castle", type=SongType.BGM, memory=0x101, location_tags=[SongGroup.Exteriors], mood_tags=[SongGroup.Gloomy, SongGroup.Calm]),
    Songs.CastleTree: Song("Creepy Castle (Tree)", type=SongType.BGM, memory=0x101, location_tags=[SongGroup.Interiors], mood_tags=[SongGroup.Gloomy]),
    Songs.CastleTunnels: Song("Creepy Castle (Tunnels)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Interiors], mood_tags=[SongGroup.Gloomy, SongGroup.Calm]),
    Songs.CastleCrypt: Song("Creepy Castle (Crypt)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Interiors], mood_tags=[SongGroup.Gloomy, SongGroup.Calm]),
    Songs.CastleInnerCrypts: Song("Creepy Castle (Inner Crypts)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Interiors], mood_tags=[SongGroup.Gloomy]),
    Songs.CastleDungeon_Chains: Song("Creepy Castle (Dungeon w/ Chains)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Interiors], mood_tags=[SongGroup.Gloomy, SongGroup.Calm]),
    Songs.CastleDungeon_NoChains: Song("Creepy Castle (Dungeon w/out Chains)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Interiors], mood_tags=[SongGroup.Gloomy, SongGroup.Calm]),
    Songs.CastleBallroom: Song("Creepy Castle (Ballroom)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Interiors], mood_tags=[SongGroup.Gloomy]),
    Songs.CastleMuseum: Song("Creepy Castle (Museum)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Interiors], mood_tags=[SongGroup.Gloomy]),
    Songs.CastleGreenhouse: Song("Creepy Castle (Greenhouse)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Interiors], mood_tags=[SongGroup.Gloomy]),
    Songs.CastleTrash: Song("Creepy Castle (Trash Can)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Interiors], mood_tags=[SongGroup.Happy, SongGroup.Gloomy]),
    Songs.CastleTower: Song("Creepy Castle (Wind Tower)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Interiors], mood_tags=[SongGroup.Happy, SongGroup.Gloomy]),
    Songs.CastleBlast: Song("Creepy Castle (Baboon Blast)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Exteriors], mood_tags=[SongGroup.Gloomy, SongGroup.Calm]),
    Songs.CastleCart: Song("Creepy Castle (Minecart)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Minigames], mood_tags=[SongGroup.Happy, SongGroup.Gloomy]),
    Songs.CastleKutOut: Song("Creepy Castle (Kut Out)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Fight], mood_tags=[SongGroup.Happy, SongGroup.Gloomy]),
    # Hideout Helm BGM
    Songs.HelmBoMOn: Song("Hideout Helm (Blast-O-Matic On)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Exteriors], mood_tags=[SongGroup.Gloomy]),
    Songs.HelmBoMOff: Song("Hideout Helm (Blast-O-Matic Off)", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Exteriors], mood_tags=[SongGroup.Gloomy, SongGroup.Calm]),
    Songs.HelmBonus: Song("Hideout Helm (Bonus Barrels)", type=SongType.BGM, memory=0x188, location_tags=[SongGroup.Minigames], mood_tags=[SongGroup.Happy]),
    # NPC BGM
    Songs.Cranky: Song("Cranky's Lab", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.LobbyShop], mood_tags=[SongGroup.Gloomy]),
    Songs.Funky: Song("Funky's Hut", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.LobbyShop], mood_tags=[SongGroup.Happy]),
    Songs.Candy: Song("Candy's Music Shop", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.LobbyShop, SongGroup.Exteriors], mood_tags=[SongGroup.Gloomy, SongGroup.Calm]),
    Songs.Snide: Song("Snide's HQ", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.LobbyShop, SongGroup.Interiors], mood_tags=[SongGroup.Gloomy]),
    Songs.WrinklyKong: Song("Wrinkly Kong", type=SongType.BGM, memory=0x18A, location_tags=[SongGroup.LobbyShop], mood_tags=[SongGroup.Gloomy, SongGroup.Calm]),
    # Moves and Animals BGM
    Songs.StrongKong: Song("Strong Kong", type=SongType.BGM, memory=0x19A, location_tags=[SongGroup.Minigames], mood_tags=[SongGroup.Happy]),
    Songs.Rocketbarrel: Song("Rocketbarrel Boost", type=SongType.BGM, memory=0x192, location_tags=[SongGroup.Minigames], mood_tags=[SongGroup.Happy]),
    Songs.Sprint: Song("Orangstand Sprint", type=SongType.BGM, memory=0x190, location_tags=[SongGroup.Minigames], mood_tags=[SongGroup.Happy]),
    Songs.MiniMonkey: Song("Mini Monkey", type=SongType.BGM, memory=0x19A, location_tags=[SongGroup.Exteriors], mood_tags=[SongGroup.Happy]),
    Songs.HunkyChunky: Song("Hunky Chunky", type=SongType.BGM, memory=0x19A, location_tags=[SongGroup.Exteriors], mood_tags=[SongGroup.Gloomy]),
    Songs.GorillaGone: Song("Gorilla Gone", type=SongType.BGM, memory=0x190, location_tags=[SongGroup.Interiors], mood_tags=[SongGroup.Gloomy, SongGroup.Calm]),
    Songs.Rambi: Song("Rambi", type=SongType.BGM, memory=0x198, location_tags=[SongGroup.Minigames], mood_tags=[SongGroup.Happy]),
    Songs.Enguarde: Song("Enguarde", type=SongType.BGM, memory=0x198, location_tags=[SongGroup.Minigames], mood_tags=[SongGroup.Happy, SongGroup.Calm]),
    # Battle BGM
    Songs.BattleArena: Song("Battle Arena", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Fight, SongGroup.Minigames], mood_tags=[SongGroup.Happy]),
    Songs.TroffNScoff: Song("Troff 'n' Scoff", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Exteriors], mood_tags=[SongGroup.Happy, SongGroup.Calm]),
    Songs.AwaitingBossEntry: Song("Awaiting Entering the Boss", type=SongType.BGM, memory=0x190, location_tags=[SongGroup.Interiors], mood_tags=[SongGroup.Gloomy]),
    Songs.BossIntroduction: Song("Boss Introduction", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Fight], mood_tags=[SongGroup.Gloomy, SongGroup.Calm]),
    Songs.MiniBoss: Song("Mini Boss", type=SongType.BGM, memory=0x1AA, location_tags=[SongGroup.Fight], mood_tags=[SongGroup.Happy]),
    Songs.KRoolBattle: Song("K Rool's Battle", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Fight], mood_tags=[SongGroup.Happy]),
    # Menu and Story BGM
    Songs.MainMenu: Song("Main Menu", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Exteriors], mood_tags=[SongGroup.Happy, SongGroup.Calm]),
    Songs.PauseMenu: Song("Pause Menu", type=SongType.BGM, memory=0x1D4, location_tags=[SongGroup.Interiors], mood_tags=[SongGroup.Gloomy, SongGroup.Calm]),
    Songs.NintendoLogo: Song("Nintendo Logo", type=SongType.BGM, memory=0x108, location_tags=[SongGroup.Exteriors], mood_tags=[SongGroup.Happy]),
    Songs.DKRap: Song("DK Rap", type=SongType.BGM, memory=0x900, location_tags=[SongGroup.Fight, SongGroup.LobbyShop, SongGroup.Interiors, SongGroup.Exteriors, SongGroup.Minigames], mood_tags=[SongGroup.Happy]),
    Songs.IntroStory: Song("Intro Story Medley", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Exteriors], mood_tags=[SongGroup.Happy, SongGroup.Calm]),
    Songs.KRoolTheme: Song("K Rool's Theme", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Interiors], mood_tags=[SongGroup.Gloomy]),
    Songs.KLumsyCelebration: Song("K-Lumsy Celebration", type=SongType.BGM, memory=0x110, location_tags=[SongGroup.Exteriors], mood_tags=[SongGroup.Happy]),
    Songs.KRoolTakeoff: Song("K Rool Takeoff", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Exteriors], mood_tags=[SongGroup.Happy]),
    Songs.KRoolEntrance: Song("K Rool's Entrance", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Exteriors], mood_tags=[SongGroup.Happy]),
    Songs.KLumsyEnding: Song("K-Lumsy Ending", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Exteriors], mood_tags=[SongGroup.Happy, SongGroup.Calm]),
    Songs.EndSequence: Song("End Sequence", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Exteriors], mood_tags=[SongGroup.Happy]),
    # Minigame BGM
    Songs.Minigames: Song("Bonus Minigames", type=SongType.BGM, memory=0x189, location_tags=[SongGroup.Minigames], mood_tags=[SongGroup.Happy]),
    Songs.MadMazeMaul: Song("Mad Maze Maul", type=SongType.BGM, memory=0x188, location_tags=[SongGroup.Minigames], mood_tags=[SongGroup.Happy]),
    Songs.StealthySnoop: Song("Stealthy Snoop", type=SongType.BGM, memory=0x188, location_tags=[SongGroup.Minigames], mood_tags=[SongGroup.Gloomy, SongGroup.Calm]),
    Songs.MinecartMayhem: Song("Minecart Mayhem", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Minigames], mood_tags=[SongGroup.Happy]),
    Songs.MonkeySmash: Song("Monkey Smash", type=SongType.BGM, memory=0x100, location_tags=[SongGroup.Minigames], mood_tags=[SongGroup.Happy]),
    # Major Items
    Songs.OhBanana: Song("Oh Banana", type=SongType.MajorItem, memory=0xABD, location_tags=[SongGroup.Spawning], mood_tags=[SongGroup.Calm], song_length=3.25),
    Songs.GBGet: Song("GB/Key Get", type=SongType.MajorItem, memory=0x8C4, location_tags=[SongGroup.Collection], mood_tags=[SongGroup.Happy], song_length=3.86),
    Songs.MoveGet: Song("Move Get", type=SongType.MajorItem, memory=0x892, location_tags=[SongGroup.Collection], mood_tags=[SongGroup.Happy], song_length=10.05),
    Songs.GunGet: Song("Gun Get", type=SongType.MajorItem, memory=0x892, location_tags=[SongGroup.Collection], mood_tags=[SongGroup.Happy], song_length=1.53),
    Songs.BananaMedalGet: Song("Banana Medal Get", type=SongType.MajorItem, memory=0x645, location_tags=[SongGroup.Collection], mood_tags=[SongGroup.Happy], song_length=3.85),
    Songs.BlueprintDrop: Song("Blueprint Drop", type=SongType.MajorItem, memory=0x63D, location_tags=[SongGroup.Spawning], mood_tags=[SongGroup.Happy], song_length=2.08),
    Songs.BlueprintGet: Song("Blueprint Get", type=SongType.MajorItem, memory=0x4C5, location_tags=[SongGroup.Collection], mood_tags=[SongGroup.Happy, SongGroup.Calm], song_length=1.87),
    Songs.HeadphonesGet: Song("Headphones Get", type=SongType.MajorItem, memory=0x4BC, location_tags=[SongGroup.Collection], mood_tags=[SongGroup.Happy], song_length=3.23),
    Songs.DropRainbowCoin: Song("Drop Rainbow Coin", type=SongType.MajorItem, memory=0x647, location_tags=[SongGroup.Spawning], mood_tags=[SongGroup.Happy], song_length=0.91),
    Songs.RainbowCoinGet: Song("Rainbow Coin Get", type=SongType.MajorItem, memory=0x647, location_tags=[SongGroup.Collection], mood_tags=[SongGroup.Happy], song_length=1.06),
    Songs.CompanyCoinGet: Song("Company Coin Get", type=SongType.MajorItem, memory=0x637, location_tags=[SongGroup.Collection], mood_tags=[SongGroup.Happy], song_length=1.07),
    Songs.BeanGet: Song("Bean Get", type=SongType.MajorItem, memory=0x645, location_tags=[SongGroup.Collection], mood_tags=[SongGroup.Happy], song_length=1.86),
    Songs.PearlGet: Song("Pearl Get", type=SongType.MajorItem, memory=0x43E, location_tags=[SongGroup.Collection], mood_tags=[SongGroup.Happy, SongGroup.Calm], song_length=0.73),
    # Minor Items
    Songs.MelonSliceDrop: Song("Melon Slice Drop", type=SongType.MinorItem, memory=0x635, location_tags=[SongGroup.Spawning], mood_tags=[SongGroup.Calm], song_length=1.14),
    Songs.MelonSliceGet: Song("Melon Slice Get", type=SongType.MinorItem, memory=0x63F, location_tags=[SongGroup.Collection], mood_tags=[SongGroup.Happy], song_length=0.87),
    Songs.BananaCoinGet: Song("Banana Coin Get", type=SongType.MinorItem, memory=0x637, location_tags=[SongGroup.Collection], mood_tags=[SongGroup.Calm], song_length=0.46),
    Songs.CrystalCoconutGet: Song("Crystal Coconut Get", type=SongType.MinorItem, memory=0x63F, location_tags=[SongGroup.Collection], mood_tags=[SongGroup.Happy], song_length=0.67),
    Songs.FairyTick: Song("Fairy Tick", type=SongType.MinorItem, memory=0x8C5, location_tags=[SongGroup.Collection], mood_tags=[SongGroup.Calm], song_length=2.08),
    Songs.MinecartCoinGet: Song("Minecart Coin Get", type=SongType.MinorItem, memory=0x63F, location_tags=[SongGroup.Collection], mood_tags=[SongGroup.Happy], song_length=0.61),
    Songs.DropCoins: Song("Drop Coins (Minecart)", type=SongType.MinorItem, memory=0x445, location_tags=[SongGroup.Spawning], mood_tags=[SongGroup.Gloomy], song_length=1.14),
    Songs.Checkpoint: Song("Checkpoint", type=SongType.MinorItem, memory=0x447, location_tags=[SongGroup.Collection], mood_tags=[SongGroup.Happy], song_length=0.64),
    Songs.NormalStar: Song("Normal Star", type=SongType.MinorItem, memory=0x645, location_tags=[SongGroup.Collection], mood_tags=[SongGroup.Happy], song_length=3.04),
    # Events
    Songs.Success: Song("Success", type=SongType.Event, memory=0x8CD, location_tags=[SongGroup.Minigames], mood_tags=[SongGroup.Happy], song_length=2.13),
    Songs.Failure: Song("Failure", type=SongType.Event, memory=0x89D, location_tags=[SongGroup.Minigames], mood_tags=[SongGroup.Gloomy], song_length=3.27),
    Songs.SuccessRaces: Song("Success (Races)", type=SongType.Event, memory=0x118, location_tags=[SongGroup.Minigames, SongGroup.Spawning], mood_tags=[SongGroup.Happy], song_length=23.75),
    Songs.FailureRaces: Song("Failure (Races & Try Again)", type=SongType.Event, memory=0x118, location_tags=[SongGroup.Minigames, SongGroup.Spawning], mood_tags=[SongGroup.Gloomy], song_length=23.75),
    Songs.BossUnlock: Song("Boss Unlock", type=SongType.Event, memory=0x98, location_tags=[SongGroup.Spawning], mood_tags=[SongGroup.Happy], song_length=12.27),
    Songs.BossDefeat: Song("Boss Defeat", type=SongType.Event, memory=0x89A, location_tags=[SongGroup.Spawning], mood_tags=[SongGroup.Happy], song_length=5.35),
    Songs.Bongos: Song("Bongo Blast", type=SongType.Event, memory=0x8C2, location_tags=[SongGroup.Exteriors], mood_tags=[SongGroup.Calm], song_length=3.42),
    Songs.Guitar: Song("Guitar Gazump", type=SongType.Event, memory=0x8C2, location_tags=[SongGroup.Exteriors], mood_tags=[SongGroup.Happy], song_length=3.99),
    Songs.Trombone: Song("Trombone Tremor", type=SongType.Event, memory=0x8C2, location_tags=[SongGroup.Exteriors], mood_tags=[SongGroup.Happy], song_length=5.05),
    Songs.Saxophone: Song("Saxophone Slam", type=SongType.Event, memory=0x8C2, location_tags=[SongGroup.Exteriors], mood_tags=[SongGroup.Happy], song_length=4.22),
    Songs.Triangle: Song("Triangle Trample", type=SongType.Event, memory=0x8C2, location_tags=[SongGroup.Exteriors], mood_tags=[SongGroup.Happy], song_length=4.47),
    Songs.BaboonBalloon: Song("Baboon Balloon", type=SongType.Event, memory=0x19A, location_tags=[SongGroup.Exteriors], mood_tags=[SongGroup.Happy], song_length=20.04),
    Songs.Transformation: Song("Transformation", type=SongType.Event, memory=0xA34, location_tags=[SongGroup.Exteriors], mood_tags=[SongGroup.Gloomy], song_length=4.31),
    Songs.VultureRing: Song("Going through Vulture Ring", type=SongType.Event, memory=0x647, location_tags=[SongGroup.Collection], mood_tags=[SongGroup.Calm]),
    Songs.BBlastFinalStar: Song("Barrel Blast Final Star", type=SongType.Event, memory=0x445, location_tags=[SongGroup.Collection], mood_tags=[SongGroup.Happy], song_length=3.36),
    Songs.FinalCBGet: Song("100th CB Get", type=SongType.Event, memory=0x645, location_tags=[SongGroup.Collection], mood_tags=[SongGroup.Happy], song_length=2.10),
    # Ambient
    Songs.WaterDroplets: Song("Water Droplets", type=SongType.Ambient, memory=0x914),
    Songs.TwinklySounds: Song("Generic Twinkly Sounds", type=SongType.Ambient, memory=0x934),
    Songs.FairyNearby: Song("Fairy Nearby", type=SongType.Ambient, memory=0x925),
    Songs.SeasideSounds: Song("Generic Seaside Sounds", type=SongType.Ambient, memory=0x912),
    # Protected
    Songs.UnusedCoin: Song("Unused Coin Pickup", type=SongType.Protected, memory=0x440),
    Songs.StartPause: Song("Start (To pause game)", type=SongType.Protected, memory=0x85E),
    Songs.JapesHighPitched: Song("Unused High-Pitched Japes", type=SongType.Protected, memory=0x444),
    Songs.BonusBarrelIntroduction: Song("Bonus Barrel Introduction", type=SongType.Protected, memory=0x100),
    Songs.TagBarrel: Song("Tag Barrel (All of them)", type=SongType.Protected, memory=0x1CA),
    Songs.GameOver: Song("Game Over", type=SongType.Protected, memory=0x1D8),
    Songs.KRoolDefeat: Song("K Rool's Defeat", type=SongType.Protected, memory=0x18),
    # System
    Songs.Silence: Song("Silence", type=SongType.System, memory=0x00),
    Songs.TransitionOpen: Song("DK Transition (Opening)", type=SongType.System, memory=0x854),
    Songs.TransitionClose: Song("DK Transition (Closing)", type=SongType.System, memory=0x854),
    Songs.NintendoLogoOld: Song("Nintendo Logo (Old?)", type=SongType.System, memory=0x102),
}

DKIslesSongs = {
    Songs.TrainingGrounds,
    Songs.Isles,
    Songs.IslesKremIsle,
    Songs.IslesKLumsy,
    Songs.IslesBFI,
    Songs.IslesSnideRoom,
    Songs.JapesLobby,
    Songs.AztecLobby,
    Songs.FactoryLobby,
    Songs.GalleonLobby,
    Songs.ForestLobby,
    Songs.CavesLobby,
    Songs.CastleLobby,
    Songs.HelmLobby,
}
JungleJapesSongs = {
    Songs.JapesMain,
    Songs.JapesStart,
    Songs.JapesTunnels,
    Songs.JapesStorm,
    Songs.JapesCaves,
    Songs.JapesBlast,
    Songs.JapesCart,
    Songs.JapesDillo,
}
AngryAztecSongs = {
    Songs.AztecMain,
    Songs.AztecTunnels,
    Songs.AztecTemple,
    Songs.Aztec5DT,
    Songs.AztecBlast,
    Songs.AztecBeetle,
    Songs.AztecChunkyKlaptraps,
    Songs.AztecDogadon,
}
FranticFactorySongs = {
    Songs.FactoryMain,
    Songs.FactoryProduction,
    Songs.FactoryResearchAndDevelopment,
    Songs.FactoryCrusher,
    Songs.FactoryCarRace,
    Songs.FactoryJack,
}
GloomyGalleonSongs = {
    Songs.GalleonTunnels,
    Songs.GalleonOutside,
    Songs.GalleonLighthouse,
    Songs.GalleonMechFish,
    Songs.Galleon2DS,
    Songs.Galleon5DS,
    Songs.GalleonMermaid,
    Songs.GalleonChest,
    Songs.GalleonBlast,
    Songs.GalleonSealRace,
    Songs.GalleonPufftoss,
}
FungiForestSongs = {
    Songs.ForestDay,
    Songs.ForestNight,
    Songs.ForestBarn,
    Songs.ForestMill,
    Songs.ForestAnthill,
    Songs.ForestMushroom,
    Songs.ForestMushroomRooms,
    Songs.ForestWinch,
    Songs.ForestSpider,
    Songs.ForestBlast,
    Songs.ForestRabbitRace,
    Songs.ForestCart,
    Songs.ForestDogadon,
}
CrystalCavesSongs = {
    Songs.Caves,
    Songs.CavesIgloos,
    Songs.CavesCabins,
    Songs.CavesRotatingRoom,
    Songs.CavesTantrum,
    Songs.CavesBlast,
    Songs.CavesIceCastle,
    Songs.CavesBeetleRace,
    Songs.CavesDillo,
}
CreepyCastleSongs = {
    Songs.Castle,
    Songs.CastleTree,
    Songs.CastleTunnels,
    Songs.CastleCrypt,
    Songs.CastleInnerCrypts,
    Songs.CastleDungeon_Chains,
    Songs.CastleDungeon_NoChains,
    Songs.CastleBallroom,
    Songs.CastleMuseum,
    Songs.CastleGreenhouse,
    Songs.CastleTrash,
    Songs.CastleTower,
    Songs.CastleBlast,
    Songs.CastleCart,
    Songs.CastleKutOut,
}
HideoutHelmSongs = {
    Songs.HelmBoMOn,
    Songs.HelmBoMOff,
    Songs.HelmBonus,
}
NPCSongs = {
    Songs.Cranky,
    Songs.Funky,
    Songs.Candy,
    Songs.Snide,
    Songs.WrinklyKong,
}
MoveSongs = {
    Songs.StrongKong,
    Songs.Rocketbarrel,
    Songs.Sprint,
    Songs.MiniMonkey,
    Songs.HunkyChunky,
    Songs.GorillaGone,
    Songs.Rambi,
    Songs.Enguarde,
}
BattleSongs = {
    Songs.BattleArena,
    Songs.MiniBoss,
    Songs.TroffNScoff,
    Songs.AwaitingBossEntry,
    Songs.BossIntroduction,
    Songs.KRoolBattle,
}
MenusAndStorySongs = {
    Songs.NintendoLogo,
    Songs.DKRap,
    Songs.MainMenu,
    Songs.PauseMenu,
    Songs.IntroStory,
    Songs.KRoolTheme,
    Songs.KLumsyCelebration,
    Songs.KRoolTakeoff,
    Songs.KRoolEntrance,
    Songs.KLumsyEnding,
    Songs.EndSequence,
}
MinigameSongs = {
    Songs.Minigames,
    Songs.MadMazeMaul,
    Songs.StealthySnoop,
    Songs.MinecartMayhem,
    Songs.MonkeySmash,
}

song_data = [
    SongList[Songs.Silence],
    SongList[Songs.JapesStart],
    SongList[Songs.Cranky],
    SongList[Songs.JapesCart],
    SongList[Songs.JapesDillo],
    SongList[Songs.JapesCaves],
    SongList[Songs.Funky],
    SongList[Songs.UnusedCoin],
    SongList[Songs.Minigames],
    SongList[Songs.Triangle],
    SongList[Songs.Guitar],
    SongList[Songs.Bongos],
    SongList[Songs.Trombone],
    SongList[Songs.Saxophone],
    SongList[Songs.AztecMain],
    SongList[Songs.Transformation],
    SongList[Songs.MiniMonkey],
    SongList[Songs.HunkyChunky],
    SongList[Songs.GBGet],
    SongList[Songs.AztecBeetle],
    SongList[Songs.OhBanana],
    SongList[Songs.AztecTemple],
    SongList[Songs.CompanyCoinGet],
    SongList[Songs.BananaCoinGet],
    SongList[Songs.VultureRing],
    SongList[Songs.AztecDogadon],
    SongList[Songs.Aztec5DT],
    SongList[Songs.FactoryCarRace],
    SongList[Songs.FactoryMain],
    SongList[Songs.Snide],
    SongList[Songs.JapesTunnels],
    SongList[Songs.Candy],
    SongList[Songs.MinecartCoinGet],
    SongList[Songs.MelonSliceGet],
    SongList[Songs.PauseMenu],
    SongList[Songs.CrystalCoconutGet],
    SongList[Songs.Rambi],
    SongList[Songs.AztecTunnels],
    SongList[Songs.WaterDroplets],
    SongList[Songs.FactoryJack],
    SongList[Songs.Success],
    SongList[Songs.StartPause],
    SongList[Songs.Failure],
    SongList[Songs.TransitionOpen],
    SongList[Songs.TransitionClose],
    SongList[Songs.JapesHighPitched],
    SongList[Songs.FairyTick],
    SongList[Songs.MelonSliceDrop],
    SongList[Songs.AztecChunkyKlaptraps],
    SongList[Songs.FactoryCrusher],
    SongList[Songs.JapesBlast],
    SongList[Songs.FactoryResearchAndDevelopment],
    SongList[Songs.FactoryProduction],
    SongList[Songs.TroffNScoff],
    SongList[Songs.BossDefeat],
    SongList[Songs.AztecBlast],
    SongList[Songs.GalleonOutside],
    SongList[Songs.BossUnlock],
    SongList[Songs.AwaitingBossEntry],
    SongList[Songs.TwinklySounds],
    SongList[Songs.GalleonPufftoss],
    SongList[Songs.GalleonSealRace],
    SongList[Songs.GalleonTunnels],
    SongList[Songs.GalleonLighthouse],
    SongList[Songs.BattleArena],
    SongList[Songs.DropCoins],
    SongList[Songs.FairyNearby],
    SongList[Songs.Checkpoint],
    SongList[Songs.ForestDay],
    SongList[Songs.BlueprintGet],
    SongList[Songs.ForestNight],
    SongList[Songs.StrongKong],
    SongList[Songs.Rocketbarrel],
    SongList[Songs.Sprint],
    SongList[Songs.ForestCart],
    SongList[Songs.DKRap],
    SongList[Songs.BlueprintDrop],
    SongList[Songs.Galleon2DS],
    SongList[Songs.Galleon5DS],
    SongList[Songs.GalleonChest],
    SongList[Songs.GalleonMermaid],
    SongList[Songs.ForestDogadon],
    SongList[Songs.MadMazeMaul],
    SongList[Songs.Caves],
    SongList[Songs.CavesTantrum],
    SongList[Songs.NintendoLogoOld],
    SongList[Songs.SuccessRaces],
    SongList[Songs.FailureRaces],
    SongList[Songs.BonusBarrelIntroduction],
    SongList[Songs.StealthySnoop],
    SongList[Songs.MinecartMayhem],
    SongList[Songs.GalleonMechFish],
    SongList[Songs.GalleonBlast],
    SongList[Songs.ForestAnthill],
    SongList[Songs.ForestBarn],
    SongList[Songs.ForestMill],
    SongList[Songs.SeasideSounds],
    SongList[Songs.ForestSpider],
    SongList[Songs.ForestMushroomRooms],
    SongList[Songs.ForestMushroom],
    SongList[Songs.BossIntroduction],
    SongList[Songs.TagBarrel],
    SongList[Songs.CavesBeetleRace],
    SongList[Songs.CavesIgloos],
    SongList[Songs.MiniBoss],
    SongList[Songs.Castle],
    SongList[Songs.CastleCart],
    SongList[Songs.BaboonBalloon],
    SongList[Songs.GorillaGone],
    SongList[Songs.Isles],
    SongList[Songs.IslesKremIsle],
    SongList[Songs.IslesBFI],
    SongList[Songs.IslesKLumsy],
    SongList[Songs.HelmBoMOn],
    SongList[Songs.MoveGet],
    SongList[Songs.GunGet],
    SongList[Songs.HelmBoMOff],
    SongList[Songs.HelmBonus],
    SongList[Songs.CavesCabins],
    SongList[Songs.CavesRotatingRoom],
    SongList[Songs.CavesIceCastle],
    SongList[Songs.CastleTunnels],
    SongList[Songs.IntroStory],
    SongList[Songs.TrainingGrounds],
    SongList[Songs.Enguarde],
    SongList[Songs.KLumsyCelebration],
    SongList[Songs.CastleCrypt],
    SongList[Songs.HeadphonesGet],
    SongList[Songs.PearlGet],
    SongList[Songs.CastleDungeon_Chains],
    SongList[Songs.AztecLobby],
    SongList[Songs.JapesLobby],
    SongList[Songs.FactoryLobby],
    SongList[Songs.GalleonLobby],
    SongList[Songs.MainMenu],
    SongList[Songs.CastleInnerCrypts],
    SongList[Songs.CastleBallroom],
    SongList[Songs.CastleGreenhouse],
    SongList[Songs.KRoolTheme],
    SongList[Songs.ForestWinch],
    SongList[Songs.CastleTower],
    SongList[Songs.CastleTree],
    SongList[Songs.CastleMuseum],
    SongList[Songs.BBlastFinalStar],
    SongList[Songs.DropRainbowCoin],
    SongList[Songs.RainbowCoinGet],
    SongList[Songs.NormalStar],
    SongList[Songs.BeanGet],
    SongList[Songs.CavesDillo],
    SongList[Songs.CastleKutOut],
    SongList[Songs.CastleDungeon_NoChains],
    SongList[Songs.BananaMedalGet],
    SongList[Songs.KRoolBattle],
    SongList[Songs.ForestLobby],
    SongList[Songs.CavesLobby],
    SongList[Songs.CastleLobby],
    SongList[Songs.HelmLobby],
    SongList[Songs.CastleTrash],
    SongList[Songs.EndSequence],
    SongList[Songs.KLumsyEnding],
    SongList[Songs.JapesMain],
    SongList[Songs.JapesStorm],
    SongList[Songs.KRoolTakeoff],
    SongList[Songs.CavesBlast],
    SongList[Songs.ForestBlast],
    SongList[Songs.CastleBlast],
    SongList[Songs.IslesSnideRoom],
    SongList[Songs.KRoolEntrance],
    SongList[Songs.MonkeySmash],
    SongList[Songs.ForestRabbitRace],
    SongList[Songs.GameOver],
    SongList[Songs.WrinklyKong],
    SongList[Songs.FinalCBGet],
    SongList[Songs.KRoolDefeat],
    SongList[Songs.NintendoLogo],
]

ExcludedSongsSelector = []
ExclSongsItems = [
    SongExclusionItem("Wrinkly", 0, "Removes Wrinkly doors from playing her theme."),
    SongExclusionItem("Transformation", 3, "The game will no longer play the transformation sound effect."),
    SongExclusionItem("Pause Music", 4, "The pause menu music will no longer play."),
    SongExclusionItem("Sub Areas", 5, "Sub-Areas will no longer play their song, meaning that there's 1 piece of music for the entire level."),
    # SongExclusionItem("Shops", 1, "COMING SOON: Makes shops inherit the previous song."), # TODO: Fix this
    # SongExclusionItem("Events", 2, "COMING SOON: Events will no longer play a song."), # TODO: Fix this
]
for item in ExclSongsItems:
    if item.name != "No Group":
        ExcludedSongsSelector.append({"name": item.name, "value": item.name.lower().replace(" ", "_"), "tooltip": item.tooltip, "shift": item.shift})

# This dict determines all of the dropdowns for selecting music, and how they
# will be grouped together.
MusicSelectionPanel = {
    "Isles": {"name": "DK Isles", "type": "BGM", "songs": []},
    "Japes": {"name": "Jungle Japes", "type": "BGM", "songs": []},
    "Aztec": {"name": "Angry Aztec", "type": "BGM", "songs": []},
    "Factory": {"name": "Frantic Factory", "type": "BGM", "songs": []},
    "Galleon": {"name": "Gloomy Galleon", "type": "BGM", "songs": []},
    "Forest": {"name": "Fungi Forest", "type": "BGM", "songs": []},
    "Caves": {"name": "Crystal Caves", "type": "BGM", "songs": []},
    "Castle": {"name": "Creepy Castle", "type": "BGM", "songs": []},
    "Helm": {"name": "Hideout Helm", "type": "BGM", "songs": []},
    "NPC": {"name": "NPCs", "type": "BGM", "songs": []},
    "Moves": {"name": "Moves and Animals", "type": "BGM", "songs": []},
    "Battle": {"name": "Battles", "type": "BGM", "songs": []},
    "Story": {"name": "Menus and Story", "type": "BGM", "songs": []},
    "Minigame": {"name": "Minigames", "type": "BGM", "songs": []},
    "MajorItem": {"name": "Major Items", "type": "MajorItem", "songs": []},
    "MinorItem": {"name": "Minor Items", "type": "MinorItem", "songs": []},
    "Event": {"name": "Events", "type": "Event", "songs": []},
}

bgmCategoryMap = {
    "Isles": DKIslesSongs,
    "Japes": JungleJapesSongs,
    "Aztec": AngryAztecSongs,
    "Factory": FranticFactorySongs,
    "Galleon": GloomyGalleonSongs,
    "Forest": FungiForestSongs,
    "Caves": CrystalCavesSongs,
    "Castle": CreepyCastleSongs,
    "Helm": HideoutHelmSongs,
    "NPC": NPCSongs,
    "Moves": MoveSongs,
    "Battle": BattleSongs,
    "Story": MenusAndStorySongs,
    "Minigame": MinigameSongs,
}

# This dict groups songs together by type, to determine which songs can be
# placed in which locations.
PlannableSongs = {
    "BGM": [],
    "MajorItem": [],
    "MinorItem": [],
    "Event": [],
}

# This list is used when resetting all selected songs at once.
SongLocationList = []

# Process possible song locations.
for songEnum, song in SongList.items():
    if song.type in [SongType.Ambient, SongType.Protected, SongType.System]:
        continue
    songJson = {
        "name": song.name,
        "value": songEnum.name,
    }
    if song.type == SongType.BGM:
        PlannableSongs["BGM"].append(songJson)
        # Remove Monkey Smash as a location, but keep it as an option for other
        # songs.
        if songEnum == Songs.MonkeySmash:
            continue
        SongLocationList.append(songEnum.name)
        # Find the category this song belongs to.
        for category, songSet in bgmCategoryMap.items():
            if songEnum in songSet:
                MusicSelectionPanel[category]["songs"].append(songJson)
    else:
        PlannableSongs[song.type.name].append(songJson)
        SongLocationList.append(songEnum.name)
        MusicSelectionPanel[song.type.name]["songs"].append(songJson)
