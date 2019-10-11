#43 Doom Projekt
from sys import exit
from random import randint
from textwrap import dedent

class scene(object):
    def enter(self):
        exit(1)

#delcares engine class, which is an object
class engine(object):
    #magic method to initiate object
    def __init__(self, scene_map):
        self.scene_map = scene_map  #sets the self.scene_map attribute to the scene_map value

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('Ending')

        #Dunder methods allow for attribute comparison, as opposed to object
        while current_scene.__class__.__name__ != last_scene.__class__.__name__:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
            #print(current_scene.__class__.__name__, last_scene.__class__.__name__)

            # current_scene.enter()
            #This causes the scenes to repeat at least once

        last_scene.enter()

class Death(scene):
    def enter(self):
        print("***You died. Hell's legions cannot be stopped***.")
        exit(1)

class Ending(scene):
    def enter(self):
        print("***Congratulations! You have closed the portal, and assumed the eternal mantle of Doomslayer!***")
        exit(1)

class Mars(scene):
    def enter(self):
        print("*"*50)
        print(dedent("""
            The wasteland of Mars greets you with swirling sands, oppressive sun, and a rapidly increasing radiation counter on your suit. A massive set of power cables snakes toward cooling towers to the north, and as you follow them, you are beset on all sides by hundreds of demons. But you are the Doom Marine! You know no fear.

            Charge!
            Fire!
            Frag out!
            How will you slay?
            """))

        action = input("> ")
        action = action.lower()

        if action == "charge":
            print(dedent("""
                Though the might of your strong right arm is fearsome, you are slowly but surely borne down by the weight of numbers. You have died.
                """))
            return 'Death'

        elif action == "fire":
            print(dedent("""
                No lone enemy is a match for the might of the Doomslayer and his weapons, but there are far too many for just bullets. Good thing you also have GRENADES! FISTS! AND A DAGGONE CHAINSAW! WAAAAAAAAAAUUUUUUUGGGGGHHHHHHH!!!!!

                The crump of detonations marks your path as you carve a bloody swathe through the ranks of Hell. The Power Plant stands before you.
                """))
            return 'Power_Plant'

        elif action == "frag out":
            print(dedent("""
                You recall the words of your first company commander: 'My philosophy is simple: GRENADES! Followed by POINT BLANK RIFLE FIRE!'

                The crump of detonations marks your path as you carve a bloody swathe through the ranks of Hell. The Power Plant stands before you.
                """))
            return 'Power_Plant'

        else:
            print("That's not something a Marine would do!")
            return 'Mars'

class Power_Plant(scene):
    def enter(self):
        print("*"*50)
        print(dedent("""
            The ceiling of the power plant is high enough to be shrouded in shadow. Venting coolant creates a knee-deep fog and condensation on every surface, but that won't mask the splash of what can only be blood. Suddenly, a massive figure emerges!

            Before you stands your old foe, the Cyberdemon! A twisted rending of machine and sorcerous flesh animated by piping hot hatred for all life points his energy cannon straight toward you.

            Charge!
            Fire!
            Frag out!
            How will you slay?
            """))

        action = input("> ")
        action = action.lower()

        if action == "charge":
            print(dedent("""
                The demon knows your fighting style, as you tried that technique on him last time. His riposte is brilliant, and you are bathed in hellish light as you fall, armor blistered away by his cannon.
                """))
            return 'Death'

        elif action == "fire":
            print(dedent("""
                Maintaining fire discipline, you duck, dodge, and weave through his blasts. Finding what cover you can, rolling, turning, and diving, you snap shots to his face with mythic precision. With ammo running out, you deliver one more stunning blast from your shotgun before he falters...then falls.
                """))
            return 'Gate'

        elif action == "frag out":
            print(dedent("""
                With all guns blazing, you duck, dodge, and weave through his blasts. Leading with frags and snapping shots to his face with mythic precision, the demon is staggered by your assault. With ammo running out, you deliver one more stunning blast from your shotgun before he falters...then falls. Your chainsaw delivers the coup d'etat, severing his head as a grisly trophy.
                """))
            return 'Gate'

        else:
            print("That's not something a Marine would do!")
            return 'Power_Plant'

class Gate(scene):
    def enter(self):
        print("*"*50)
        print(dedent("""
            You stand before the open Hellgate on Mars: a massive skull, covered in unintelligible carvings, runes which scramble your HUD and reinforce your determination to finish this, once and for all. A steady stream of demons warps in through the writhing portal at the forehead, guarded by a massive, nightmarish Cerberus, which stalks among the swollen horde and cruelly marshalls them forward.

            Face them! Annihilate the guardian and descend into Hell!

            Charge!
            Fire!
            Frag out!
            How will you slay?
            """))

        action = input("> ")
        action = action.lower()

        if action == 'charge':
            print(dedent("""
                The sight of the portal itself ignites a berserk fury in you. Stowing weapons, you charge into the fray with matchless speed and brutality. Too busy defending itself to do more than scream at the demons, the Cerberus wilts under your furious assault. The remaining demon horde is easily dismantled by the pounding of your fists.
                """))
            return 'Hell'

        elif action == 'fire':
            print(dedent("""
                There are far too many enemies and no cover to permit focus on the leader. Attempting to destroy the demons first allows the guardian to outflank you, and you are shredded by its jaws.
                """))
            return 'Death'

        elif action == 'frag out':
            print(dedent("""
            You find the BFG! AAAAAAAAAAAAAAAND YOU USE IT!!!!!

            A torrent of raw energy leaps from body to body, shattering the milling legion into pulped fragments. The only creature still intact is the Cerberus, stunned and staggering backward, its three heads harmonizing a sanity-eroding wail. You distribute indiscriminate grenades, shotgun blasts, and elbows to the teeth of the monster, and though it may have put up quite a fight before it was stunned, its resistance is futile. You stand over the fallen demon, and enter the mystic portal.
            """))
            return 'Hell'

        else:
            print("That's not something a Marine would do!")
            return 'Gate'


class Hell(scene):
    def enter(self):
        print("*"*50)
        print(dedent("""
            Abandon all hope, ye who enter here! There are no words to describe the churning miasma of broken stones, burning sky, and screaming, tortured dead. Up and down barely make sense in the pulsing, scourged environ. You are barely able to make sense of what your senses provide when, from what must be a great height, descends the Spider Mastermind!

            Charge!
            Fire!
            Frag out!
            How will you slay?
            """))

        action = input("> ")
        action = action.lower()

        if action == 'charge':
            print(dedent("""
                Oh god....oh god YOU'RE everywhere! The spider mastermind screams something unintelligible and from nowhere, two Hell Barons emerge. One catches you mid leap and flings you into the air, as the other blasts you with a ball of green fire, thy flesh consumed.
                """))
            return 'Death'

        elif action == 'fire':
            print(dedent("""
            What, are you just gonna run around and shoot this thing? Noh. GTFO.
            """))
            return 'Death'

        elif action == 'frag out':
            print(dedent("""
                After a throwing everything you have at this monster, a momentary misstep allows you to ram the BFG into the spider mastermind's maw and pull the trigger. The detonation completely shears off the top half of its skull, and, shrieking and thrashing, it falls to the floor. Blood and demons erupt from the walls and ceiling, and as you endlessly annihilate, the portal closes, trapping them in Hell with you.
                """))
            return 'Ending'

        else:
            print("That's not something a Marine would do!")
            return 'Hell'

class Map(object):

    scene = {
        'Mars': Mars(),
        'Power_Plant': Power_Plant(),
        'Gate': Gate(),
        'Hell': Hell(),
        'Death': Death(),
        'Ending': Ending()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def opening_scene(self):
        return self.next_scene(self.start_scene)

    def next_scene(self, scene_name):
        return Map.scene.get(scene_name)

    # def last_scene(self, scene_name):
    #     return Map.scene.get('Ending')
    # This doesn't seem to do anything

a_map = Map('Mars') #starts the player at the designated Map
a_game = engine(a_map)
a_game.play()
