
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0) 
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLUE_GREEN = (0, 255, 255)
VIOLET = (175, 0, 175)
GRAY = (150, 150, 150) # Example hero color
GOLD = (180, 150, 25)
HIGHLIGHTGREEN = (0, 255, 0, 128)
#(self, 0name, 1x, 2y, 3color, 4size = (1, 1), 5height. 6health = 8000, 7shields = 0, 8movement = 5,
        #                9jump = 2, 10jump_type = "jump", 11clamber = 0, 12attack_range = 1):

# Spawning heroes, used in tandem with the start button      

spawnable_heroes = [["Agarthan Wastebringer",       0, 0, BLACK, (1,1),1, 8000, 0, 5, 2, "jump", 0, 3],
                ["Apollonian Grenadier",            0, 0, BLUE, (1,1), 1, 8000, 0, 4, 2, "jump", 0, 4],
               ["Apollonian Swordmaster",           0, 0, BLUE, (1,1),1,  8000, 0, 5, 2, "jump", 0, 2],
               ["Apollonian Tank",                  0, 0, BLUE, (1,1),1,  12000, 0, 3, 0, "clamber", 1, 1],
               ["Aquilan Dipped Sword Dancer" ,     0, 0, RED, (1,1),1,   6000, 0, 5, 1, "clamber", 4, 1],
               ["Aquilan Energy Technician",        0, 0, RED, (1,1),1,   8500, 600, 5, 2, "fly", 0, 1],
               ["Aquilan Tempest",                  0, 0, RED, (1,1),1,   8000, 0, 4, 1, "jump", 0, 3],
               ["Biologic Amplifier",               0, 0, GREEN, (1,1),1, 7000, 0, 5, 1, "jump", 0, 1],
               ["Gothmaug Marauder",                0, 0, GOLD, (2,2),1,  12000, 400, 5, 1, "glide", 1, 1],
               ["Iksnik Hivemind",                  0, 0, GOLD, (1,1), 1, 4000, 0, 3, 1, "clamber", 4, 1],
               ["Leonid Carrier",                   0, 0, YELLOW,(1,1),1, 9000, 0, 5, 1, "jump", 1, 1],
               ["Leonid Commandant",                0, 0, YELLOW,(1,1),1, 8500, 0, 4, 1, "clamber", 0, 2],
               ["Leonid Lieutenant",                0, 0, YELLOW,(1,1),1, 8000, 0, 5, 1, "clamber", 1, 1],
               #The Hivemind is a set of 3 heroes, will be tough 
               ["Molochite All-Mother",             0, 0, ORANGE,(1,1), 1, 8000, 0, 4, 2, "jump", 0, 5],
               ["Molochite Quarantine Runner",      0, 0, ORANGE,(1,1), 1, 8000, 0, 4, 2, "jump", 0, 4],
               ["Molochite Weapons Technician",     0, 0, ORANGE, (1,1), 1, 8000, 500, 3, 2, "jump", 0, 7],
               ["Mogwai Mass Mystic",               0, 0, GRAY, (2,2), 1, 15000, 0, 3, 0, "clamber", 3, 1],
               ["Normanus World-Bearer",            0, 0, GRAY, (2,2), 1, 10000, 0, 5, 0, "clamber", 1, 1],
               ["Saturni Reaper",                   0, 0, GRAY, (2,2), 1, 8000, 0, 5, 1, "clamber", 1, 1],
               ["Selene Femmentalist",              0, 0, BLUE_GREEN, (1,1), 1, 7500, 0, 5, 2, "jump", 0, 1],
               ["Selene Master Weavemaker",         0, 0, BLUE_GREEN, (1,1), 1, 9000, 500, 5, 1, "jump", 0, 1],
               ["Selene Perfectionist",             0, 0, BLUE_GREEN, (1,1), 1,6500, 0, 6, 1, "clamber", 2, 1],
               #The phase walker transforms, will be tough to code
               ["The Phase Walker",                 0, 0, GREEN, (1,1), 1, 8000, 0, 5, 2, "jump", 0, 5],
               #The spore splits into multiple parts, will be tough to code
               ["The Spore",                        0, 0, GREEN, (1,1), 1, 5000, 0, 3, 0, "clamber", 1, 3],
               ["Urik La",                          0, 0, VIOLET, (1,1), 1, 7500, 0, 4, 2, "hover", 0, 3],
               ["Urik Mimic",                       0, 0, VIOLET, (1,1), 1, 8000, 0, 4, 2, "jump", 0, 1],
               ["Urik Ra",                          0, 0, VIOLET, (1,1), 1, 10000, 0, 5, 2, "jump", 0, 1],
               ["Verouk Shadow",                    0, 0, GOLD, (1,1), 1, 8000, 0, 5, 1, "clamber", 1, 1],
               ["Volucris Bullet Beak",             0, 0, BLACK, (1,1), 1, 6000, 0, 5, 3, "fly", 0, 1],
               ["Volucris Dart Thrower",            0, 0, BLACK, (1,1), 1, 8000, 0, 7, 3, "fly", 0, 3],
               ["Volucris Salter",                  0, 0, BLACK, (1,1), 1, 8600, 0, 6, 2, "glide", 0, 1]
               ]

herocard_decks = [



                                                            #0attack, 1double attack, 2defense, 3counterattack, 4damage, 5counterdamage, 6heal, 7burn, 8radiation, trap, trapactivations
                                                                                                                #spc/acti: 5attack, 6double attack, 7defense, 8counterattack, 9damage, 10counterdamage, 11heal, 12burn, 13radiation, 14 trap, 15 trapactivations, 16 specialstuff, 17 standalone, 18 range, 
                    #combat:   4attack, 5double attack, 6defense, 7counterattack, 8damage, 9counterdamage, 10heal, 11burn, 12radiation, 13 trap, 14 trap activation, 15 specialstuff, 16 standalone, 17 range, 

                    ["Agarthan Wastebringer", "action", "Illusive Intent","Playable with an attack.  The defender must make two separate defenses.  The Wastebringer chooses which defense is used", 2, None, None, None, None, None, None, None, None, None, False, None, True, False, (3,0)],
                    ["Agarthan Wastebringer", "special", "Rule-Breaker",  "Played as a trap attack card with attack value 3200 and two activations.  ", 2, 3200, None, None, None, None, None, None, None, None, True, 2, None, False, (3,0)],
                    ["Agarthan Wastebringer", "special", "Waste", "Playable after an attack that deals damage or a defense in which no damage was taken.  Return your card to your hand", 3, None, None, None, None, None, None, None, None, None, False, None, True, False, (25,0)],
                    ["Agarthan Wastebringer", "special", "Equivalent Exchange", "Discard 2 cards.  Draw 2 cards.", 3, None, None, None, None, None, None, None, None, None, False, None, True, False, (25,0)],
                    ["Agarthan Wastebringer", "special", "Famine", "Playable anytime.  You and a target discard your hands and draw 4.", 2, None, None, None, None, None, None, None, None, None, False, None, True, False, (25,0)],

                    ["Agarthan Wastebringer", "combat", "2700/0", 2  , 2700, None, 0, None, None, None, None, None, None, False, None, False, False, (3,0)],
                    ["Agarthan Wastebringer", "combat", "2400/300", 6, 2400, None, 300, None, None, None, None, None, None, False, None, False, False, (3,0)],
                    ["Agarthan Wastebringer", "combat", "800/1900", 5, 800, None, 1900, None, None, None, None, None, None, False, None, False, False, (3,0)],
                    ["Agarthan Wastebringer", "combat", "600/2100", 4, 600, None, 2100, None, None, None, None, None, None, False, None, False, False, (3,0)],
                    ["Agarthan Wastebringer", "combat", "400/2300", 3, 400, None, 2300, None, None, None, None, None, None, False, None, False, False, (3,0)],


                    ["Apollonian Grenadier", "action", "Ionized Plutonium Dart",  "Playable as a stand-alone attack with range 3, Attack = 3000.  The enemy rolls a D(20).  1-5: Att (+700), 6-10: (200)^2 rad damage, 11-15: Attack (+300), 16-18: All 3 effects, 19-20: No Effects", 2, 3000, None, None, None, None, None, None, None, None, False, None, True, True, (3,0)],
                    ["Apollonian Grenadier", "action", "Stimulant Grenade", "Playable as a stand-alone attack with range 5.  Effects all adjacent to target.  Att/Def (+500), Move (+1), Draw (+1), clamber.The enemy rolls a D(20).  1-5: Att/Def (+500), 6-10: Move (+1), 11-15: Draw +1, 16-18: All 3 effects, 19-20: No effects", 2, None, None, None, None, None, None, None, None, None, False, None, True, True, (5,0)],
                    ["Apollonian Grenadier", "action", "Thermobaric Detonator", "Playable as a stand-alone attack with range 5.  Effects all adjacent to target.  Attack = (1500).  The enemy rolls a D(20).  1-5: Att/Def (+500), 6-10: Move (+1), 11-15: Draw +1, 16-18: All 3 effects, 19-20: No effects", 3, 1500, None, None, None, None, None, None, None, None, False, None, True, True, (5,0)],
                    ["Apollonian Grenadier", "special", "Cryogenic Grenade",  "Playable as a stand-alone attack with range 5.  Effects all adjacent to target.  Attack = (500), Move (-1).  The enemy rolls a D(20).  1-5: Attack (+300), 6-10: Move (-1), 11-15: -1 action next turn, 16-18: All 3 effects, 19-20: No effects", 3, 500, None, None, None, None, None, None, None, None, False, None, True, True, (5,0)],
                    ["Apollonian Grenadier", "special", "Perks of Mercs", "Playable anytime.  If played when an enemy has more cards than you draw 3.  If not draw 2.", 2, None, None, None, None, None, None, None, None, None, False, None, True, False, (25,0)],

                    ["Apollonian Grenadier", "combat", "2000/700", 3, 2000, None, 700, None, None, None, None, None, None, False, None, False, False, (4, 0)],
                    ["Apollonian Grenadier", "combat", "1900/800", 4, 1900, None, 800, None, None, None, None, None, None, False, None, False, False, (4, 0)],
                    ["Apollonian Grenadier", "combat", "1800/900", 4, 1800, None, 900, None, None, None, None, None, None, False, None, False, False, (4, 0)],
                    ["Apollonian Grenadier", "combat", "700/2000", 3, 700, None, 2000, None, None, None, None, None, None, False, None, False, False, (4, 0)],
                    ["Apollonian Grenadier", "combat", "600/2100", 3, 600, None, 2100, None, None, None, None, None, None, False, None, False, False, (4, 0)],
                    ["Apollonian Grenadier", "combat", "500/2200", 3, 500, None, 2200, None, None, None, None, None, None, False, None, False, False, (4, 0)],


                    ["Apollonian Swordmaster", "action", "Servant of the Blue Sun", "Playable with a defensive round.  Defense +(1000).", 3, None, None, 1000, None, None, None, None, None, None, False, None, True, False, (25, 0)],
                    ["Apollonian Swordmaster", "special", "Servant of the Red Sun", "Playable after a combat round has occured but before damage is counted.  Target defense -800", 3, None, None, None, None, None, None, None, None, None, False, None, True, False, (25, 0)],
                    ["Apollonian Swordmaster", "action", "Extended Reach", "Playable with an attack.  Attack +(500), Range = 3.", 2, 500, None, None, None, None, None, None, None, None, False, None, False, False, (3, 0)],
                    ["Apollonian Swordmaster", "special", "Vault",  "Playable while moving.  Jump = 3 + clamber", 2, None, None, None, None, None, None, None, None, None, False, None, True, False, (25, 0)],
                    ["Apollonian Swordmaster", "special", "Bide",  "Playable as an attack.  This is your last attack this turn.  Draw 1.  Increase attack +(500) next turn.", 2, 500, None, None, None, None, None, None, None, None, False, None, True, False, (2, 0)],

                    ["Apollonian Swordmaster", "combat", "2500/700", 11, 2500, None, 700, None, None, None, None, None, None, False, None, False, False, (2, 0)],
                    ["Apollonian Swordmaster", "combat", "1000/2200",4, 1000, None, 2200, None, None, None, None, None, None, False, None, False, False, (2, 0)],
                    ["Apollonian Swordmaster", "combat", "800/2400", 4 , 800, None, 2400, None, None, None, None, None, None, False, None, False, False, (2, 0)],
                    ["Apollonian Swordmaster", "combat", "600/2600", 3 , 600, None, 2600, None, None, None, None, None, None, False, None, False, False, (2, 0)],


                    ["Apollonian Tank", "action", "FlashBang", "Playable as an attack.  Range 3.  Hits all adjacent target, Move (-2) and Draw (-1).", 3, None, None, None, None, None, None, None, None, None, False, None, True, False, (3, 0)],
                    ["Apollonian Tank", "special", "Napalm Jets", "Playable as an attack or instead of defending.  Fire 2 jets of napalm 3 squares long.  Enemies in the fire take 200 damage per phase.  Lasts 2 turns", 3, 2000, None, 700, None, 200, None, None, None, None, False, None, False, False, (3, 0)],
                    ["Apollonian Tank", "action", "Rocket Tackle", "Playable on your turn, counts as an action.  Choose a line 3 squares from the tank and move to the end.  Any enemies in the line take 300 damage and defend a 1500 Attack.", 3, 1500, None, None, None, 300, None, None, None, None, False, None, True, False, (3, 0)],
                    ["Apollonian Tank", "action", "Remote Shielding","Playable as an attack.  Range 3.  Remove shields.  Ally Shields (+600)", 3, None, None, None, None, None, None, ("shields", 600), None, None, False, None, True, False, (3, 0)],

                    ["Apollonian Tank", "combat", "2000/1000", 4, 2000, None, 700, None, None, None, None, None, None, False, None, False, False, (3, 0)],
                    ["Apollonian Tank", "combat", "1800/1200", 4,1800, None, 1200, None, None, None, None, None, None, False, None, False, False, (3, 0)],
                    ["Apollonian Tank", "combat", "600/2400", 4 , 600, None, 2400, None, None, None, None, None, None, False, None, False, False, (3, 0)],
                    ["Apollonian Tank", "combat", "500/2500", 3 , 500, None, 2500, None, None, None, None, None, None, False, None, False, False, (3, 0)],
                    ["Apollonian Tank", "combat", "300/2700", 3 , 300, None, 2700, None, None, None, None, None, None, False, None, False, False, (3, 0)],
                    ["Apollonian Tank", "combat", "0/3000",   2   , 0, None, 3000, None, None, None, None, None, None, False, None, False, False, (3, 0)],

                    ["Aquilan Dipped Sword Dancer", "action", "Finesse of the Flying Sword", "During the next turn, for every phase of combat in which you are involved the enemy takes 300 damage", 3, None, None, None, None, 300, None, None, None, None, False, None, True, False, (25, 0)],
                    ["Aquilan Dipped Sword Dancer", "action", "Jack Hammer Wing Thrust", "Playable before moving.  Movement this turn = 0.  Attack phases this turn = 4.", 3, None, None, None, None, None, None, None, None, None, False, None, True, False, (25, 0)],
                    ["Aquilan Dipped Sword Dancer", "action", "Final Fury", "Playable with an attack.  Forfeit your next attack phase.  Attack +2400.  Defensive -800 for a turn.", 2, 2400, None, -800, None, None, None, None, None, None, False, None, True, False, (1, 0)],
                    ["Aquilan Dipped Sword Dancer", "special", "Sword Dance", "Playable on offense with 2 or more unused Movement, or on defense with a combat card.  Next turn attack +1000.", 4, 1000, None, None, None, None, None, None, None, None, False, None, True, False, (25, 0)],

                    ["Aquilan Dipped Sword Dancer", "combat", "2500/200", 5, 2500, None, 200, None, None, None, None, None, None, False, None, False, False, (1, 0 )],
                    ["Aquilan Dipped Sword Dancer", "combat", "2400/300", 8, 2400, None, 300, None, None, None, None, None, None, False, None, False, False, (1, 0 )],
                    ["Aquilan Dipped Sword Dancer", "combat", "500/2200", 4, 500, None, 2200, None, None, None, None, None, None, False, None, False, False, (1, 0 )],
                    ["Aquilan Dipped Sword Dancer", "combat", "300/2400", 3, 300, None, 2400, None, None, None, None, None, None, False, None, False, False, (1, 0 )],
                 

                    ["Aquilan Energy Technician", "special", "Transformative Multiplication", "Playable on your turn or while defending.  Trap with 2 activations.  Sacrifice an attack card.  On activation increase shields by 1/3 the attack value of the card sacrificed", 3, 2000, None, 700, None, None, None, ("shields",1/3), None, None, True, 2, True, False, (3, 0)],
                    ["Aquilan Energy Technician", "action", "Launch", "Playable on your turn if it can be used to move into attack range.  Move 5 with Fly of 3", 3, None, None, None, None, None, None, None, None, None, False, None, True, False, (5, 0)],
                    ["Aquilan Energy Technician", "action", "Bountiful Rest", "Playable when not moving or attacking this turn.  Draw +2.  Move +2", 3, None, None, None, None, None, None, None, None, None, False, None, True, False, (25, 0)],
                    ["Aquilan Energy Technician", "special", "Conspicuous Stealth Trap", "Playable on offense, but only before moving.  Playable on defense in range 2 of the attacker.  Enemy draw (-2), range(-2).", 3, None, None, None, None, None, None, None, None, None, False, None, True, False, (2, 0)],

                    ["Aquilan Energy Technician", "combat", "2000/200", 2, 2000, None, 200 , None, None, None, None, None, None, False, None, False, False, (1, 0)],
                    ["Aquilan Energy Technician", "combat", "1800/400", 5, 1800, None, 400 , None, None, None, None, None, None, False, None, False, False, (1, 0)],
                    ["Aquilan Energy Technician", "combat", "200/2000", 6, 200 , None, 2000, None, None, None, None, None, None, False, None, False, False, (1, 0)],
                    ["Aquilan Energy Technician", "combat", "100/2100", 4, 100 , None, 2100, None, None, None, None, None, None, False, None, False, False, (1, 0)],
                    ["Aquilan Energy Technician", "combat", "0/2200", 3  , 0   , None, 2200, None, None, None, None, None, None, False, None, False, False, (1, 0)],


                    ["Aquilan Tempest", "action", "Bone-Chilling Gusts", "Playable with an attack.  All targets effected by the attack, Move (-2)", 3, None, None, None, None, None, None, None, None, None, False, None, True, False, (3,2)],
                    ["Aquilan Tempest", "action", "Infernal Squall", "Playable with an attack.  Target takes 300/100 burn damage", 3, None, None, None, None, None, None, None, None, None, False, None, True, False, (3,2)],
                    ["Aquilan Tempest", "action", "Strategic Stormfronts", "Playable as a stand-alone attack.  Attack = 1500.  Move enemies that take no damage 1 square.  Move enemies that take damage 2 squares.  Move allies 2 squares", 3, 1500, None, None, None, None, None, None, None, None, False, None, True, True, (3, 2)],
                    ["Aquilan Tempest", "action", "Turbulent Advantage", "Playable on your turn by forfeiting your next attack.  Move 4 with Fly of 2.", 3, None, None, None, None, None, None, None, None, None, False, None, True, False, (3, 2)],

                    ["Aquilan Tempest", "combat", "1800/700", 4, 1800, None, 700 , None, None, None, None, None, None, False, None, False, False, (3,2)],
                    ["Aquilan Tempest", "combat", "1700/800", 4, 1700, None, 800 , None, None, None, None, None, None, False, None, False, False, (3,2)],
                    ["Aquilan Tempest", "combat", "1500/1000",5, 1500, None, 1000, None, None, None, None, None, None, False, None, False, False, (3,2)],
                    ["Aquilan Tempest", "combat", "200/2300", 4, 200 , None, 2300, None, None, None, None, None, None, False, None, False, False, (3,2)],
                    ["Aquilan Tempest", "combat", "0/2500", 3  , 0   , None, 2500, None, None, None, None, None, None, False, None, False, False, (3,2)],


                    ["Biologic Amplifier", "special", "Black-Listed Vitals", "Playable anytime as a trap with 2 activations.  Choose a target.  For 1 turn that target is uneffected by the amplification rods.", 3, None, None, None, None, None, None, None, None, None, True, 2, True, False, (25, 0)],
                    ["Biologic Amplifier", "action", "Serotonin Cerebral Expansion", "Playable as an attack.  Place a 1000 health amplifying rod adjacent to the Biologic Amplifier.  All targets in range 2 Draw (+1) and view opponents cards in combat.", 3, None, None, None, None, None, None, None, None, None, False, None, True, False, (1, 0)],
                    ["Biologic Amplifier", "action", "Disorienting Stimuli", "Playable as an attack.  Place a 1000 health amplifying rod adjacent to the Biologic Amplifier.  All targets in range 2 Move (-2) and Draw (-1).", 3, None, None, None, None, None, None, None, None, None, False, None, True, False, (1, 0)],
                    ["Biologic Amplifier", "action", "Fast-Twitch Stimulation", "Playable as an attack.  Place a 1000 health amplifying rod adjacent to the Biologic Amplifier.  All targets in range 2 Move (+2) Att/Def + 600.", 3, 600, None, 600, None, None, None, None, None, None, False, None, True, False, (1, 0)],

                    ["Biologic Amplifier", "combat", "600/2700", 3, 600 , None, 2700, None, None, None, None, None, None, False, None, False, False, (1, 0)],
                    ["Biologic Amplifier", "combat", "800/2500", 5, 800 , None, 2500, None, None, None, None, None, None, False, None, False, False, (1, 0)],
                    ["Biologic Amplifier", "combat", "2500/800", 5, 2500, None, 800 , None, None, None, None, None, None, False, None, False, False, (1, 0)],
                    ["Biologic Amplifier", "combat", "2700/600", 7, 2700, None, 600 , None, None, None, None, None, None, False, None, False, False, (1, 0)],


                    ["Gothmaug Marauder", "special", "Launch Ally", "Playable when adjacent to an ally.  Move the ally 3 x (ally Movement).", 3, None, None, None , None, None, None, None, None, None, False, None, True, False, (1, 0)],
                    ["Gothmaug Marauder", "special", "Read Mind", "Playable during combat after cards have been chosen.  The opponent reveals their cards and you can change your cards.", 2, None, None, None , None, None, None, None, None, None, False, None, True, False, (1,0)],
                    ["Gothmaug Marauder", "special", "Intercept", "Playable anytime an enemy is in Range 2 and moving.  Enemy Movement -2.", 3, None, None, None , None, None, None, None, None, None, False, None, True, False, (2, 0)],
                    ["Gothmaug Marauder", "action", "Mighty Leap", "Playable as an attack or defense.  Move (+6) with glide 2 + clamber.", 2, None, None, None, None, None, None, None, None, None, False, None, True, False, (1, 0)],
                    ["Gothmaug Marauder", "action", "Mighty Strike", "Playable as a stand-alone attack.  Forfeit your next attack phase.  Attack = 3600", 2, 3600, None, None, None, None, None, None, None, None, False, None, True, True, (1, 0)],

                    ["Gothmaug Marauder", "combat", "600/2700", 3, 600 , None, 2700, None, None, None, None, None, None, False, None, False, False, (1, 0)],
                    ["Gothmaug Marauder", "combat", "800/2500", 5, 800 , None, 2500, None, None, None, None, None, None, False, None, False, False, (1, 0)],
                    ["Gothmaug Marauder", "combat", "2500/800", 5, 2500, None, 800 , None, None, None, None, None, None, False, None, False, False, (1, 0)],
                    ["Gothmaug Marauder", "combat", "2700/600", 7, 2700, None, 600 , None, None, None, None, None, None, False, None, False, False, (1, 0)],


                    ["Iksnik Hivemind", "special", "Hivemind Replication", "Discard a card, then take a card of the same type from your graveyard.", 3, 2700, None, 600 , None, None, None, None, None, None, False, None, False, False, (1,0)],
                    ["Iksnik Hivemind", "special", "Unified Retreat", "Playable as an instant action defense.  Move 1 Iksnik 5 squares or move all Iksnik by 1.", 3, 2700, None, 600 , None, None, None, None, None, None, False, None, False, False, (1, 0)],
                    ["Iksnik Hivemind", "action", "Unified Preparation", "Playable as an attack.  The Iksnik can either Move (+3) and Draw (2) or they can Move (+2) with Att/Def +400 for a turn.", 3, 2700, None, 600 , None, None, None, None, None, None, False, None, False, False, (1, 0)],
                    ["Iksnik Hivemind", "action", "Unified Attack", "Playable with an attack.  The Iksnik can either attack together with their attack values summed or they can attack individual for 1 action.", 3, 2700, None, 600 , None, None, None, None, None, None, False, None, False, False, (1, 0)],

                    ["Iksnik Hivemind", "combat", "1400/800", 4,1400, None, 800 , None, None, None, None, None, None, False, None, False, False, (1, 0)],
                    ["Iksnik Hivemind", "combat", "1200/1000",4,1200, None, 1000, None, None, None, None, None, None, False, None, False, False, (1, 0)],
                    ["Iksnik Hivemind", "combat", "400/1800", 8, 400, None, 1800, None, None, None, None, None, None, False, None, False, False, (1, 0)],
                    ["Iksnik Hivemind", "combat", "100/2000", 4, 100, None, 2000, None, None, None, None, None, None, False, None, False, False, (1, 0)],



                    ["Leonid Carrier", "special", "Cross Species Catalysts","Playable as a trap with two activations.  1st activation on an enemy in attack range.  Enemy Att/Def +300.  2nd Activation on an ally in range.  Ally Att/Def +1200",3, 300, None, None , None, None, None, None, None, None, True, 2, True, False, (1, 0)],
                    ["Leonid Carrier", "action", "Deliver to Safety","Playable while adjacent to an ally on your turn.  Move (-2).  Move the ally with you wherevver you move this turn.",3, None, None, None, None, None, None, None, None, None, False, None, True, False, (1,0)],
                    ["Leonid Carrier", "action", "Deliver to Harm","Playable while adjacent to an enemy on your turn.  Move (-3).  Move the enemy with you wherever you move this turn.",3, None, None, None, None, None, None, None, None, None, False, None, True, False, (1,0)],
                    ["Leonid Carrier", "action", "Deliver Supplies","Playable while moving and adjacent to an ally.  Discard up to 3 cards.  The ally draws 1 more than you discard",3 , None, None, None, None, None, None, None, None, None, False, None, True, False, (1,0)],

                    ["Leonid Carrier", "combat", "2600/400", 8, 2600, None, 400 , None, None, None, None, None, None, False, None, False, False, (1, 0)],
                    ["Leonid Carrier", "combat", "600/2400", 4, 600 , None, 2400, None, None, None, None, None, None, False, None, False, False, (1, 0)],
                    ["Leonid Carrier", "combat", "500/2500", 4, 500 , None, 2500, None, None, None, None, None, None, False, None, False, False, (1, 0)],
                    ["Leonid Carrier", "combat", "300/2700", 2, 300 , None, 2700, None, None, None, None, None, None, False, None, False, False, (1, 0)],
                    ["Leonid Carrier", "combat", "0/3000", 2  , 0   , None, 3000, None, None, None, None, None, None, False, None, False, False, (1, 0)],


                    ["Leonid Commandant", "action", "Tearing Claw","Stand-Alone attack.  Attack value = 3000.  If damaged include 400/100 bleed damage.", 3, 3000, None, None , None, None, None, None, (400,-300), None, False, None, True, True, (2, 0)],
                    ["Leonid Commandant", "action", "Coordinated Logistics","Playable after drawing.  Allies draw (+2).  If no allies left alive, draw 3.", 3, None, None, None , None, None, None, None, None, None, False, None, True, False, (2, 0)],
                    ["Leonid Commandant", "action", "Tactical Assault","Playable after your last attack phase if another ally is an attack range of your targer.  Your ally can attack immediately if the Commandant forfeits an attack phase next turn.", 3, None, None, None , None, None, None, None, None, None, False, None, True, False, (2, 0)],
                    ["Leonid Commandant", "action", "Command","Playable after moving.  Move yourself and your allies by 2.  If no allies left alive, move 4.", 3, None, None, None , None, None, None, None, None, None, False, None, True, False, (2, 0)],

                    ["Leonid Commandant", "combat", "2700/700", 3, 2700, None, 700 , None, None, None, None, None, None, False, None, False, False, (2, 0)],
                    ["Leonid Commandant", "combat", "2500/900", 5, 2500, None, 900 , None, None, None, None, None, None, False, None, False, False, (2, 0)],
                    ["Leonid Commandant", "combat", "1200/2200",4, 1200, None, 2200, None, None, None, None, None, None, False, None, False, False, (2, 0)],
                    ["Leonid Commandant", "combat", "900/2500", 4, 900 , None, 2500, None, None, None, None, None, None, False, None, False, False, (2, 0)],
                    ["Leonid Commandant", "combat", "600/2800", 4, 600 , None, 2800, None, None, None, None, None, None, False, None, False, False, (2, 0)],

                   
                    ["Leonid Lieutenant", "action", "Swift Claw", "Stand-Alone attack.  Attack = 2200.  Does not use an attack phase.  Only 1 Swift Claw can be played per turn.", 3, 2200, None, None , None, None, None, None, None, None, False, None, True, False, (1, 0)],
                    ["Leonid Lieutenant", "action", "Super Swift Claw", "Stand-Alone attack.  Attack = 2500.  Does not use an attack phase.  Only 1 Super Swift Claw can be played per turn.", 3, 2500, None, None , None, None, None, None, None, None, False, None, True, False, (1, 0)],
                    ["Leonid Lieutenant", "action", "Ultra Swift Claw", "Stand-Alone attack.  Attack = 2800.  Does not use an attack phase.  Only 1 Ultra Swift Claw can be played per turn.", 3, 2800, None, None , None, None, None, None, None, None, False, None, True, False, (1, 0)],
                    ["Leonid Lieutenant", "action", "Power Claw", "Stand-Alone attack.  Attack = 3500", 3, 3500, None, None , None, None, None, None, None, None, False, None, False, True, (1, 0)],

                    ["Leonid Lieutenant", "combat", "2400/0", 12, 2400, None, 0   , None, None, None, None, None, None, False, None, True, False, (1, 0)],
                    ["Leonid Lieutenant", "combat", "0/2400", 8 , 0   , None, 2400, None, None, None, None, None, None, False, None, True, False, (1, 0)],



                    ["Mogwai Mass Mystic", "special", "Here Me", "Playable as a trap with two activations.  Only 1 activation can be used per turn.  Move 1 square.", 3, None, None, None , None, None, None, None, None, None, False, None, True, False, (1, 0)],
                    ["Mogwai Mass Mystic", "action", "Here Ye", "Playable as an attack.  Move the target 2 spaces.", 3, None, None, None , None, None, None, None, None, None, False, None, True, False, (1, 0)],
                    ["Mogwai Mass Mystic", "special", "You Shall Not", "Playable anytime an enemy is in range.  Enemy Movement -3.", 3, None, None, None , None, None, None, None, None, None, False, None, True, False, (1, 0)],
                    ["Mogwai Mass Mystic", "special", "I Shall", "Playable anytime.  Movement = 3 with a Hover of 3.", 3, None, None, None , None, None, None, None, None, None, False, None, True, False, (1, 0)],

                    ["Mogwai Mass Mystic", "combat", "2000/2000", 20, 2000, None, 2000 , None, None, None, None, None, None, False, None, False, False, (1, 0)],
                    
                    ["Molochite All-Mother", "special", "Deaths Acolyte", "Playable after any player's attack phase ends.  Roll a 6 sided. 1-2: The All-Mother heals 1/2 damage taken.  3-4: The All-Mother Heals 1200.  5-6: The All-Mother or her ally can heal half the damage taken or 1200.", 3, None, None, None , None, None, None, ("health", 1200), None, None, False, None, True, False, (5, 0)],
                    ["Molochite All-Mother", "action", "Despair", "Playable instead of attacking.  Choose a target.  The All-Mother and her target cannot attack until the target discards 3.", 2, None, None, None , None, None, None, None, None, None, False, None, True, False, (5, 0)],
                    ["Molochite All-Mother", "special", "Disarming Illusions", "Playable anytime another hero in range (ally or enemy).  Trade up to 3 attack cards with the hero", 3, None, None, None , None, None, None, None, None, None, False, None, True, False, (1, 0)],
                    ["Molochite All-Mother", "special", "Death's Faithful Servant", "Playable anytime a player doesn't attack on their turn.  That player takes 1000 damage", 4, None, None, None , None, 1000, None, None, None, None, False, None, True, False, (5, 0)],

                    ["Molochite All-Mother", "combat", "0/2400",   5,  0, None, 2400, None, None, None, None, None, None, False, None, False, False, (5, 0)],
                    ["Molochite All-Mother", "combat", "0/2200", 5, 2200, None, 200 , None, None, None, None, None, None, False, None, False, False, (5, 0)],
                    ["Molochite All-Mother", "combat", "0/2100", 5, 2200, None, 600 , None, None, None, None, None, None, False, None, False, False, (5, 0)],
                    ["Molochite All-Mother", "combat", "0/2000", 5, 1000, None, 1600, None, None, None, None, None, None, False, None, False, False, (5, 0)],


                    ["Molochite Weapons Technician", "action", "Overcharge Rifle", "Playable before moving.  Move (-2), Action Phases (-1).  Attack (+1500).", 3, 1500, None, None , None, None, None, None, None, None, False, None, True, False, (25, 0)],
                    ["Molochite Weapons Technician", "action", "Overcharge Jump Boots", "Playable before or after moving.  Move up to 3 spaces with 3 jump, but a max fall of 2.", 3, None, None, None , None, None, None, None, None, None, False, None, True, False, (25, 0)],
                    ["Molochite Weapons Technician", "special", "Redirect Shields", "Playable on your turn.  For 1 turn you have no shields.  For 1 turn Attack (+1000).", 3, 1000, None, None , None, None, None, ("shields", -500), None, None, False, None, True, False, (25, 0)],
                    ["Molochite Weapons Technician", "special", "Overcharge Bayonette", "Playable in range 1 of an enemy.  Stand-Alone, Attack = 3000", 3, 3000, None, None , None, None, None, None, None, None, False, None, True, True, (1, 0)],

                    ["Molochite Weapons Technician", "combat", "1800/600", 5, 1800, None, 600 , None, None, None, None, None, None, False, None, False, False, (7, 0)],
                    ["Molochite Weapons Technician", "combat", "1700/700", 5, 1700, None, 700 , None, None, None, None, None, None, False, None, False, False, (7, 0)],
                    ["Molochite Weapons Technician", "combat", "1600/800", 5, 1600, None, 800 , None, None, None, None, None, None, False, None, False, False, (7, 0)],
                    ["Molochite Weapons Technician", "combat", "800/1600", 5, 800 , None, 1600, None, None, None, None, None, None, False, None, False, False, (7, 0)],


                    ["Molochite Quarantine Runner", "action", "Hologram", "Playable before moving.  Creates three holograms.  Play this turn as though you are all four characters.  Any attack to the hologram will destroy it.", 3, None, None, None , None, None, None, None, None, None, False, None, True, False, (25, 0)],
                    ["Molochite Quarantine Runner", "action", "Holographic Ambush", "Playable when in range to attack from at least 2 different squares.  Roll a 6 sided di. 1-4: Attack (+1000). 5-6:Attack (+1000) and Move(+1)", 3, 1000, None, None , None, None, None, None, None, None, False, None, True, False, (4, 0)],
                    ["Molochite Quarantine Runner", "special","Violent Greed", "Playable on the last attack of your turn.  Gain an attack phase with (-600) Attack.", 3, -600, None, None , None, None, None, None, None, None, False, None, True, False, (4, 0)],
                    ["Molochite Quarantine Runner", "special","Greed", "Draw 3.", 3, None, None, None , None, None, None, None, None, None, False, None, True, False, (25, 0)],

                    ["Molochite Quarantine Runner", "combat", "2400/400", 2, 2400, None, 400 , None, None, None, None, None, None, False, None, False, False, (4, 0)],
                    ["Molochite Quarantine Runner", "combat", "2300/500", 5, 2300, None, 500 , None, None, None, None, None, None, False, None, False, False, (4, 0)],
                    ["Molochite Quarantine Runner", "combat", "2200/2600", 6, 2200, None, 600 , None, None, None, None, None, None, False, None, False, False,(4, 0)],
                    ["Molochite Quarantine Runner", "combat", "1000/1600", 4, 1000, None, 1600, None, None, None, None, None, None, False, None, False, False,(4, 0)],
                    ["Molochite Quarantine Runner", "combat", "800/1700", 3, 800 , None, 1700, None, None, None, None, None, None, False, None, False, False, (4, 0)],

                    ["Normanus World-Bearer", "special", "Starvation Rations","Playable after drawing.  No other players may draw this turn.", 2, None, None, None , None, None, None, None, None, None, False, None, True, False, (25, 0)],
                    ["Normanus World-Bearer", "special", "Northlands Bounty","Draw 2", 2, None, None, None , None, None, None, None, None, None, False, None, True, False, (25, 0)],
                    ["Normanus World-Bearer", "action", "Cleave","Playable as a stand-alone attack.  Attack = 2500.  Hits all targets in a 3x1.", 4, 2500, None, None , None, None, None, None, None, None, False, None, True, True, (1,3)],
                    ["Normanus World-Bearer", "action", "World Bearing Resiliency","Playable on your turn instead of attacking.  Discard up to 2 cards.  For 1 turn your shields equal 800 x the number of cards discarded", 4, None, None, None , None, None, None, ("shields", 800), None, None, False, None, True, False, (25, 0)],
                    #Half damage at range 1 due to them having war-axe/warhammer
                    ["Normanus World-Bearer", "combat", "1600/3200 /800", 20, 3200, None, 800, None, None, None, None, None, None, False, None, True, False, (2, 0)],



                    ["Saturni Reaper", "special", "Death Ritual","Playable as a trap card.  Activated when a target dies or takes 2500 damage in one turn.  Heal 1500.", 4, None, None, None , None, None, None, ("health", 1500), None, None, False, None, True, True, (25, 0)],
                    ["Saturni Reaper", "action", "Regenerative Fury","Playable with your first defense of the turn.  Heal 1/3 of the damage taken.  Increase attack by the amount healed for 1 turn.", 3, None, None, None , None, None, None, ("health", 1/3), None, None, False, None, True, False, (25, 0)],
                    ["Saturni Reaper", "action", "Reaping","Playable as a stand-alone attack.  Attack = 2000.  Hits all targets in a 3x2 and pulls them 1 square closer if possible.", 3, 2000, None, None , None, None, None, None, None, None, False, None, True, True, (2, 3)],
                    ["Saturni Reaper", "action", "Reap","Playable on your turn instead of attacking.  Draw 2", 2, None, None, None , None, None, None, None, None, None, False, None, True, False, (25, 0)],

                    ["Saturni Reaper", "combat", "2400/1600", 20, 2400, None, 1600 , None, None, None, None, None, None, False, None, True, False, (25, 0)], 


                    ["Selene Femmentalist", "special", "Secrets Revealed","Playable when an attack is declared.  You and your target reveal your hands.  You then discard your hand and draw 4", 2, None, None, None , None, None, None, None, None, None, False, None, True, False, (25, 0)],
                    ["Selene Femmentalist", "special", "Blinding Agility","Playable while moving.  Move (+3), Jump = 2 + clamber.", 2, None, None, None , None, None, None, None, None, None, False, None, True, False, (25, 0)],
                    ["Selene Femmentalist", "action", "Instinct Fatale", "Playable anytime on your turn or while defending.  Discard 2 and choose a target.  That target's Defense (-1000), on your next turn.", 2, None, None, None , None, None, None, None, None, None, False, None, True, False, (1, 0)],
                    ["Selene Femmentalist", "action", "Feminine Fury","Playable with an attack, Attack (+800).  If you do damage draw 1 and the target must play combat cards face-up during the next phase of combat.", 3, 800, None, None , None, None, None, None, None, None, False, None, True, False, (1, 0)],
                    ["Selene Femmentalist", "action", "Battledance of Fate","Playable with an attack as a trap with two activations if you do damage draw (+2), scry (+3), and discard 1 of the scried cards if you wish.", 3, None, None, None , None, None, None, None, None, None, True, 2, True, False, (25, 0)],

                    ["Selene Femmentalist", "combat", "2500/300", 4, 2500, None, 300 , None, None, None, None, None, None, False, None, False, False, (1, 0)],
                    ["Selene Femmentalist", "combat", "2300/500", 6, 2300, None, 500 , None, None, None, None, None, None, False, None, False, False, (1, 0)],
                    ["Selene Femmentalist", "combat", "400/2400", 6, 400 , None, 2400, None, None, None, None, None, None, False, None, False, False, (1, 0)],
                    ["Selene Femmentalist", "combat", "200/2600", 4, 200 , None, 2600, None, None, None, None, None, None, False, None, False, False, (1, 0)],


                    ["Selene Master Weavemaker", "action", "Serene Calm","Playable at the end of your turn after no combat with 2 movement left.  Heal 1500.", 3, None, None, None , None, None, None, ("health", 1500), None, None, False, None, True, False, (1, 0)],
                    ["Selene Master Weavemaker", "action", "Shield Toss", "Playable as a stand alone.  Range 5.  Attack = 3000 - (200 * range) For 1 turn Defense (-1000) unless you move adjacent to the attack square.", 3, 3000, None, -1000, None, None, None, None, None, None, False, None, True, True, (5, 0)],
                    ["Selene Master Weavemaker", "special", "Divine Grace", "Playable anytime.  Move 2.  Has a second activation that only works during the movement phase.", 2, None, None, None , None, None, None, None, None, None, True, 2, True, False, (25, 0)],
                    ["Selene Master Weavemaker", "action", "Battlestudy", "Playable at the end of your turn.  Defense (+500) * # of defenses this turn.", 2, None, 500, None , None, None, None, None, None, None, False, None, True, False, (25, 0)],
                    ["Selene Master Weavemaker", "action", "Afterburning Shields", "Playable with a defense.  Shields +1500 per enemy attack phase (even if they don't attack).  All enemies who attack take 500 damage.", 2, None, None, None , None, 500, None, ("shields", 1500), None, None, False, None, True, False, (25, 0)],

                    ["Selene Master Weavemaker", "combat", "2500/500", 2, 2500, None,2500, None, None, None, None, None, None, False, None, False, False, (1, 0)],
                    ["Selene Master Weavemaker", "combat", "2400/600", 3, 2400, None,2400, None, None, None, None, None, None, False, None, False, False, (1, 0)],
                    ["Selene Master Weavemaker", "combat", "2200/800", 3, 800 , None,2200, None, None, None, None, None, None, False, None, False, False, (1, 0)],
                    ["Selene Master Weavemaker", "combat", "500/2500", 4, 500, None, 2500, None, None, None, None, None, None, False, None, False, False, (1, 0)],
                    ["Selene Master Weavemaker", "combat", "400/2600", 4, 400, None, 2600, None, None, None, None, None, None, False, None, False, False, (1, 0)],
                    ["Selene Master Weavemaker", "combat", "200/2800", 4, 200, None, 2800, None, None, None, None, None, None, False, None, False, False, (1, 0)],


                    ["Selene Perfectionist", "action", "Precise Strike", "Playable with an attack.  With this card you choose your attack value after the attack.  Any value Attack (+-500).  2 activations", 3, None, None, None , None, None, None, None, None, None, True, 2, True, False, (1, 0)],
                    ["Selene Perfectionist", "special", "Intuited Perfection", "Playable after any combat with the Selene Perfectionist where the attack and defense values are equal.  Target takes 700 damage.  2 activations", 3, None, None, None , None, 700, None, None, None, None, True, 2, True, False, (25, 0)],
                    ["Selene Perfectionist", "action", "Replacement", "Playable instead of attacking.  Look at the top 5 cards in your deck and graveyard.  Replace up to 3 cards of the same type from your hand.", 2, None, None, None , None, None, None, None, None, None, False, None, True, False, (25, 0)],
                    ["Selene Perfectionist", "action", "Perfection", "All damage is blocked.", 2, None, None, 100000, None, None, None, None, None, None, False, None, True, False, (1, 0)],
                    ["Selene Perfectionist", "action", "Divination", "Playable instead of attacking.  Look at the top 4 cards in your deck.  Put 1 in your hand and order the other 3 at the top of your deck.", 2, None, None, None , None, None, None, True, None, None, False, None, True, False, (25, 0)],

                    ["Selene Perfectionist", "combat", "2400/400", 7, 2400, None, 400, None, None, None, None, None, None, False, None, False, False, (1, 0)],
                    ["Selene Perfectionist", "combat", "1000/2000",1, 1000, None, 200, None, None, None, None, None, None, False, None, False, False, (1, 0)],
                    ["Selene Perfectionist", "combat", "900/2100", 2, 900 , None, 2100, None, None, None, None, None, None, False, None, False, False, (1, 0)],
                    ["Selene Perfectionist", "combat", "800/2200", 2, 800 , None, 2200, None, None, None, None, None, None, False, None, False, False, (1, 0)],
                    ["Selene Perfectionist", "combat", "700/2300", 2, 700 , None, 2300, None, None, None, None, None, None, False, None, False, False, (1, 0)],
                    ["Selene Perfectionist", "combat", "600/2400", 2, 600 , None, 2400, None, None, None, None, None, None, False, None, False, False, (1, 0)],
                    ["Selene Perfectionist", "combat", "500/2600", 2, 500 , None, 2500, None, None, None, None, None, None, False, None, False, False, (1, 0)],
                    ["Selene Perfectionist", "combat", "400/2600", 2, 400 , None, 2600, None, None, None, None, None, None, False, None, False, False, (1, 0)],


                    ["The Phase Walker", "action", "Triple Point", "Playable anytime as a trap card with 2 activations.  You may use any value on a combat card (regardless of form).", 4, None, None, None , None, None, None, None, None, None, True, 2, True, False, (5, 0)],
                    ["The Phase Walker", "action", "Phase Mastery", "In Gas form Attack +1000.  In liquid form Movement +3.  In Solid form Defense +1500.", 4, 1000, None, 1500 , None, None, None, None, None, None, False, None, True, False, (5, 0)],
                    ["The Phase Walker", "special", "Transform", "Playable anytime as an instant action trap with 2 activations.  Discard 1 card.  Change form.", 4, None, None, None , None, None, None, None, None, None, True, 2, True, False, (5, 0)],

                    ["The Phase Walker", "combat", "3000/0 1500/1500 0/3000", 20, 3000, None, 3000, None, None, None, None, None, None, False, None, True, False, (5, 0)],


                    ["The Spore", "special", "Replicate", "Playable as an attack or with a defense.  Place a spore miniature in attack range.  Decrease Health of the spore throwing it by 1000.", 6, None, None, None , None, None, None, None, None, None, True, 2, True, False, (25, 0)],
                    ["The Spore", "special", "Unify", "Playable on your turn.  Unify spores in range healing the remaining one for 1000 for each spore unified", 3, None, None, None , None, None, None, 1000, None, None, None, None, True, False, (3, 0)],
                    ["The Spore", "special", "Simplify", "Playable in combat, spores not in combat cannot move or attack next turn.  If defending multiply defense value by number of spores on the field.  If attacking, use the attack value 1200 and multiply by the spores on the field", 3, 600, None, 1200 , None, None, None, None, None, None, None, None, True, False, (25, 0)],

                    ["The Spore", "combat", "600/1200", 20, 600, None, 1200, None, None, None, None, None, None, False, None, True, False, (3, 0)],   


                    ["Urik La", "action", "Blood Sacrifice", "Playable after drawing.  If above 3500 Health transfer up 2500 health to an ally.  Otherwise, or if allies are dead, Heal 2500.", 3, None, None, None , None, None, None, -2500, None, None, False, None, True, False, (25, 0)],
                    ["Urik La", "action", "Mirrored Regeneration", "Playable with a defense.  If you survive the attack heal yourself or an ally for half the attack value", 3, None, None, None , None, None, None, ("health", 1/2), None, None, False, None, True, False, (3, 0)],
                    ["Urik La", "special", "Congeal", "Playable anytime.  Choose a target.  The target heals half the damage they take over the next turn.", 2, None, None, None , None, None, None, ("health", 1/2), None, None, False, None, True, False, (3, 0)],
                    ["Urik La", "action", "Red Prophecy", "Playable after drawing.  Attack (+800).  If the Urik La deals 500 damage she scries 3 from the opponents deck.  If not the opponent scries 1 from her deck.", 2, 800, None, None , None, None, None, None, None, None, False, None, True, False, (3, 0)],
                    ["Urik La", "action", "Black Prophecy", "Playable on another characters turn.  The target leaves the cards they drew facedown for this turn.  They can try to play these cards, but if they misplay they forfeit an action.", 2, None, None, None , None, None, None, None, None, None, None, None, True, False, (3, 0)],

                    ["Urik La", "combat", "2200/500", 4, 2200, None, 500 , None, None, None, None, None, None, False, None, False, False, (3, 0)],
                    ["Urik La", "combat", "2000/700", 6, 2000, None, 700 , None, None, None, None, None, None, False, None, False, False, (3, 0)],
                    ["Urik La", "combat", "800/1900", 6, 800 , None, 1900, None, None, None, None, None, None, False, None, False, False, (3, 0)],
                    ["Urik La", "combat", "600/2100", 4, 600 , None, 2100, None, None, None, None, None, None, False, None, False, False, (3, 0)],


                    ["Urik Mimic", "special", "Reverberate", "Playable after combat.  Take the enemy's combat card used during combat and put them in your hand.  Attack/Def +400", 5, 400, None, 400, None, None, None, None, None, None, False, None, True, False, (1, 0)],
                    ["Urik Mimic", "special", "Imitate", "Plays as a trap with 2 activations.  Playable after an enemy uses an action or special card in range 5.  Put the enemy's card in your hand.", 3, None, None, None, None, None, None, None, None, None, True, 2, True, False, (5, 0)],
                    ["Urik Mimic", "action", "Blood Memories", "Discard 2.  Draw 2.", 3, None, None, None, None, None, None, None, None, None, False, None, True, False, (25, 0)],
 
                    ["Urik Mimic", "combat", "500/2500", 15, 500, None, 2500, None, None, None, None, None, None, False, None, False, False, (1, 0)],
                    ["Urik Mimic", "combat", "2000/1000", 5, 2000, None, 1000, None, None, None, None, None, None, False, None, False, False, (1, 0)],


                    ["Urik Ra", "special", "Transform", "Playable while wielding embodied equipment.  Change what embodied equipment it is.  Lasts 1 turn.", 2, None, None, None, None, None, None, None, None, None, False, None, True, False, (25, 0)],
                    ["Urik Ra", "special", "Embodied Bloodwood Spear", "Playable anytime.  Attack (+800), Defense (+1200), lasts 1 turn.", 2, 1200, None, 800, None, None, None, None, None, None, False, None, True, False, (25, 0)],
                    ["Urik Ra", "action", "Embodied Longsword", "Playable anytime.  Attack (+1500), Defense (+800), lasts 1 turn.", 2, 1500, None, 800, None, None, None, None, None, None, False, None, True, False, (25, 0)],
                    ["Urik Ra", "action", "Embodied Chained Flail", "Playable anytime.  Attack (+2000), lasts 1 turn.", 2, 2000, None, None, None, None, None, None, None, None, False, None, True, False, (25, 0)],
                    ["Urik Ra", "action", "Embodied Technique", "Playable with an attack or defense while wielding embodied weapons/armor.  Longsword: Attack (+1000).  Great-Shield: Defense (+1000).  Chained Flail: No Action Used.  Bloodwood Spear: Attack (+1000), range 7, spear is gone after.", 2, 1000, None, 1000, None, None, None, None, None, None, False, None, True, False, (25, 0)],
                    ["Urik Ra", "action", "Embodied Great Shield", "Playable anytime.  Defense (+2000), lasts 1 turn.", 2, None, None, 2000, None, None, None, None, None, None, False, None, True, False, (25, 0)],

                    ["Urik Ra", "combat", "1500/1500", 12, 1500, None, 1500, None, None, None, None, None, None, False, None, False, False, (1, 0)],
                    ["Urik Ra", "combat", "300/2700" , 5 , 300 , None, 2700, None, None, None, None, None, None, False, None, False, False, (1, 0)],  
                    ["Urik Ra", "combat", "0/3000"   , 3 , 0   , None, 1300, None, None, None, None, None, None, False, None, False, False, (1, 0)], 


                    ["Verouk Shadow", "special", "Silence", "Playable in combat after the enemy chooses cards.  The enemies cards go to the graveyard, yours return to your hand.", 4, None, None, None, None, None, None, None, None, None, False, None, True, False, (25, 0)],
                    ["Verouk Shadow", "action", "Shadow Strike", "Playable as a Stand-Alone attack.  Contains two attacks Double Attack (1500), and Attack (500).  They are blocked separately", 4, 500, 1500, None, None, None, None, None, None, None, False, None, True, True, (1, 0)],
                    ["Verouk Shadow", "action", "Super Shadow Strike", "Playable as an attack with no attack phase.  Double Attack = (2000)", 4, None, 2000, None, None, None, None, None, None, None, False, None, True, False, (1, 0)],

                    ["Verouk Shadow", "combat", "1500/1500", 2, 2800, None, 800 , None, None, None, None, None, None, False, None, False, False, (1, 0)],
                    ["Verouk Shadow", "combat", "300/2700" , 9 , 2500, None, 110, None, None, None, None, None, None, False, None, False, False, (1, 0)],  
                    ["Verouk Shadow", "combat", "0/3000"   , 5 , 1400, None, 2200, None, None, None, None, None, None, False, None, False, False, (1, 0)], 
                    ["Verouk Shadow", "combat", "0/3000"   , 4 , 1100, None, 2500, None, None, None, None, None, None, False, None, False, False, (1, 0)], 



                    ["Volucris Bullet Beak", "special", "Tempest", "Playable anytime as an instant action.  Forfeit your draw phase next turn.  Move 2 with jump 3.", 3, None, None, None, None, None, None, None, None, None, False, None, True, False, (25, 0)],
                    ["Volucris Bullet Beak", "special", "Plant Talons", "Playable while defending or instead of attacking.  Effects last until you move.  Gain two attack phases, Defense (+1000).", 3, None, None, 1000, None, None, None, None, None, None, False, None, True, False, (25, 0)],
                    ["Volucris Bullet Beak", "action", "Ascend", "Playable before moving.  Move to height 6 within range 2.  You may attack this turn or the next.  When you return to the ground you may attack an enemy in range 3 with this card as a standalone of attack value 4500.", 2, 4500, None, None, None, None, None, None, None, None, False, None, True, True, (25, 0)],
                    ["Volucris Bullet Beak", "special", "Death Grip", "Playable when adjacent to an enemy.  Until your turn move with this enemy.  Target takes 200 damage each attack phase.", 2, None, None, None, None, 200, None, None, None, None, False, None, True, False, (1, 0)],
                    ["Volucris Bullet Beak", "special", "Ride Ally", "Playable when adjacent to an ally.  Until your turn, move with your ally.", 2, None, None, None, None, None, None, None, None, None, False, None, True, False, (1, 0)],

                    ["Volucris Bullet Beak", "combat", "2800/0", 2   , 2800, None, 0   , None, None, None, None, None, None, False, None, False, False, (1, 0)],
                    ["Volucris Bullet Beak", "combat", "2600/200", 4 , 2600, None, 200 , None, None, None, None, None, None, False, None, False, False, (1, 0)],  
                    ["Volucris Bullet Beak", "combat", "2500/300", 5 , 2500, None, 300 , None, None, None, None, None, None, False, None, False, False, (1, 0)],
                    ["Volucris Bullet Beak", "combat", "1000/1800", 3, 1000, None, 1800, None, None, None, None, None, None, False, None, False, False, (1, 0)],
                    ["Volucris Bullet Beak", "combat", "800/2000", 3 , 800 , None, 2000, None, None, None, None, None, None, False, None, False, False, (1, 0)],  
                    ["Volucris Bullet Beak", "combat", "600/2200", 3 , 600 , None, 2200, None, None, None, None, None, None, False, None, False, False, (1, 0)] ,              


                    ["Volucris Dart Thrower", "action", "Swift Retreat", "Playable with a combat card.  After the attack move (+3).  If perched this plays as an instant action with Move (+5)", 3, None, None, None, None, None, None, None, None, None, False, None, True, False, (3, 0)],
                    ["Volucris Dart Thrower", "action", "Swift Attack", "Playable with an attack.  Attack + (100 x distance traveled).  If perched, Attack + (200 x distance traveled -500)", 3, 100, None, None, None, None, None, None, None, None, False, None, True, False, (3, 0)],
                    ["Volucris Dart Thrower", "action", "Counter", "Playable with a combat card on defense.  Attackers attack (-500), Attacker Health (-500).", 3, 500, None, None, None, 500, None, None, None, None, False, None, True, False, (1, 0)],
                    ["Volucris Dart Thrower", "special", "Perch", "Playable instead of moving.  Perch on any raised surface in range 3.  Draw 1.  To unperch use an action card.  Move with Move (+2).  If you remain perched next turn Draw (+2).", 3, None, None, None, None, None, None, None, None, None, False, None, True, False, (3, 0)],

                    ["Volucris Dart Thrower", "combat", "2500/0", 2  , 2500, None, 0   , None, None, None, None, None, None, False, None, False, False, (3, 0)],
                    ["Volucris Dart Thrower", "combat", "2300/200", 9, 2300, None, 200 , None, None, None, None, None, None, False, None, False, False, (3, 0)],
                    ["Volucris Dart Thrower", "combat", "500/2000", 9, 500 , None, 2000, None, None, None, None, None, None, False, None, False, False, (3, 0)],
            
    
                    ["Volucris Salter", "special", "Salted Body", "Playable anytime on yourself or when adjacent to a target.  For self,heal 1200 for allies heal 700", 3, None, None, None, None, None, None, ("health", 1200), None, None, False, None, True, False, (1, 0)],
                    ["Volucris Salter", "special", "Salted Water", "Playable anytime.  Choose a square in range.  All enemies in range 2 of that square take 400 damage, allies heal 800.", 3, None, None, None, None, 400, None, ("health", 800), None, None, False, None, True, False, (25, 0)],
                    ["Volucris Salter", "action", "Salted Air", "Playable after drawing.  Choose a square in range.  Enemies in range 2 Draw (-1) and Move (-1).  Allies in range Draw (+1) Move + (1).", 3, None, None, None, None, None, None, None, None, None, False, None, True, False, (25, 0)],
                    ["Volucris Salter", "action", "Salted Earth", "Playable before moving.  Choose a square in range.  Enemies in range 2 of that square -400 Att/Def, -200 Health.  For allies +800 Att/Def , +500 Health", 3, 400, None, 400, None, 200, None, ("health", 500), None, None, False, None, True, False, (3, 0)] ,

                    ["Volucris Salter", "combat", "0/1800", 10, 1800, None, 0   , None, None, None, None, None, None, False, None, False, False, (1, 0)],
                    ["Volucris Salter", "combat", "1800/0", 10, 0   , None, 1800, None, None, None, None, None, None, False, None, False, False, (1, 0)],
                    ]                     




