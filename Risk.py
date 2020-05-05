import random
from Input import *

p1 = Player()
p2 = Player()
p3 = Player()    
p4 = Player()

p1.set_pcolor(red)
p2.set_pcolor(blue) 
p3.set_pcolor(green)
p4.set_pcolor(yellow)

players = [p1,p2,p3,p4]
count = 0

for p in players:
    count += 1
    p.add_pmen(30) 
    p.set_pid(count)

input = open_file()
terrtories = input[0]
continents = input[1]

def dice_roll(): 
    return random.randrange(1,7)

def attack(units):
    if units >= 3:
        roll = [dice_roll(),dice_roll(),dice_roll()]
    elif units == 2:
        roll = [dice_roll(),dice_roll()]
    else:
        roll = [dice_roll()]
    return sorted(roll, reverse=True)

def defend(units):
    if units >= 2: 
        roll = [dice_roll(),dice_roll()]
    else: 
        roll = [dice_roll()]
    return sorted(roll, reverse = True)


def play(player, attackers, defending_t, verbose=False):
    d = terrtories[defending_t]
    defenders = d.get_num_of_units()
    if verbose:
        print("Attacker has", attackers, "units")
        print("Defender has", defenders, "units")
        print()

    while attackers > 0 and defenders > 0:
        the_attack = attack(attackers)
        the_defense = defend(defenders)

        if verbose:
            print(the_attack, "vs.", the_defense)

        while len(the_attack) > 0 and len(the_defense) > 0:
            if the_attack.pop(0) > the_defense.pop(0):
                defenders -= 1
                if verbose:
                    print("Defender unit dies ({} left)".format(defenders)) 
            else:
                attackers -= 1
                if verbose:
                    print("Attacker unit dies ({} left)".format(attackers)) 
        if verbose:
            print()
    if attackers > 0:
        if verbose:
            print("Attacker wins with", attackers, "units left")
        return attackers
    else:
        if verbose:
            print("Defender wins with", defenders, "units left")
            c = p.get_color()
            d.set_color = c
        return defenders

def populate(player, id, num):
    player.remove_pmen(num)
    terrtories[id].set_color(player.get_color())
    terrtories[id].add_num_of_units(num)
    return terrtories

#adds units to terrtories that have been selected
def random_reinforce(player,terrtiories):
        owns = player.get_powns()
        while(player.get_pmen()):
            index = random.randrange(len(owns))
            id = owns[index]
            populate(player, id, 1)
        return terrtories
    
#Selects random terrtiories that have not been selected yet 
def claim_random_terr():    
    empty_countries = terrtories.copy()
    while(empty_countries):
        for player in players:
            rand_index =  random.randrange(len(empty_countries))
            rand_id = empty_countries[rand_index].get_id() - 1
            empty_countries.pop(rand_index)            
            populate(player,rand_id,1)
            player.add_t(rand_id)
            if len(empty_countries) == 0: 
                break
    return terrtories

def bonus(p):
    p_owns = p.get_powns()
    for continent in continents: 
        check = all(country in p_owns for country in continent.get_countries())        
        if check is True: 
            p.add_pmen(continent.get_bonus())

def attack_all(p):
    for t in p.get_powns():
       adj_t = terrtories[t].get_adj_list()
       if terrtories[t].get_num_of_units() > 0:
           for at in adj_t:
               if at not in p.get_powns():
                   play(1,at,True)
                   print("here",terrtories[t].get_id(), at)
# claim_random_terr()
# attack_all(p1)