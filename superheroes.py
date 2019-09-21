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
    def defend(self, damage_amt):
        '''Runs 'block' method on each armor.
            Returns sum of all blocks
        '''
        total_block = 0
        for armor in self.armors:
            armor.block()
            new_block = ability.attack()
            total_block += new_block

if __name__ == "__main__":
# If you run this file from the terminal
    # this block is executed.
    ability = Ability("Great Debugging", 50)
    onepunch = Ability("OnePunch", 50)
    print(ability.name)
    print(ability.attack())
    print(onepunch.name)
    print(onepunch.attack())
    my_hero = Hero("Saitama", 20000)
    #print(my_hero.name)
    #print(my_hero.current_health)
    my_hero.add_ability(ability)
    my_hero.add_ability(onepunch)
    print(my_hero.attack())
    #print(my_hero.abilities)

