# fmt: off
"""Shufflable exit class and list file."""

from randomizer.Enums.Exits import Exits
from randomizer.Enums.ExitCategories import ExitCategories
from randomizer.Enums.Regions import Regions


class ShufflableExit:
    """Class that stores data about an exit to be shuffled."""

    def __init__(self, name, region, reverse, category=None):
        """Initialize with given parameters."""
        self.name = name
        self.region = region
        self.reverse = reverse
        self.category = category
        # Here dest is the entrance to go to, rather than just the target region
        # Initialized as its default reverse value
        self.dest = reverse
        self.shuffled = False
        self.ignore = False  # used for spoiler so reverse entrances are not printed if not decoupled


ShufflableExits = {
    # Level Exits
    Exits.IslesToJapes: ShufflableExit("DK Isles to Jungle Japes", Regions.JungleJapesLobby, Exits.JapesToIsles, ExitCategories.IslesLevelExits),
    Exits.JapesToIsles: ShufflableExit("Jungle Japes to DK Isles", Regions.JungleJapesMain, Exits.IslesToJapes, ExitCategories.LevelExits),
    Exits.IslesToAztec: ShufflableExit("DK Isles to Angry Aztec", Regions.AngryAztecLobby, Exits.AztecToIsles, ExitCategories.IslesLevelExits),
    Exits.AztecToIsles: ShufflableExit("Angry Aztec to DK Isles", Regions.AngryAztecStart, Exits.IslesToAztec, ExitCategories.LevelExits),
    Exits.IslesToFactory: ShufflableExit("DK Isles to Frantic Factory", Regions.FranticFactoryLobby, Exits.FactoryToIsles, ExitCategories.IslesLevelExits),
    Exits.FactoryToIsles: ShufflableExit("Frantic Factory to DK Isles", Regions.FranticFactoryStart, Exits.IslesToFactory, ExitCategories.LevelExits),
    Exits.IslesToGalleon: ShufflableExit("DK Isles to Gloomy Galleon", Regions.GloomyGalleonLobby, Exits.GalleonToIsles, ExitCategories.IslesLevelExits),
    Exits.GalleonToIsles: ShufflableExit("Gloomy Galleon to DK Isles", Regions.GloomyGalleonStart, Exits.IslesToGalleon, ExitCategories.LevelExits),
    Exits.IslesToForest: ShufflableExit("DK Isles to Fungi Forest", Regions.FungiForestLobby, Exits.ForestToIsles, ExitCategories.IslesLevelExits),
    Exits.ForestToIsles: ShufflableExit("Fungi Forest to DK Isles", Regions.FungiForestStart, Exits.IslesToForest, ExitCategories.LevelExits),
    Exits.IslesToCaves: ShufflableExit("DK Isles to Crystal Caves", Regions.CrystalCavesLobby, Exits.CavesToIsles, ExitCategories.IslesLevelExits),
    Exits.CavesToIsles: ShufflableExit("Crystal Caves to DK Isles", Regions.CrystalCavesMain, Exits.IslesToCaves, ExitCategories.LevelExits),
    Exits.IslesToCastle: ShufflableExit("DK Isles to Creepy Castle", Regions.CreepyCastleLobby, Exits.CastleToIsles, ExitCategories.IslesLevelExits),
    Exits.CastleToIsles: ShufflableExit("Creepy Castle to DK Isles", Regions.CreepyCastleMain, Exits.IslesToCastle, ExitCategories.LevelExits),
    Exits.IslesToHelm: ShufflableExit("DK Isles to Hideout Helm", Regions.HideoutHelmLobby, Exits.HelmToIsles, ExitCategories.IslesLevelExits),
    Exits.HelmToIsles: ShufflableExit("Hideout Helm to DK Isles", Regions.HideoutHelmStart, Exits.IslesToHelm, ExitCategories.LevelExits),
    # DK Isles Exits
    Exits.IslesMainToStart: ShufflableExit("DK Isles Main to Start Area", Regions.IslesMain, Exits.IslesStartToMain, ExitCategories.IslesExterior),
    Exits.IslesStartToMain: ShufflableExit("DK Isles Start Area to Main", Regions.StartArea, Exits.IslesMainToStart, ExitCategories.IslesStart),
    Exits.IslesStartToTreehouse: ShufflableExit("DK Isles Start Area to Treehouse", Regions.StartArea, Exits.IslesTreehouseToStart, ExitCategories.IslesStart),
    Exits.IslesTreehouseToStart: ShufflableExit("DK Isles Treehouse to Start", Regions.Treehouse, Exits.IslesStartToTreehouse),
    Exits.IslesMainToPrison: ShufflableExit("DK Isles Main to Prison", Regions.IslesMain, Exits.IslesPrisonToMain, ExitCategories.IslesExterior),
    Exits.IslesPrisonToMain: ShufflableExit("DK Isles Prison to Main", Regions.Prison, Exits.IslesMainToPrison),
    Exits.IslesMainToFairy: ShufflableExit("DK Isles Main to Banana Fairy Queen", Regions.IslesMain, Exits.IslesFairyToMain, ExitCategories.IslesExterior),
    Exits.IslesFairyToMain: ShufflableExit("DK Isles Banana Fairy Queen to Main", Regions.BananaFairyRoom, Exits.IslesMainToFairy),
    Exits.IslesMainToSnideRoom: ShufflableExit("DK Isles Crocodile Isle to Snide Room", Regions.CrocodileIsleBeyondLift, Exits.IslesSnideRoomToMain, ExitCategories.IslesExterior),
    Exits.IslesSnideRoomToMain: ShufflableExit("DK Isles Snide Room to Crocodile Isle", Regions.IslesSnideRoom, Exits.IslesMainToSnideRoom),
    Exits.IslesMainToJapesLobby: ShufflableExit("DK Isles Main to Jungle Japes Lobby", Regions.IslesMain, Exits.IslesJapesLobbyToMain, ExitCategories.IslesExterior),
    Exits.IslesJapesLobbyToMain: ShufflableExit("DK Isles Jungle Japes Lobby to Main", Regions.JungleJapesLobby, Exits.IslesMainToJapesLobby),
    Exits.IslesMainToAztecLobby: ShufflableExit("DK Isles Main to Angry Aztec Lobby", Regions.IslesMain, Exits.IslesAztecLobbyToMain, ExitCategories.IslesExterior),
    Exits.IslesAztecLobbyToMain: ShufflableExit("DK Isles Angry Aztec Lobby to Main", Regions.AngryAztecLobby, Exits.IslesMainToAztecLobby),
    Exits.IslesMainToFactoryLobby: ShufflableExit("DK Isles Main to Frantic Factory Lobby", Regions.CrocodileIsleBeyondLift, Exits.IslesFactoryLobbyToMain, ExitCategories.IslesExterior),
    Exits.IslesFactoryLobbyToMain: ShufflableExit("DK Isles Frantic Factory Lobby to Main", Regions.FranticFactoryLobby, Exits.IslesMainToFactoryLobby),
    Exits.IslesMainToGalleonLobby: ShufflableExit("DK Isles Main to Gloomy Galleon Lobby", Regions.IslesMain, Exits.IslesGalleonLobbyToMain, ExitCategories.IslesExterior),
    Exits.IslesGalleonLobbyToMain: ShufflableExit("DK Isles Gloomy Galleon Lobby to Main", Regions.GloomyGalleonLobby, Exits.IslesMainToGalleonLobby),
    Exits.IslesMainToForestLobby: ShufflableExit("DK Isles Cabin Isle to Fungi Forest Lobby", Regions.CabinIsle, Exits.IslesForestLobbyToMain, ExitCategories.IslesExterior),
    Exits.IslesForestLobbyToMain: ShufflableExit("DK Isles Fungi Forest Lobby to Cabin Isle", Regions.FungiForestLobby, Exits.IslesMainToForestLobby),
    Exits.IslesMainToCavesLobby: ShufflableExit("DK Isles Main to Crystal Caves Lobby", Regions.IslesMain, Exits.IslesCavesLobbyToMain, ExitCategories.IslesExterior),
    Exits.IslesCavesLobbyToMain: ShufflableExit("DK Isles Crystal Caves Lobby to Main", Regions.CrystalCavesLobby, Exits.IslesMainToCavesLobby),
    Exits.IslesMainToCastleLobby: ShufflableExit("DK Isles Main to Creepy Castle Lobby", Regions.IslesMain, Exits.IslesCastleLobbyToMain, ExitCategories.IslesExterior),
    Exits.IslesCastleLobbyToMain: ShufflableExit("DK Isles Creepy Castle Lobby to Main", Regions.CreepyCastleLobby, Exits.IslesMainToCastleLobby),
    Exits.IslesMainToHelmLobby: ShufflableExit("DK Isles Crocodile Isle to Hideout Helm Lobby", Regions.IslesMain, Exits.IslesHelmLobbyToMain, ExitCategories.IslesExterior),
    Exits.IslesHelmLobbyToMain: ShufflableExit("DK Isles Hideout Helm Lobby to Crocodile Isle", Regions.HideoutHelmLobby, Exits.IslesMainToHelmLobby),
    # Jungle Japes Exits
    Exits.JapesMainToMine: ShufflableExit("Jungle Japes Main to Mine", Regions.JungleJapesMain, Exits.JapesMineToMain, ExitCategories.JapesExterior),
    Exits.JapesMineToMain: ShufflableExit("Jungle Japes Mine to Main", Regions.Mine, Exits.JapesMainToMine, ExitCategories.JapesMine),
    Exits.JapesMainToLankyCave: ShufflableExit("Jungle Japes Main to Lanky Cave", Regions.IslesMain, Exits.JapesLankyCaveToMain, ExitCategories.JapesExterior),
    Exits.JapesLankyCaveToMain: ShufflableExit("Jungle Japes Lanky Cave to Main", Regions.JapesLankyCave, Exits.JapesMainToLankyCave),
    Exits.JapesMainToCatacomb: ShufflableExit("Jungle Japes Main to Catacomb", Regions.JungleJapesMain, Exits.JapesCatacombToMain, ExitCategories.JapesExterior),
    Exits.JapesCatacombToMain: ShufflableExit("Jungle Japes Catacomb to Main", Regions.JapesCatacomb, Exits.JapesMainToCatacomb),
    Exits.JapesMainToTinyHive: ShufflableExit("Jungle Japes Main to Tiny Hive", Regions.JapesBeyondFeatherGate, Exits.JapesTinyHiveToMain, ExitCategories.JapesExterior),
    Exits.JapesTinyHiveToMain: ShufflableExit("Jungle Japes Tiny Hive to Main", Regions.TinyHive, Exits.JapesMainToTinyHive),
    Exits.JapesMineToCarts: ShufflableExit("Jungle Japes Mine to Minecarts", Regions.Mine, Exits.JapesCartsToMine, ExitCategories.JapesMine),
    Exits.JapesCartsToMine: ShufflableExit("Jungle Japes Minecarts to Main", Regions.JapesMinecarts, Exits.JapesMineToCarts),
    # Angry Aztec Exits
    Exits.AztecStartToTemple: ShufflableExit("Angry Aztec Start to Temple", Regions.AngryAztecStart, Exits.AztecTempleToStart, ExitCategories.AztecExterior),
    Exits.AztecTempleToStart: ShufflableExit("Angry Aztec Temple to Start", Regions.TempleStart, Exits.AztecStartToTemple),
    Exits.AztecMainToDonkey: ShufflableExit("Angry Aztec Main to Donkey 5DT", Regions.AngryAztecMain, Exits.AztecDonkeyToMain, ExitCategories.AztecExterior),
    Exits.AztecDonkeyToMain: ShufflableExit("Angry Aztec Donkey 5DT to Main", Regions.DonkeyTemple, Exits.AztecMainToDonkey),
    Exits.AztecMainToDiddy: ShufflableExit("Angry Aztec Main to Diddy 5DT", Regions.AngryAztecMain, Exits.AztecDiddyToMain, ExitCategories.AztecExterior),
    Exits.AztecDiddyToMain: ShufflableExit("Angry Aztec Diddy 5DT to Main", Regions.DiddyTemple, Exits.AztecMainToDiddy),
    Exits.AztecMainToLanky: ShufflableExit("Angry Aztec Main to Lanky 5DT", Regions.AngryAztecMain, Exits.AztecLankyToMain, ExitCategories.AztecExterior),
    Exits.AztecLankyToMain: ShufflableExit("Angry Aztec Lanky 5DT to Main", Regions.LankyTemple, Exits.AztecMainToLanky),
    Exits.AztecMainToTiny: ShufflableExit("Angry Aztec Main to Tiny 5DT", Regions.AngryAztecMain, Exits.AztecTinyToMain, ExitCategories.AztecExterior),
    Exits.AztecTinyToMain: ShufflableExit("Angry Aztec Tiny 5DT To Main", Regions.TinyTemple, Exits.AztecMainToTiny),
    Exits.AztecMainToChunky: ShufflableExit("Angry Aztec Main to Chunky 5DT", Regions.AngryAztecMain, Exits.AztecChunkyToMain, ExitCategories.AztecExterior),
    Exits.AztecChunkyToMain: ShufflableExit("Angry Aztec Chunky 5DT to Main", Regions.ChunkyTemple, Exits.AztecMainToChunky),
    Exits.AztecMainToRace: ShufflableExit("Angry Aztec Main to Beetle Race", Regions.AngryAztecMain, Exits.AztecRaceToMain, ExitCategories.AztecExterior),
    Exits.AztecRaceToMain: ShufflableExit("Angry Aztec Beetle Race to Main", Regions.AztecTinyRace, Exits.AztecMainToRace),
    Exits.AztecMainToLlama: ShufflableExit("Angry Aztec Main to Llama Temple", Regions.AngryAztecMain, Exits.AztecLlamaToMain, ExitCategories.AztecExterior),
    Exits.AztecLlamaToMain: ShufflableExit("Angry Aztec Llama Temple to Main", Regions.LlamaTemple, Exits.AztecMainToLlama),
    # Frantic Factory Exits
    Exits.FactoryRandDToRace: ShufflableExit("Frantic Factory R&D to Car Race", Regions.RandD, Exits.FactoryRaceToRandD, ExitCategories.FactoryExterior),
    Exits.FactoryRaceToRandD: ShufflableExit("Frantic Factory Car Race to R&D", Regions.FactoryTinyRace, Exits.FactoryRandDToRace),
    Exits.FactoryChunkyRoomToPower: ShufflableExit("Frantic Factory Chunky Room to Power Room", Regions.ChunkyRoomPlatform, Exits.FactoryPowerToChunkyRoom, ExitCategories.FactoryExterior),
    Exits.FactoryPowerToChunkyRoom: ShufflableExit("Frantic Factory Power Room to Chunky Room", Regions.PowerHut, Exits.FactoryChunkyRoomToPower),
    Exits.FactoryBeyondHatchToInsideCore: ShufflableExit("Frantic Factory Beyond Hatch to Inside Core", Regions.BeyondHatch, Exits.FactoryInsideCoreToBeyondHatch, ExitCategories.FactoryExterior),
    Exits.FactoryInsideCoreToBeyondHatch: ShufflableExit("Frantic Factory Inside Core to Beyond Hatch", Regions.InsideCore, Exits.FactoryBeyondHatchToInsideCore),
    # Gloomy Galleon Exits
    Exits.GalleonLighthouseAreaToLighthouse: ShufflableExit("Gloomy Galleon Main to Lighthouse", Regions.LighthouseArea, Exits.GalleonLighthouseToLighthouseArea, ExitCategories.GalleonExterior),
    Exits.GalleonLighthouseToLighthouseArea: ShufflableExit("Gloomy Galleon Lighthouse to Main", Regions.Lighthouse, Exits.GalleonLighthouseAreaToLighthouse),
    Exits.GalleonLighthousAreaToMermaid: ShufflableExit("Gloomy Galleon Main to Mermaid Room", Regions.LighthouseArea, Exits.GalleonMermaidToLighthouseArea, ExitCategories.GalleonExterior),
    Exits.GalleonMermaidToLighthouseArea: ShufflableExit("Gloomy Galleon Mermaid Room to Main", Regions.MermaidRoom, Exits.GalleonLighthousAreaToMermaid),
    Exits.GalleonLighthouseAreaToSickBay: ShufflableExit("Gloomy Galleon Main to Sick Bay", Regions.LighthouseArea, Exits.GalleonSickBayToLighthouseArea, ExitCategories.GalleonExterior),
    Exits.GalleonSickBayToLighthouseArea: ShufflableExit("Gloomy Galleon Sick Bay to Main", Regions.SickBay, Exits.GalleonLighthouseAreaToSickBay),
    Exits.GalleonShipyardToSeal: ShufflableExit("Gloomy Galleon Main to Seal Race", Regions.Shipyard, Exits.GalleonSealToShipyard, ExitCategories.GalleonExterior),
    Exits.GalleonSealToShipyard: ShufflableExit("Gloomy Galleon Seal Race to Main", Regions.SealRace, Exits.GalleonShipyardToSeal),
    Exits.GalleonShipyardToSubmarine: ShufflableExit("Gloomy Galleon Main to Submarine", Regions.Shipyard, Exits.GalleonSubmarineToShipyard, ExitCategories.GalleonExterior),
    Exits.GalleonSubmarineToShipyard: ShufflableExit("Gloomy Galleon Submarine to Main", Regions.Submarine, Exits.GalleonShipyardToSubmarine),
    Exits.GalleonShipyardToMechafish: ShufflableExit("Gloomy Galleon Main to Mechafish", Regions.Shipyard, Exits.GalleyonMechafishToShipyard, ExitCategories.GalleonExterior),
    Exits.GalleyonMechafishToShipyard: ShufflableExit("Gloomy Galleon Mechafish to Main", Regions.Mechafish, Exits.GalleonShipyardToMechafish),
    Exits.GalleonShipyardToLanky: ShufflableExit("Gloomy Galleon Main to Lanky 2DS", Regions.Shipyard, Exits.GalleonLankyToShipyard, ExitCategories.GalleonExterior),
    Exits.GalleonLankyToShipyard: ShufflableExit("Gloomy Galleon Lanky 2DS to Main", Regions.LankyShip, Exits.GalleonShipyardToLanky),
    Exits.GalleonShipyardToTiny: ShufflableExit("Gloomy Galleon Main to Tiny 2DS", Regions.Shipyard, Exits.GalleonTinyToShipyard, ExitCategories.GalleonExterior),
    Exits.GalleonTinyToShipyard: ShufflableExit("Gloomy Galleon Tiny 2DS to Main", Regions.TinyShip, Exits.GalleonShipyardToTiny),
    Exits.GalleonShipyardToBongos: ShufflableExit("Gloomy Galleon Main to Donkey 5DS", Regions.Shipyard, Exits.GalleonBongosToShipyard, ExitCategories.GalleonExterior),
    Exits.GalleonBongosToShipyard: ShufflableExit("Gloomy Galleon Donkey 5DS to Main", Regions.BongosShip, Exits.GalleonShipyardToBongos),
    Exits.GalleonShipyardToGuitar: ShufflableExit("Gloomy Galleon Main to Diddy 5DS", Regions.Shipyard, Exits.GalleonGuitarToShipyard, ExitCategories.GalleonExterior),
    Exits.GalleonGuitarToShipyard: ShufflableExit("Gloomy Galleon Diddy 5DS to Main", Regions.GuitarShip, Exits.GalleonShipyardToGuitar),
    Exits.GalleonShipyardToTrombone: ShufflableExit("Gloomy Galleon Main to Lanky 5DS", Regions.Shipyard, Exits.GalleonTromboneToShipyard, ExitCategories.GalleonExterior),
    Exits.GalleonTromboneToShipyard: ShufflableExit("Gloomy Galleon Lanky 5DS to Main", Regions.TromboneShip, Exits.GalleonShipyardToTrombone),
    Exits.GalleonShipyardToSaxophone: ShufflableExit("Gloomy Galleon Main to Tiny 5DS", Regions.Shipyard, Exits.GalleonSaxophoneToShipyard, ExitCategories.GalleonExterior),
    Exits.GalleonSaxophoneToShipyard: ShufflableExit("Gloomy Galleon Tiny 5DS to Main", Regions.SaxophoneShip, Exits.GalleonShipyardToSaxophone),
    Exits.GalleonShipyardToTriangle: ShufflableExit("Gloomy Galleon Main to Chunky 5DS", Regions.Shipyard, Exits.GalleonTriangleToShipyard, ExitCategories.GalleonExterior),
    Exits.GalleonTriangleToShipyard: ShufflableExit("Gloomy Galleon Chunky 5DS to Main", Regions.TriangleShip, Exits.GalleonShipyardToTriangle),
    Exits.GalleonTreasureToChest: ShufflableExit("Gloomy Galleon Main to Chest", Regions.TreasureRoom, Exits.GalleonChestToTreasure, ExitCategories.GalleonExterior),
    Exits.GalleonChestToTreasure: ShufflableExit("Gloomy Galleon Chest to Main", Regions.TinyChest, Exits.GalleonTreasureToChest),
    # Fungi Forest Exits
    Exits.ForestMainToCarts: ShufflableExit("Fungi Forest Main to Minecarts", Regions.FungiForestStart, Exits.ForestCartsToMain, ExitCategories.ForestExterior),
    Exits.ForestCartsToMain: ShufflableExit("Fungi Forest Minecarts to Main", Regions.ForestMinecarts, Exits.ForestMainToCarts),
    Exits.ForestMainToLowerMushroom: ShufflableExit("Fungi Forest Main to Mushroom Lower", Regions.GiantMushroomArea, Exits.ForestLowerMushroomToMain, ExitCategories.ForestExterior),
    Exits.ForestLowerMushroomToMain: ShufflableExit("Fungi Forest Mushroom Lower to Main", Regions.MushroomLower, Exits.ForestMainToLowerMushroom, ExitCategories.ForestMushroom),
    Exits.ForestLowerExteriorToLowerMushroom: ShufflableExit("Fungi Forest Lower Exterior to Lower Mushroom", Regions.MushroomLowerExterior, Exits.ForestLowerMushroomToLowerExterior, ExitCategories.ForestExterior),
    Exits.ForestLowerMushroomToLowerExterior: ShufflableExit("Fungi Forest Lower Mushroom to Lower Exterior", Regions.MushroomLower, Exits.ForestLowerExteriorToLowerMushroom, ExitCategories.ForestMushroom),
    Exits.ForestLowerExteriorToUpperMushroom: ShufflableExit("Fungi Forest Lower Exterior to Upper Mushroom", Regions.MushroomLowerExterior, Exits.ForestUpperMushroomToLowerExterior, ExitCategories.ForestExterior),
    Exits.ForestUpperMushroomToLowerExterior: ShufflableExit("Fungi Forest Upper Mushroom to Lower Exterior", Regions.MushroomUpper, Exits.ForestLowerExteriorToUpperMushroom, ExitCategories.ForestMushroom),
    Exits.ForestUpperExteriorToUpperMushroom: ShufflableExit("Fungi Forest Upper Exterior to Upper Mushroom", Regions.MushroomUpperExterior, Exits.ForestUpperMushroomToUpperExterior, ExitCategories.ForestExterior),
    Exits.ForestUpperMushroomToUpperExterior: ShufflableExit("Fungi Forest Upper Mushroom to Upper Exterior", Regions.MushroomUpper, Exits.ForestUpperExteriorToUpperMushroom, ExitCategories.ForestMushroom),
    Exits.ForestExteriorToNight: ShufflableExit("Fungi Forest Night Exterior to Night Door", Regions.MushroomNightExterior, Exits.ForestNightToExterior, ExitCategories.ForestExterior),
    Exits.ForestNightToExterior: ShufflableExit("Fungi Forest Night Door to Night Exterior", Regions.MushroomNightDoor, Exits.ForestExteriorToNight, ExitCategories.ForestMushroom),
    Exits.ForestExteriorToChunky: ShufflableExit("Fungi Forest Upper Exterior to Chunky Room", Regions.MushroomUpperExterior, Exits.ForestChunkyToExterior, ExitCategories.ForestExterior),
    Exits.ForestChunkyToExterior: ShufflableExit("Fungi Forest Chunky Room to Upper Exterior", Regions.MushroomChunkyRoom, Exits.ForestExteriorToChunky),
    Exits.ForestExteriorToZingers: ShufflableExit("Fungi Forest Upper Exterior to Zinger Room", Regions.MushroomUpperExterior, Exits.ForestZingersToExterior, ExitCategories.ForestExterior),
    Exits.ForestZingersToExterior: ShufflableExit("Fungi Forest Zinger Room to Upper Exterior", Regions.MushroomLankyZingersRoom, Exits.ForestExteriorToZingers),
    Exits.ForestExteriorToMushrooms: ShufflableExit("Fungi Forest Upper Exterior to Mushroom Room", Regions.MushroomUpperExterior, Exits.ForestMushroomsToExterior, ExitCategories.ForestExterior),
    Exits.ForestMushroomsToExterior: ShufflableExit("Fungi Forest Mushroom Room to Upper Exterior", Regions.MushroomLankyMushroomsRoom, Exits.ForestExteriorToMushrooms),
    Exits.ForestTreeToAnthill: ShufflableExit("Fungi Forest Hollow Tree Area to Anthill", Regions.HollowTreeArea, Exits.ForestAnthillToTree, ExitCategories.ForestExterior),
    Exits.ForestAnthillToTree: ShufflableExit("Fungi Forest Anthill to Hollow Tree Area", Regions.Anthill, Exits.ForestTreeToAnthill),
    Exits.ForestMainToChunkyMill: ShufflableExit("Fungi Forest Main to Mill Chunky Door", Regions.MillArea, Exits.ForestChunkyMillToMain, ExitCategories.ForestExterior),
    Exits.ForestChunkyMillToMain: ShufflableExit("Fungi Forest Mill Chunky Door to Mill", Regions.MillChunkyArea, Exits.ForestMainToChunkyMill, ExitCategories.ForestMill),
    Exits.ForestMainToTinyMill: ShufflableExit("Fungi Forest Main to Mill Tiny Entrance", Regions.MillArea, Exits.ForestTinyMillToMain, ExitCategories.ForestExterior),
    Exits.ForestTinyMillToMain: ShufflableExit("Fungi Forest Mill Tiny Entrance to Main", Regions.MillTinyArea, Exits.ForestMainToTinyMill, ExitCategories.ForestMill),
    Exits.ForestMainToGrinder: ShufflableExit("Fungi Forest Main to Grinder Room", Regions.MillArea, Exits.ForestGrinderToMain, ExitCategories.ForestExterior),
    Exits.ForestGrinderToMain: ShufflableExit("Fungi Forest Grinder Room to Main", Regions.GrinderRoom, Exits.ForestMainToGrinder, ExitCategories.ForestGrinder),
    Exits.ForestMainToRafters: ShufflableExit("Fungi Forest Main to Rafters", Regions.MillArea, Exits.ForestRaftersToMain, ExitCategories.ForestExterior),
    Exits.ForestRaftersToMain: ShufflableExit("Fungi Forest Rafters to Main", Regions.MillRafters, Exits.ForestMainToRafters),
    Exits.ForestMainToWinch: ShufflableExit("Fungi Forest Main to Winch Room", Regions.MillArea, Exits.ForestWinchToMain, ExitCategories.ForestExterior),
    Exits.ForestWinchToMain: ShufflableExit("Fungi Forest Winch Room to Main", Regions.WinchRoom, Exits.ForestMainToWinch),
    Exits.ForestMainToAttic: ShufflableExit("Fungi Forest Main to Mill Attic", Regions.MillArea, Exits.ForestAtticToMain, ExitCategories.ForestExterior),
    Exits.ForestAtticToMain: ShufflableExit("Fungi Forest Mill Attic to Main", Regions.MillAttic, Exits.ForestMainToAttic),
    Exits.ForestTinyMillToSpider: ShufflableExit("Fungi Forest Mill to Spider Boss", Regions.MillTinyArea, Exits.ForestSpiderToTinyMill, ExitCategories.ForestMill),
    Exits.ForestSpiderToTinyMill: ShufflableExit("Fungi Forest Spider Boss to Mill", Regions.SpiderRoom, Exits.ForestTinyMillToSpider),
    Exits.ForestTinyMillToGrinder: ShufflableExit("Fungi Forest Tiny Entrance to Grinder Room", Regions.MillTinyArea, Exits.ForestGrinderToTinyMill, ExitCategories.ForestMill),
    Exits.ForestGrinderToTinyMill: ShufflableExit("Fungi Forest Grinder Room to Tiny Entrance", Regions.GrinderRoom, Exits.ForestTinyMillToGrinder, ExitCategories.ForestGrinder),
    Exits.ForestMainToBarn: ShufflableExit("Fungi Forest Main to Thornvine Barn", Regions.ThornvineArea, Exits.ForestBarnToMain, ExitCategories.ForestExterior),
    Exits.ForestBarnToMain: ShufflableExit("Fungi Forest Thornvine Barn to Main", Regions.ThornvineBarn, Exits.ForestMainToBarn),
    # Crystal Caves Exits
    Exits.CavesMainToRace: ShufflableExit("Crystal Caves Main to Beetle Race", Regions.CrystalCavesMain, Exits.CavesRaceToMain, ExitCategories.CavesExterior),
    Exits.CavesRaceToMain: ShufflableExit("Crystal Caves Beetle Race to Main", Regions.CavesLankyRace, Exits.CavesMainToRace),
    Exits.CavesMainToCastle: ShufflableExit("Crystal Caves Main to Frozen Castle", Regions.CrystalCavesMain, Exits.CavesCastleToMain, ExitCategories.CavesExterior),
    Exits.CavesCastleToMain: ShufflableExit("Crystal Caves Frozen Castle to Main", Regions.FrozenCastle, Exits.CavesMainToCastle),
    Exits.CavesIglooToDonkey: ShufflableExit("Crystal Caves Main to Donkey 5DI", Regions.IglooArea, Exits.CavesDonkeyToIgloo, ExitCategories.CavesExterior),
    Exits.CavesDonkeyToIgloo: ShufflableExit("Crystal Caves Donkey 5DI to Main", Regions.DonkeyIgloo, Exits.CavesIglooToDonkey),
    Exits.CavesIglooToDiddy: ShufflableExit("Crystal Caves Main to Diddy 5DI", Regions.IglooArea, Exits.CavesDiddyToIgloo, ExitCategories.CavesExterior),
    Exits.CavesDiddyToIgloo: ShufflableExit("Crystal Caves Diddy 5DI to Main", Regions.DiddyIgloo, Exits.CavesIglooToDiddy),
    Exits.CavesIglooToLanky: ShufflableExit("Crystal Caves Main to Lanky 5DI", Regions.IglooArea, Exits.CavesLankyToIgloo, ExitCategories.CavesExterior),
    Exits.CavesLankyToIgloo: ShufflableExit("Crystal Caves Lanky 5DI to Main", Regions.LankyIgloo, Exits.CavesIglooToLanky),
    Exits.CavesIglooToTiny: ShufflableExit("Crystal Caves Main to Tiny 5DI", Regions.IglooArea, Exits.CavesTinyToIgloo, ExitCategories.CavesExterior),
    Exits.CavesTinyToIgloo: ShufflableExit("Crystal Caves Tiny 5DI to Main", Regions.TinyIgloo, Exits.CavesIglooToTiny),
    Exits.CavesIglooToChunky: ShufflableExit("Crystal Caves Main to Chunky 5DI", Regions.IglooArea, Exits.CavesChunkyToIgloo, ExitCategories.CavesExterior),
    Exits.CavesChunkyToIgloo: ShufflableExit("Crystal Caves Chunky 5DI to Main", Regions.ChunkyIgloo, Exits.CavesIglooToChunky),
    Exits.CavesCabinToRotating: ShufflableExit("Crystal Caves Main to Rotating Cabin", Regions.CabinArea, Exits.CavesRotatingToCabin, ExitCategories.CavesExterior),
    Exits.CavesRotatingToCabin: ShufflableExit("Crystal Caves Rotating Cabin to Main", Regions.RotatingCabin, Exits.CavesCabinToRotating),
    Exits.CavesCabinToDonkey: ShufflableExit("Crystal Caves Main to Donkey 5DC", Regions.CabinArea, Exits.CavesDonkeyToCabin, ExitCategories.CavesExterior),
    Exits.CavesDonkeyToCabin: ShufflableExit("Crystal Caves Donkey 5DC to Main", Regions.DonkeyCabin, Exits.CavesCabinToDonkey),
    Exits.CavesCabinToDiddyLower: ShufflableExit("Crystal Caves Main to Diddy Lower 5DC", Regions.CabinArea, Exits.CavesDiddyLowerToCabin, ExitCategories.CavesExterior),
    Exits.CavesDiddyLowerToCabin: ShufflableExit("Crystal Caves Diddy Lower 5DC to Main", Regions.DiddyLowerCabin, Exits.CavesCabinToDiddyLower),
    Exits.CavesCabinToDiddyUpper: ShufflableExit("Crystal Caves Main to Diddy Upper 5DC", Regions.CabinArea, Exits.CavesDiddyUpperToCabin, ExitCategories.CavesExterior),
    Exits.CavesDiddyUpperToCabin: ShufflableExit("Crystal Caves Diddy Upper 5DC to Main", Regions.DiddyUpperCabin, Exits.CavesCabinToDiddyUpper),
    Exits.CavesCabinToLanky: ShufflableExit("Crystal Caves Main to Lanky 1DC", Regions.CabinArea, Exits.CavesLankyToCabin, ExitCategories.CavesExterior),
    Exits.CavesLankyToCabin: ShufflableExit("Crystal Caves Lanky 1DC to Main", Regions.LankyCabin, Exits.CavesCabinToLanky),
    Exits.CavesCabinToTiny: ShufflableExit("Crystal Caves Main to Tiny 5DC", Regions.CabinArea, Exits.CavesTinyToCabin, ExitCategories.CavesExterior),
    Exits.CavesTinyToCabin: ShufflableExit("Crystal Caves Tiny 5DC to Main", Regions.TinyCabin, Exits.CavesCabinToTiny),
    Exits.CavesCabinToChunky: ShufflableExit("Crystal Caves Main to Chunky 5DC", Regions.CabinArea, Exits.CavesChunkyToCabin, ExitCategories.CavesExterior),
    Exits.CavesChunkyToCabin: ShufflableExit("Crystal Caves Chunky 5DC to Main", Regions.ChunkyCabin, Exits.CavesCabinToChunky),
    # Creepy Castle Exits
    Exits.CastleMainToTree: ShufflableExit("Creepy Castle Main to Tree", Regions.CreepyCastleMain, Exits.CastleTreeToMain, ExitCategories.CastleExterior),
    Exits.CastleTreeToMain: ShufflableExit("Creepy Castle Tree to Main", Regions.CastleTree, Exits.CastleMainToTree),
    Exits.CastleMainToLibrary: ShufflableExit("Creepy Castle Main to Library", Regions.CreepyCastleMain, Exits.CastleLibraryToMain, ExitCategories.CastleExterior),
    Exits.CastleLibraryToMain: ShufflableExit("Creepy Castle Library to Main", Regions.Library, Exits.CastleMainToLibrary),
    Exits.CastleMainToBallroom: ShufflableExit("Creepy Castle Main to Ballroom", Regions.CreepyCastleMain, Exits.CastleBallroomToMain, ExitCategories.CastleExterior),
    Exits.CastleBallroomToMain: ShufflableExit("Creepy Castle Ballroom to Main", Regions.Ballroom, Exits.CastleMainToBallroom, ExitCategories.CastleBallroom),
    Exits.CastleMainToTower: ShufflableExit("Creepy Castle Main to Tower", Regions.CreepyCastleMain, Exits.CastleTowerToMain, ExitCategories.CastleExterior),
    Exits.CastleTowerToMain: ShufflableExit("Creepy Castle Tower to Main", Regions.Tower, Exits.CastleMainToTower),
    Exits.CastleMainToGreenhouse: ShufflableExit("Creepy Castle Main to Greenhouse", Regions.CreepyCastleMain, Exits.CastleGreenhouseToMain, ExitCategories.CastleExterior),
    Exits.CastleGreenhouseToMain: ShufflableExit("Creepy Castle Greenhouse to Main", Regions.Greenhouse, Exits.CastleMainToGreenhouse),
    Exits.CastleMainToTrash: ShufflableExit("Creepy Castle Main to Trash Can", Regions.CreepyCastleMain, Exits.CastleTrashToMain, ExitCategories.CastleExterior),
    Exits.CastleTrashToMain: ShufflableExit("Creepy Castle Trash Can to Main", Regions.TrashCan, Exits.CastleMainToTrash),
    Exits.CastleMainToShed: ShufflableExit("Creepy Castle Main to Shed", Regions.CreepyCastleMain, Exits.CastleShedToMain, ExitCategories.CastleExterior),
    Exits.CastleShedToMain: ShufflableExit("Creepy Castle Shed to Main", Regions.Shed, Exits.CastleMainToShed),
    Exits.CastleMainToMuseum: ShufflableExit("Creepy Castle Main to Museum", Regions.CreepyCastleMain, Exits.CastleMuseumToMain, ExitCategories.CastleExterior),
    Exits.CastleMuseumToMain: ShufflableExit("Creepy Castle Museum to Main", Regions.Museum, Exits.CastleMainToMuseum),
    Exits.CastleMainToLower: ShufflableExit("Creepy Castle Main to Lower Cave", Regions.CreepyCastleMain, Exits.CastleLowerToMain, ExitCategories.CastleExterior),
    Exits.CastleLowerToMain: ShufflableExit("Creepy Castle Lower Cave to Main", Regions.LowerCave, Exits.CastleMainToLower, ExitCategories.CastleLower),
    Exits.CastleMainToUpper: ShufflableExit("Creepy Castle Main to Upper Cave", Regions.CreepyCastleMain, Exits.CastleUpperToMain, ExitCategories.CastleExterior),
    Exits.CastleUpperToMain: ShufflableExit("Creepy Castle Upper Cave to Main", Regions.UpperCave, Exits.CastleMainToUpper, ExitCategories.CastleUpper),
    Exits.CastleWaterfallToUpper: ShufflableExit("Creepy Castle Waterfall to Upper Cave", Regions.CastleWaterfall, Exits.CastleUpperToWaterfall, ExitCategories.CastleExterior),
    Exits.CastleUpperToWaterfall: ShufflableExit("Creepy Castle Upper Cave to Waterfall", Regions.UpperCave, Exits.CastleWaterfallToUpper, ExitCategories.CastleUpper),
    Exits.CastleBallroomToRace: ShufflableExit("Creepy Castle Ballroom to Car Race", Regions.Ballroom, Exits.CastleRaceToBallroom, ExitCategories.CastleBallroom),
    Exits.CastleRaceToBallroom: ShufflableExit("Creepy Castle Car Race to Ballroom", Regions.CastleTinyRace, Exits.CastleBallroomToRace),
    Exits.CastleLowerToCrypt: ShufflableExit("Creepy Castle Lower Cave to Crypt", Regions.LowerCave, Exits.CastleCryptToLower, ExitCategories.CastleLower),
    Exits.CastleCryptToLower: ShufflableExit("Creepy Castle Crypt to Lower Cave", Regions.Crypt, Exits.CastleLowerToCrypt, ExitCategories.CastleCrypt),
    Exits.CastleLowerToMausoleum: ShufflableExit("Creepy Castle Lower Cave to Mausoleum", Regions.LowerCave, Exits.CastleMausoleumToLower, ExitCategories.CastleLower),
    Exits.CastleMausoleumToLower: ShufflableExit("Creepy Castle Mausoleum to Lower cave", Regions.Mausoleum, Exits.CastleLowerToMausoleum),
    Exits.CastleCryptToCarts: ShufflableExit("Creepy Castle Crypt to Minecarts", Regions.Crypt, Exits.CastleCartsToCrypt, ExitCategories.CastleCrypt),
    Exits.CastleCartsToCrypt: ShufflableExit("Creepy Castle Minecarts to Crypt", Regions.CastleMinecarts, Exits.CastleCryptToCarts),
    Exits.CastleUpperToDungeon: ShufflableExit("Creepy Castle Upper Cave to Dungeon", Regions.UpperCave, Exits.CastleDungeonToUpper, ExitCategories.CastleUpper),
    Exits.CastleDungeonToUpper: ShufflableExit("Creepy Castle Dungeon to Upper Cave", Regions.Dungeon, Exits.CastleUpperToDungeon),
}
