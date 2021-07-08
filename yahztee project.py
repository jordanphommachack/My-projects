from random import randint
#@Author Jordan Phommachack
YAHTZEE_POINTS = 50
TWO_OF_KIND = 25
playerPoints = 0
computerPoints = 0
die1 = 0
die2 = 0
die3 = 0

answer =  input("wanna play Yahtzee? Y or N: ")
while answer.upper() == 'Y':
     die1 = randint(1,6)
     die2 = randint(1,6)
     die3 = randint(1,6)
     print("Player Roll:", die1, die2, die3)
     if die1 == die2 and die2 == die3:
          playerPoints = playerPoints + YAHTZEE_POINTS
          print("Yahtzee! (+50)")
     elif die1 == die2:
          playerPoints = playerPoints + TWO_OF_KIND
          print("Two of a Kind! (+25)")
     elif die1 == die3:
          playerPoints = playerPoints + TWO_OF_KIND
          print("Two of a Kind! (+25)")
     elif die2 == die3:
          playerPoints = playerPoints + TWO_OF_KIND
          print("Two of a Kind! (+25)")
     else:
          playerPoints = playerPoints + die1 + die2 + die3
          print("Chance! (+{})".format(die1 + die2 + die3))
     die1 = randint(1,6)
     die2 = randint(1,6)
     die3 = randint(1,6)
     print("Computer Roll:", die1, die2, die3)
     if die1 == die2 and die2 == die3:
          computerPoints = computerPoints + YAHTZEE_POINTS
          print("Yahtzee! (+50)")
     elif die1 == die2:
          computerPoints = computerPoints + TWO_OF_KIND
          print("Two of a Kind! (+25)")
     elif die1 == die3:
          computerPoints = computerPoints + TWO_OF_KIND
          print("Two of a Kind! (+25)")
     elif die2 == die3:
          computerPoints = computerPoints + TWO_OF_KIND
          print("Two of a Kind! (+25)")
     else:
          computerPoints = computerPoints + die1 + die2 + die3
          print("Chance! (+{})".format(die1 + die2 + die3))     
     
     print("==================================")
     print("Player points: {}".format(playerPoints))
     print("Computer points: {}".format(computerPoints))
     print("==================================")
     answer = input("Roll again? Y or N: ")
print("==================================")
print("Player points: {}".format(playerPoints))
print("Computer points: {}".format(computerPoints))
print("==================================")