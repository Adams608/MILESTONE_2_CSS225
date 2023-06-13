#Adam Gboyega-dixon
#6/6/2023
class character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

        def get_model(self):
            return self.nickname

        def get_year(self):
            return self.weapons

        def get_color(self):
            return self.weaknesses

        def profile(self):
            return self.nickname, self.weapons, self.weaknesses


player1 = character('', '', '')
player1.nickname = 'Dragon Slayer'
player1.weapons = ['pan', 'paper', 'idea', 'rope', 'groceries']
player1.weaknesses = ['slow']
for item in player1.weapons:
    print("Item: ", item)
    for debuff in player1.weaknesses:
        print("Debuff: ", debuff)

task = input("What task shall you complete today?? " + "will you cook, climb, write: ")
# Climbing a mountain

if (task == 'climb' and player1.weaknesses != 'slow'):
    print("Player cannot climb mountain")
elif len(player1.weapons):
    print('The player can climb')
else:
    print("The player will not climb a mountain")

# Cooking
if task == "cook":
    if player1.weaknesses == "small":
        print("This Player cannot cook")
    elif ('pan' in player1.weaknesses and 'groceries' in player1.weaknesses):
        print("The player can cook")
    else:
        print("The player cannot cook")

# To write a book
if task == 'write':
    if player1.weaknesses != "confusion":
        print("The player cannot write a book")
    elif (('pen', 'paper', 'idea') in player1.weapons):
        print("This charater can write a book")
    else:
        print("The character will not write a book")


