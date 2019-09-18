import random

class Ability:
    def __init__(self, name, attack_strength):
        '''Create Instance Variables:
            name:String
            max_damage: Integer
        '''
        self.name = ""
        self.max_damage = 0
    def attack(self):
        ''' Return a value between 0 and the value set by self.max_damage.'''
        self.max_damage = random.randint(0, 20)
        return self.max_damage
if __name__ == "__main__":
# If you run this file from the terminal
    # this block is executed.
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())