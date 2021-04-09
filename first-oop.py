from random import randint

class Player:
  def __init__(self, name):
    self.dice = []
    self.name = name  # whatever is passed in is set as the name

  def roll(self):
    self.dice = [] # clears current dice
    for i in range(3):
      self.dice.append(randint(1,6))

  def get_dice(self):
    return self.dice

player1 = Player(input("What is Player1's name? "))
player2 = Player(input("What is Player2's name? "))

player1.roll()
player2.roll()

print(f"{player1.name} rolled {player1.get_dice()}")
print(f"{player2.name} rolled {player2.get_dice()}")

if sum(player1.get_dice()) == sum(player2.get_dice()):
  print("Draw!")
elif sum(player1.get_dice()) > sum(player2.get_dice()):
  print(f"Player 1, {player1.name} wins!")
else:
  print(f"Player 2, {player2.name} wins!")

