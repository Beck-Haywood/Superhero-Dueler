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
        self.deaths = 0
        self.kills = 0
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
        if damage < block_amt:
            self.current_health = self.current_health
        else: 
            self.current_health = self.current_health - (damage - block_amt)
    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not.
        '''
        if self.current_health <= 0:
            return False
        else:
            return True
    def add_kill(self, num_kills):
        '''Update kills with num_kills'''
        self.kills += num_kills
        
    def add_death(self, num_deaths):
        ''' Update deaths with num_deaths'''
        self.deaths += num_deaths
    def calculate_hero_stats(self):
        if self.deaths > 0 and self.kills > 0:
            kd_ratio = self.kills // self.deaths
        elif self.deaths > 0 and self.kills <= 0:
            kd_ratio = 0
        else:
            kd_ratio = self.kills
        print(f"{self.name} K/D ratio is {kd_ratio}")
    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.
        '''
        if self.is_alive() == True and opponent.is_alive() == True:
            while self.is_alive() == True and opponent.is_alive() == True:
                opponent.take_damage(self.attack())
                self.take_damage(opponent.attack())
                #print(self.current_health)
                #print(opponent.current_health)
                if self.is_alive() == False and opponent.is_alive() == True:
                    print('{} Wins!'.format(opponent.name))
                    opponent.add_kill(1)
                    self.add_death(1)
                elif self.is_alive() == True and opponent.is_alive() == False:
                    print('{} Wins!'.format(self.name))
                    self.add_kill(1)
                    opponent.add_death(1)
                elif self.is_alive() == False and opponent.is_alive() == False:
                    print("They both died...")
                    self.add_kill(1)
                    opponent.add_death(1)
                    opponent.add_kill(1)
                    self.add_death(1)
    def add_weapon(self, weapon):
        '''add weapon to self.abilities'''
        self.abilities.append(weapon)
        pass
class Weapon(Ability):
    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        return random.randint((self.max_damage // 2), self.max_damage)
class Team(object):
    def __init__(self, name):
        ''' Initialize your team with its team name
        '''
        self.name = name
        self.heroes = []
        # TODO: Implement this constructor by assigning the name and heroes, which should be an empty list
    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, name):
        index = 0
        length = len(self.heroes)
        for hero in self.heroes:
            if hero.name == name:
                del self.heroes[index]
            else:
                index += 1
        if len(self.heroes) == length:
            return 0
    def view_all_hero(self):
        for hero in self.heroes:
            print(str(hero.name))
    def team_members_alive(self):
        heroes_alive = []
        for hero in self.heroes:
            if hero.is_alive() == True:
                heroes_alive.append(hero)
        return heroes_alive
    def number_of_team_members_alive(self):
        number_heroes_alive = 0
        for hero in self.heroes:
            if hero.is_alive() == True:
                number_heroes_alive += 1
        return number_heroes_alive
    def attack(self, other_team):
        #create an instance of 1 hero and another randomize them on each team and set equal to the instance  then call fight on eachother
        while self.number_of_team_members_alive() > 0 and other_team.number_of_team_members_alive() > 0:
            hero1 = random.choice(self.team_members_alive())
            hero2 = random.choice(other_team.team_members_alive())
            hero1.fight(hero2)
    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = 100
    def stats(self):
        for hero in self.heroes:
            hero.calculate_hero_stats()
class Arena:
    def __init__(self):
        '''Instantiate properties
        team_one: None
        team_two: None
        '''
        self.team_one = None
        self.team_two = None
    def create_ability(self):
        '''Prompt for Ability information.
        return Ability with values from user Input
        '''
        ability_name = input("Input ability name ").lower()
        ability_damage = int(input("Input ability damage "))
        return Ability(ability_name, ability_damage)
    def create_weapon(self):
        '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''
        weapon_name = input("Input weapon name ").lower()
        weapon_damage = int(input("Input weapon damage "))
        return Ability(weapon_name, weapon_damage)
    def create_armor(self):
        '''Prompt user for Armor information
          return Armor with values from user input.
        '''
        armor_name = input("Input armor name ").lower()
        armor_points = int(input("Input armor value "))
        return Armor(armor_name, armor_points)
    def create_hero(self):
        '''Prompt user for Hero information
          return Hero with values from user input.
        '''
        
        hero_name = input("Input hero name ").lower()
        hero_health = int(input("Input hero health "))
        hero = Hero(hero_name, hero_health)

        desicion_ability = "YES"
        while desicion_ability == "YES":
            ability  = self.create_ability() 
            hero.add_ability(ability)
            desicion_ability = input("Would you like to add another ability? (Yes or No) ").upper()

        desicion_weapon = "YES"
        while desicion_weapon == "YES":
            weapon  = self.create_weapon() 
            hero.add_weapon(weapon)
            desicion_weapon = input("Would you like to add another weapon? (Yes or No) ").upper()

        desicion_armor = "YES"
        while desicion_armor == "YES":
            armor = self.create_armor() 
            hero.add_armor(armor)
            desicion_armor = input("Would you like to add more armor? (Yes or No) ").upper()
        # return the new hero object
        return hero
    def build_team_one(self):
        '''Prompt the user to build team_one '''
        # TODO: This method should allow a user to create team one.
        # Prompt the user for the number of Heroes on team one
        number_of_team_members = int(input("Choose the amount of heros on this team (Enter a Whole Number) ")) 
        team_name = input("Enter a team name: ")
        self.team_one = Team(team_name)
        for i in range(number_of_team_members):
            hero = self.create_hero()
            self.team_one.heroes.append(hero)
            i += 1
            i -= 1
        return self.team_one
        
    def build_team_two(self):
        '''Prompt the user to build team_two'''
        # TODO: This method should allow a user to create team two.
        # Prompt the user for the number of Heroes on team two
        number_of_team_members = int(input("Choose the amount of heros on this team (Enter a Whole Number) ")) 
        team_name = input("Enter a team name: ")
        self.team_two = Team(team_name)
        for i in range(number_of_team_members):
            hero = self.create_hero()
            self.team_two.heroes.append(hero)
            i += 1
            i -= 1
        return self.team_two
    def team_battle(self):
        team_one = self.team_one
        team_two = self.team_two
        team_one.attack(team_two)
    def team_kda(self, team):
        team_deaths = 0
        team_kills = 0
        for hero in team.heroes:
            team_deaths += hero.deaths
            team_kills += hero.kills
        if team_deaths < 1:
            team_kda = team_kills
        else:
            team_kda = team_kills // team_deaths
        return team_kda
        
    def winner(self):
        if self.team_kda(self.team_one) > self.team_kda(self.team_two):
            return self.team_one
        else:
            return self.team_two
    def loser(self):
        if self.team_kda(self.team_one) < self.team_kda(self.team_two):
            return self.team_one
        else:
            return self.team_two
    def alive_heroes(self):
        alive_heroes = []
        for hero in self.winner().team_members_alive():
            alive_heroes.append(hero.name)
        return alive_heroes
    def show_stats(self):
        print(f"Winning team: {self.winner().name}" )
        print(f"Alive heroes: {self.alive_heroes()}")
        print(f"Winning team's KDA: {self.team_kda(self.winner())}")
        print(f"Losing team's KDA: {self.team_kda(self.loser())}")

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()