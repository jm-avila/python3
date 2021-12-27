import random
from .magic import Spell

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[94m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def get_name(self):
        print("\n" + bcolors.BOLD + "  " + self.name + bcolors.ENDC)

    def choose_action(self):
        i = 1
        self.get_name()
        print(bcolors.OKBLUE + bcolors.BOLD + "  ACTIONS:" + bcolors.ENDC)
        for item in self.actions:
            print("    " + str(i) + ":", item)
            i += 1

    def choose_magic(self):
        i = 1
        print(bcolors.OKBLUE + bcolors.BOLD + "  MAGIC:" + bcolors.ENDC)
        for spell in self.magic:
            print("    " + str(i) + ":", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1

    def choose_item(self):
        i = 1
        print(bcolors.OKGREEN + bcolors.BOLD + "  ITEMS:" + bcolors.ENDC)
        for item in self.items:
            print("    " + str(i) + ".", item["item"].name, ":", item["item"].description + " (x" + str(item["quantity"]) + ")")
            i += 1

    def get_hp_bar(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 / 4
        
        while bar_ticks > 0:
            hp_bar += "▓"
            bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        return hp_bar

    def get_bars(self, current_value, max_value, num_of_spaces):
        bars = ""
        bar_ticks = (current_value / max_value) * num_of_spaces
        
        while bar_ticks > 0:
            bars += "▓"
            bar_ticks -= 1

        while len(bars) < num_of_spaces:
            bars += " "

        return bars

    def get_stat_string(self, current_value, max_value, num_of_spaces):
        string = str(current_value) + "/" + str(max_value)
        string_len = len(string)
        value = ""

        if string_len < num_of_spaces:
            decreased = num_of_spaces - string_len

            while decreased > 0:
                value += " "
                decreased -= 1

            value += string
        else:
            value = string

        return value

    def get_stats(self):
        hp_bar = self.get_bars(self.hp, self.maxhp, 25)
        mp_bar = self.get_bars(self.mp, self.maxmp, 10)
        hp_string = self.get_stat_string(self.hp, self.maxhp, 11)
        mp_string = self.get_stat_string(self.mp, self.maxmp, 9)

        print("                        -------------------------                ----------")
        print(bcolors.BOLD + self.name + ":     " + hp_string + " |" + bcolors.OKGREEN + hp_bar + bcolors.ENDC + bcolors.BOLD + "|    " + mp_string + " |" + bcolors.OKBLUE + mp_bar + bcolors.ENDC + "|")