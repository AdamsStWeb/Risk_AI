from types import BuiltinMethodType
from pygame.constants import BUTTON_LEFT
from Input3 import ReadFile
import random

white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
blue=(0,0,255)
green=(0,255,0)
grey=(100,100,100)
yellow=(255,255,0)
purple = (240,0,255)
colors = [red,green,grey,yellow,purple,white]
colors_id = ['red','green','grey','yellow','purple','white']


class Player:    
    def __init__(self, id, color, color_id, units, bot_id, order, profile):
        self.id = id
        self.color = color
        self.color_id = color_id
        self.units = units 
        self.bot_id = bot_id
        self.dice_roll = self.roll_dice()
        self.order = order
        self.profile = profile
        self.owns = []
    
    def __repr__(self):
        return f'Player(id={self.id},color={self.color_id},units={self.units}),bot_id={self.bot_id},dice_roll={self.dice_roll},order={self.order}'
    
    def roll_dice(self): 
        return  random.randrange(1,7)
        #print("Player {0} rolled a {1}".format(self.id, self.dice_roll))


class Human:
    def __init__(self, player, territories):
        self.player = player
        self.territories = territories
    
    def empty_populate_territory(self, empty_countries):
        print("Please enter a territory id,")
        t_id = int(input()) 

        if t_id in range(len(self.territories)):
            for i , v in enumerate(empty_countries):
                if v.id == t_id:
                    index = i
            return self.territories[t_id -1], index
        else:
            print("invalid territory id")
            self.empty_populate_territory(self.player, empty_countries)
    
    def pick_territory(self):
        print("Which territory would you like to renforce? Please enter territory id")
        # for id in self.player.owns:
        #     print("Id:{0} Name:{1} Units:{2}".format(self.territories[id].id, self.territories[id].name, self.territories[id].units))
        t_id = int(input()) - 1
        if t_id in range(len(self.territories)):
            print("picked {0}".format( self.territories[t_id].name))
            return self.territories[t_id], t_id
        else:
            print("invalid territory id")
            self.pick_territory()
    
    def pick_units(self, t):
        print("How many units would add to {0}? You have {1} units. {0} has {2} units".format(t.name, self.player.units, t.units))
        try:
            units = int(input)
            return units
        except:
            print("Invalid entry")
            self.pick_units(t)


class Random:
    def __init__(self, player, territories):
        self.player = player
        self.territories = territories
    def empty_populate_territory(self,  empty_countries):
        index =  int(random.randrange(len(empty_countries)))
        t = empty_countries[index]  
        return t, index
    
    def pick_territory(self):
        print("{} which territory would you like to renforce? Please enter territory id".format(self.player.id))
        
        # for id in self.player.owns:
        #     print("Id:{0} Name:{1} Units:{2}".format(self.territories[id].id, self.territories[id].name, self.territories[id].units))
        t_id = int(input()) - 1
        
        if t_id in range(len(self.territories)):
            print("picked {0}".format( self.territories[t_id].name))
            return self.territories[t_id], t_id
        else:
            print("invalid territory id")
            self.pick_territory()
    
    def pick_units(self, t):
        print("How many units would add to {0}? You have {1} units. {0} has {2} units".format(t.name, self.player.units, t.name, t.units))
        units = int(input())
        return units
        # except:
        #     print("Invalid entry")
        #     self.pick_units(t)
    
class CreataePlayers:
    def __init__(self,  territories):
        self.territories = territories

    def orginalUnits(self,num_of_players):
        switch = {
            2: 40,
            3: 35,
            4: 30,
            5: 25,
            6: 20
        }
        return switch.get(num_of_players, "") 

    def selectBotId(self,p):
        print("is player {0} a human? y/n".format(p.id)) 
        human = input()
        if human == 'y':
            p.bot_id = 0
            p.profile = Human(p,self.territories)
        elif human == 'n':
            print("Which bot profile?:Enter 1 for Random, 2 for Passive, and 3 for Agressive")
            bot_id = int(input())
            if bot_id != 1 and bot_id != 2 and bot_id !=3:
                print("Pick only 1, 2, or 3.")
                self.selectBotId(p) 
            p.bot_id = bot_id
            p.profile = Random(p,self.territories)
        else:
            print("Please press only y or n followed by enter.")
            self.selectBotId(p)
        return p

    def createPlayers(self):
        players = []    
        print("How many players are playing?")    
        num_of_players = input()
        try:
            num_of_players = int(num_of_players)
            units = int(self.orginalUnits(num_of_players))
            for i in range(0,num_of_players):
                p = Player(i+1, colors[i], colors_id[i], units, 0, 0,Human(1,self.territories))
                p.profile.player = p
                p = self.selectBotId(p)
                players.append(p)
            players = self.playerOrder(players)  
            return players
        except: 
            print("You must enter a number 2-6")
            self.createPlayers()

    def playerOrder(self, players):        
        dice_rolls = sorted( [(p, p.dice_roll) for p in players], key = lambda x: x[1] )
        ordered_players = []
        for i, tup in enumerate(dice_rolls): 
            tup[0].order = i
            ordered_players.append(tup[0])
        return ordered_players

class Populate:
        def __init__(self, players, territories):
            self.players = players
            self.territories = territories
                    
        def empty_populate_territories(self):
            empty_countries = self.territories.copy()

            while(len(empty_countries) > 0):
                for player in self.players:
                   self.empty_populate_territory(player, empty_countries)
    
        def empty_populate_territory(self, player, empty_countries):
            t, index = player.profile.empty_populate_territory(empty_countries)
            #Territory Valid?
            if t.units == 0:
                    print("Player {0} picked territory {1}".format(player.id, t.name))      
                    t.color = player.color
                    empty_countries.pop(index) 
                    player.owns.append(t.id - 1)
                    t.units = 1
                    return empty_countries
            else:
                print("That territory already has already been chosen. Player {0} picked territory {1}".format(player.id, t.name))
                self.empty_populate_territory(player,empty_countries)
                    
        def first_renforce(self):
            total_units = sum([player.units for player in self.players])
            while total_units > 0:
                for player in self.players:
                    if player.units > 0:
                       self.renforce(player)
                        
        def renforce(self, player):
            t, t_id =  player.profile.pick_territory()
            print(t_id)
            print(player.owns)                     
            if t_id in player.owns:
                self.unit_check(player,t)
            else:
                print("You don't own that territory. Pick one that you own.")
                self.renforce(player)
        
        def unit_check(self, player, t):
            units = player.profile.pick_units(t)
            if player.units - units >= 0:
                player.units = player.units - units
                t.units = t.units + units
                print("Player {0} added {1} to {2}. {2} has a total of {3} units".format(player.id, player.units, t.name, t.units))
            else:
                print("You don't have that many units.")
                units = player.profile.pick_units(t)

c , t = ReadFile()
players = CreataePlayers(t).createPlayers()
pop = Populate(players,t)
pop.empty_populate_territories()
for p in players:
    print("Player {} owns {}".format(p.id,p.owns))
pop.first_renforce()

