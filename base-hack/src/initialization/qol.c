/**
 * @file qol.c
 * @author Ballaam
 * @brief Initialize Quality of Life features
 * @version 0.1
 * @date 2023-01-17
 * 
 * @copyright Copyright (c) 2023
 * 
 */
#include "../../include/common.h"

void disableAntiAliasing(void) {
    __osViSwapContext();
    int disable_antialiasing = Rando.quality_of_life.reduce_lag;
    if (Rando.quality_of_life.fast_boot) {
        if (CurrentMap == MAP_NINTENDOLOGO) {
            disable_antialiasing = 1;
        }
    } else if (FrameReal < 230) {
        disable_antialiasing = 1;
    }
    if (disable_antialiasing) {
        *(int*)(0x8001013C) = 0x3216;
        *(int*)(0x8001016C) = 0x3216;
    }
}

typedef struct skipped_cutscene {
    /* 0x000 */ unsigned char map;
    /* 0x001 */ unsigned char cutscene;
} skipped_cutscene;

void initQoL_Cutscenes(void) {
    /**
     * @brief Initialize any quality of life features which aim to reduce the amount of cutscenes inside DK64
     * Current Elements covered here:
     * - Compressing all key turn in cutscenes in K. Lumsy
     * - Removing the 30s cutscene for freeing the Vulture in Angry Aztec
     * - Adding cutscenes for Item Rando back in if deemed important enough
     */
    if (Rando.cutscene_skip_setting == CSSKIP_OFF) {
        // Clear the cutscene skip database
        for (int i = 0; i < 432; i++) {
            cs_skip_db[i] = 0;
        }
    } else {
        if (Rando.item_rando) {
            skipped_cutscene cs_unskip[] = {
                {.map=MAP_FACTORY, .cutscene=2}, // Diddy Prod Spawn
                {.map=MAP_FACTORY, .cutscene=3}, // Tiny Prod Peek
                {.map=MAP_FACTORY, .cutscene=4}, // Lanky Prod Peek
                {.map=MAP_FACTORY, .cutscene=5}, // Chunky Prod Spawn
                {.map=MAP_AZTEC, .cutscene=14}, // Free Llama
                {.map=MAP_FUNGIGIANTMUSHROOM, .cutscene=0}, // Tiny Barrel Spawn
                {.map=MAP_FUNGIGIANTMUSHROOM, .cutscene=1}, // Cannon GB Spawn
                {.map=MAP_CASTLEGREENHOUSE, .cutscene=0}, // Greenhouse Intro
                {.map=MAP_CASTLEDUNGEON, .cutscene=0}, // Dungeon Lanky Trombone Bonus
            };
            for (int i = 0; i < (sizeof(cs_unskip) / sizeof(skipped_cutscene)); i++) {
                int cs_offset = 0;
                int cs_val = cs_unskip[i].cutscene;
                int cs_map = cs_unskip[i].map;
                int shift = cs_val % 31;
                if (cs_val > 31) {
                    cs_offset = 1;
                }
                int comp = 0xFFFFFFFF - (1 << shift);
                cs_skip_db[(2 * cs_map) + cs_offset] &= comp;
            }
        }
        writeFunction(0x80628508, &renderScreenTransitionCheck); // Remove transition effects if skipped cutscene
        if (Rando.cutscene_skip_setting == CSSKIP_PRESS) {
            writeFunction(0x8061DD80, &pressSkipHandler); // Handler for press start to skip
        }
    }
    if (Rando.quality_of_life.remove_cutscenes) {
        // K. Lumsy
        *(short*)(0x80750680) = MAP_ISLES;
        *(short*)(0x80750682) = 0x1;
        *(int*)(0x806BDC24) = 0x0C17FCDE; // Change takeoff warp func
        *(short*)(0x806BDC8C) = 0x1000; // Apply no cutscene to all keys
        *(short*)(0x806BDC3C) = 0x1000; // Apply shorter timer to all keys
        // Fast Vulture
        writeFunction(0x806C50BC, &clearVultureCutscene); // Modify Function Call
        // Speedy T&S Turn-Ins
        *(int*)(0x806BE3E0) = 0; // NOP
        // Remove final mermaid text
        *(int*)(0x806C3E10) = 0;
        *(int*)(0x806C3E20) = 0;
    }
}

void fixRaceHoopCode(void) {
    unkProjectileCode_3(CurrentActorPointer_0, 0);
}

void renderHoop(void) {
    unkBonusFunction(CurrentActorPointer_0);
    CurrentActorPointer_0->rot_x -= 0x39; // Rotate Hoop
    renderActor(CurrentActorPointer_0, 0);
}

void quickWrinklyTextboxes(void) {
    /**
     * @brief Speeds up the wrinkly textboxes by setting the textbox timer to 0x1e upon init if A is pressed
     */
    if (CurrentActorPointer_0->control_state == 0) {
        if (NewlyPressedControllerInput.Buttons.a) {
            short* paad = CurrentActorPointer_0->paad;
            *paad = 0x1E;
        }
    }
    unkTextFunction(CurrentActorPointer_0);
}

static char boot_speedup_done = 0;
void bootSpeedup(void) {
    /**
     * @brief Speed up the boot process by reducing the amount of setups the game is loading
     */
    if (!boot_speedup_done) {
		boot_speedup_done = 1;
		int balloon_patch_count = 0;
		for (int j = 0; j < 8; j++) {
			coloredBananaCounts[j] = 0;
		}
		int patch_index = 0;
        int crate_index = 0;
		for (int i = 0; i < 221; i++) {
			balloonPatchCounts[i] = balloon_patch_count;
			int* setup = getMapData(TABLE_MAP_SETUPS,i,1,1);
			char* modeltwo_setup = 0;
			char* actor_setup = 0;
			if (setup) {
				int world = getWorld(i,1);
				getModel2AndActorInfo(setup,(int**)&modeltwo_setup,(int**)&actor_setup);
				int model2_count = *(int*)(modeltwo_setup);
				int actor_count = *(int*)(actor_setup);
				char* focused_actor = (char*)(actor_setup + 4);
				char* focused_model2 = (char*)(modeltwo_setup + 4);
                int subworld = LEVEL_ISLES;
                if (!isLobby(i)) {
                    subworld = levelIndexMapping[i];
                }
				if (actor_count > 0) {
					for (int j = 0; j < actor_count; j++) {
						int actor = *(short*)((int)focused_actor + 0x32) + 0x10;
						balloon_patch_count += isBalloonOrPatch(actor);
						if (actor == 139) {
                            populatePatchItem(*(short*)((int)focused_actor + 0x34), i, patch_index, subworld);
							patch_index += 1;
						}
						focused_actor += 0x38;
					}
				}
				if (model2_count > 0) {
					for (int j = 0; j < model2_count; j++) {
                        unsigned short m2_obj_type = *(unsigned short*)(focused_model2 + 0x28);
						coloredBananaCounts[world] += isSingleOrBunch(m2_obj_type);
                        if (m2_obj_type == 181) {
                            populateCrateItem(*(short*)((int)focused_model2 + 0x2A), i, crate_index, subworld);
                            crate_index += 1;
                        }
						focused_model2 += 0x30;
					}
				}
				enableComplexFree();
				complexFreeWrapper(setup);
			}
		}
	}
}

void initQoL_FastWarp(void) {
    /**
     * @brief Initialize any quality of life features which speed up bananaporting
     */
    if (Rando.fast_warp) {
        // Replace vanilla warp animation (0x52) with monkeyport animation (0x53)
        *(short*)(0x806EE692) = 0x54;
        writeFunction(0x806DC2AC, &fastWarp); // Modify Function Call
        if (!Rando.disabled_music.chunk_songs) {
            writeFunction(0x806DC318, &fastWarp_playMusic); // Modify Function Call
        }
    }
}

static const char exittoisles[] = "EXIT TO ISLES";
static const char exittospawn[] = "EXIT TO SPAWN";

void initSpawn(void) {
    /**
     * @brief Initialize the world spawning procedure
     */
    // Starting map rando
    int starting_map_rando_on = 1;
    if (Rando.starting_map == 0) {
        // Default
        Rando.starting_map = MAP_ISLES;
        Rando.starting_exit = 0;
        starting_map_rando_on = 0;
    } else {
        *(short*)(0x8071454A) = Rando.starting_map;
        *(int*)(0x80714550) = 0x24050000 | Rando.starting_exit;
    }
    setPrevSaveMap();
    if (Rando.warp_to_isles_enabled) {
        if (!starting_map_rando_on) {
            PauseSlot3TextPointer = (char*)&exittoisles;
        } else {
            PauseSlot3TextPointer = (char*)&exittospawn;
        }
    }
}

void initNonControllableFixes(void) {
    /**
     * @brief Initialize any changes which we do not want to give the user any control over whether it's removed
     */
    // Inverted Controls Option
    *(short*)(0x8060D01A) = getHi(&InvertedControls); // Change language store to inverted controls store
    *(short*)(0x8060D01E) = getLo(&InvertedControls); // Change language store to inverted controls store
}

void QoL_DisplayInstrument(void* handler, int x, int y, int unk0, int unk1, int count, int unk2, int unk3) {
    displayPauseSpriteNumber(handler, x, y, unk0, unk1, CollectableBase.InstrumentEnergy, unk2, unk3);
}

void HeadphonesCodeContainer(void) {
    int has_headphones = 0;
    for (int kong = 0; kong < 5; kong++) {
        if (MovesBase[kong].instrument_bitfield & 1) {
            has_headphones = 1;
        }
    }
    headphonesCode(0, has_headphones);
}

int newInstrumentRefill(int item, int player_index) {
    int refill_count = getRefillCount(item, player_index);
    if (refill_count > 0) {
        CollectableBase.InstrumentEnergy = refill_count >> 1;
    }
    return refill_count;
}

int getInstrumentRefillCount(void) {
    for (int i = 0; i < 5; i++) {
        int btf = MovesBase[i].instrument_bitfield;
        if (btf & 1) {
            int refill_mult = 1;
            while (btf != 0) {
                btf >>= 1;
                refill_mult += 1;
            }
            return refill_mult * 5;
        }
    }
    return 0;
}

int correctRefillCap(int index, int player) {
    if (index == 7) {
        // Instrument
        return getInstrumentRefillCount();
    }
    return getRefillCount(index, player);
}

void initQoL(void) {
    /**
     * @brief Initialize all quality of life functionality
     */
    writeFunction(0x80004EB4, &disableAntiAliasing); // Disable Anti-Aliasing
    initQoL_Cutscenes();
    initSpawn();
    initQoL_FastWarp();
    initNonControllableFixes();
}