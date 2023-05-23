import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = random.randint(40, 50)
        self.damage = random.randint(15, 30)
        self.defense = False

    def attack(self, opponent):
        damage = self.damage
        if random.randint(1, 10) == 10:
            print("Critical hit!")
            damage += 10
        if opponent.defense:
            damage /= 4
            print(f"{opponent.name} защитился от атаки!")
        opponent.health -= damage
        print(f"{self.name} атаковал {opponent.name} на {damage} урона!")
        print(f"У {opponent.name} осталось {opponent.health} здоровья.")
        if opponent.defense:
            opponent.reset_defense()

    def defend(self):
        self.defense = True
        print(f"{self.name} защищается!")

    def reset_defense(self):
        self.defense = False
        print(f"{self.name} больше не защищается")

# Ask for player names
name1 = input("Введите имя для игрока 1: ")
name2 = input("Введите имя для игрока 2: ")

# Create players
player1 = Player(name1)
player2 = Player(name2)

# Game loop
while player1.health > 0 and player2.health > 0:
    print()
    print(f"{player1.name} осталось {player1.health} здоровья.")
    print(f"{player2.name} осталось {player2.health} здоровья.")

    # Player 1's turn
    print(f"Ходит {player1.name}.")
    action = input("Вы хотите атаковать или защититься? ")
    if action.lower() == "атаковать":
        player1.attack(player2)
    elif action.lower() == "защититься":
        player1.defend()
    else:
        print("Некорректное действие. Ход пропущен.")

    # Player 2's turn
    print(f"Ходит {player2.name}.")
    action = input("Вы хотите атаковать или защититься? ")
    if action.lower() == "атаковать":
        player2.attack(player1)
    elif action.lower() == "защититься":
        player2.defend()
    else:
        print("Некорректное действие. Ход пропущен.")


# Game over
if player1.health > 0:
    print(f"{player1.name} победил(а)!")
elif player2.health > 0:
    print(f"{player2.name} победил(а)!")
else:
    print("Ничья!")
