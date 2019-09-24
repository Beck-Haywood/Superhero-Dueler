import random

class Ability:
    def __init__(self, name, attack_strength):
        '''Create Instance Variables:
            name:String
            max_damage: Integer
        '''
        self.name = name
        self.max_damage = attack_strength
    def attack(self):
        ''' Return a value between 0 and the value set by self.max_damage.'''
        return random.randint(0, self.max_damage)
class Armor:
    def __init__(self, name, block_strength):
        self.name = name
        self.max_block = block_strength
    def block(self):
        return random.randint(0, self.max_block)
class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []
    def add_ability(self, ability):
        ''' Add ability to abilites list '''
        self.abilities.append(ability)
    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            ability.attack()
            new_damage = ability.attack()
            total_damage += new_damage
        return total_damage
    def add_armor(self, armor):
        '''Add armor to self.armors
        Armor: Armor Object
        '''
        self.armors.append(armor)
    def defend(self):
        '''Runs 'block' method on each armor.
            Returns sum of all blocks
        '''
        total_block = 0
        for armor in self.armors:
            armor.block()
            new_block = armor.block()
            total_block += new_block
        return total_block
    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense. '''
        block_amt = self.defend()
        self.current_health = self.current_health - abs(block_amt - damage)
    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not.
        '''
        if self.current_health <= 0:
            return False
        else:
            return True
    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.
        '''
        if self.is_alive() == True and opponent.is_alive() == True:
            while self.is_alive() == True and opponent.is_alive() == True:
                opponent.take_damage(self.attack())
                self.take_damage(opponent.attack())
                if self.is_alive() == False and opponent.is_alive() == True:
                    print('{} Wins!'.format(opponent.name))
                elif self.is_alive() == True and opponent.is_alive() == False:
                    print('{} Wins!'.format(self.name))
                elif self.is_alive() == False and opponent.is_alive() == False:
                    print("They both died...")
class Weapon(Ability):
    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        return random.randint((self.max_damage // 2), self.max_damage)
class Team(Hero):
    def __init__(self, name):
        ''' Initialize your team with its team name
        '''
        self.name = name
        self.heroes = []
        # TODO: Implement this constructor by assigning the name and heroes, which should be an empty list
    def add_hero(self, hero):
        self.heroes.append(hero)
    def remove_hero(self, name):
        index = self.heroes.index(name)
        if self.heroes == []:
            return 0
        else:
            self.heroes.pop(index)
    def view_all_hero(self):
        for hero in self.heroes:
            print(hero)
if __name__ == "__main__":
# If you run this file from the terminal
    # this block is executed.
    '''
    my_hero = Hero("Saitama", 100)
    shield = Armor("Sheild", 50)
    my_hero.add_armor(shield)
    my_hero.take_damage(50)
    print(my_hero.current_health)
    '''
    '''
    hero = Hero("Grace Hopper", 200)
    hero.take_damage(150)
    print(hero.is_alive())
    hero.take_damage(15000)
    print(hero.is_alive())
    '''
    #print(my_hero.name)
    #print(my_hero.current_health)
    #my_hero.add_ability(ability)
    #my_hero.add_ability(onepunch)
    #print(my_hero.attack())
    #print(my_hero.abilities)

hero1 = Hero("Wonder Woman")
hero2 = Hero("Dumbledore")
ability1 = Ability("Super Speed", 75)
ability2 = Ability("Super Eyes", 75)
ability3 = Ability("Wizard Wand", 75)
ability4 = Ability("Wizard Beard", 75)
hero1.add_ability(ability1)
hero1.add_ability(ability2)
hero2.add_ability(ability3)
hero2.add_ability(ability4)
hero1.fight(hero2)
print(hero1.current_health)
print(hero2.current_health)

team = Team("Squad Team")
team.add_hero("Beck")
team.view_all_hero()
team.add_hero('Bruh')
team.remove_hero("Beck")
team.view_all_hero()
