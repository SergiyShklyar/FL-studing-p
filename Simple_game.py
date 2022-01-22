from typing import List, Any

NUMBER_OF_ENEMIES = 3
LIVES_PER_ENEMY = 3
ACTION_PROMPT = "> "


# Count zeros, positive elements in a list and
# sum up all the elements of the list
def zeros_positives_and_sum(a_list):
    z = 0
    p = 0
    s = 0
    for x in a_list:
        if x == 0:
            z = z + 1
        if x > 0:
            p = p + 1
        s = s + x
    return z, p, s


def print_menu():
    print("Attack n    - attack the nth enemy")
    print("Check n     - check the number of lives left of the nth enemy")
    print("Status      - show the number of lives left for every enemy")
    print("Quit        - show the status, and finish the game")


class Enemy:
    def __init__(self, initial_lives=LIVES_PER_ENEMY):
        self.lives = initial_lives

    def is_alive(self):
        return (self.lives > 0)

    # I do not remember what I wanted to do with parameter verbose
    # Print the number of lives left
    def checkLife(self, verbose=False):
        if self.lives:
            if self.lives == 1:
                print("1 life is left.")
            else:
                print(f"{self.lives} lives are left.")
        else:
            print("The enemy is dead.")

    # Take away one life if any lives left, then print the number of lives left
    def attack(self):
        if self.is_alive():
            print("Ouch!", end=" ")
            self.lives -= 1
        self.checkLife(False)


def show_status(enemies):
    list_of_lives_left = [enemy.lives for enemy in enemies]
    number_of_enemies = len(enemies)
    dead_enemies, living_enemies, total_lives_left = zeros_positives_and_sum(list_of_lives_left)
    print('Lives left for each enemy:')
    print(list_of_lives_left)
    print(f'Enemies left: {living_enemies} alive and {dead_enemies} dead.')
    print(" ".join([
        "In total,",
        str(total_lives_left) if total_lives_left else "no",
        "enemy's" if number_of_enemies == 1 else "enemies'",
        "life is left." if total_lives_left == 1 else "lives are left."
    ]))


# string is a character string of format
#   Attack<integer>
#   Check<integer>
#   Status ...
#   Quit ...
# string is case-insensitive
# Spaces around <integer> are allowed. Spaces before "Attack", etc. are not allowed.
# Everything after "Status" or "Quit" is ignored.
# enemies if a list of objects of class Enemy
def action_on_string(string, enemies):
    number_of_enemies = len(enemies)
    lowercase_string = string.lower()

    if lowercase_string.startswith("attack"):
        try:
            n = int(lowercase_string[6::])
        except ValueError:
            pass
        else:
            if 1 <= n <= number_of_enemies:
                enemies[n-1].attack()
    elif lowercase_string.startswith("check"):
        try:
            n = int(lowercase_string[5::])
        except ValueError:
            print("The format of Check command is not recognised")
        else:
            if 1 <= n <= number_of_enemies:
                enemies[n-1].checkLife(verbose=True)
            else:
                print(f"Enemy {n} does not exist")
    elif lowercase_string.startswith("status"):
        show_status(enemies)
    elif lowercase_string.startswith("quit"):
        return False

    return True


# Initialize the list of enemies.
# Create a list of number copies of an instance of class Enemy
# Each enemy has lives_per_an_enemy lives.
def init_the_list_of_enemies(enemies, number=NUMBER_OF_ENEMIES, lives_per_an_enemy=LIVES_PER_ENEMY):
    for i in range(number):
        enemies.append(Enemy(initial_lives=lives_per_an_enemy))


# Global (more precisely, top-level) variables
# The list of objects of class Enemy
the_list_of_enemies: list[Enemy] = []
flag_continue = True

init_the_list_of_enemies(the_list_of_enemies, NUMBER_OF_ENEMIES, LIVES_PER_ENEMY)
print_menu()
while flag_continue:
    input_string = input(ACTION_PROMPT)
    if input_string:
        flag_continue = action_on_string(input_string, the_list_of_enemies)
    else:
        flag_continue = False

show_status(the_list_of_enemies)
