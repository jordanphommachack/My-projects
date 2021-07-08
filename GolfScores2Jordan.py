# @author Jordan Phommachack
# This program computes the best ball score for two paired players.
from random import randint

def main() :
  player1Scores = []
  player2Scores = []
  player3Scores = []
  pars = []
  # call fillGolfScores for par scores
  fillGolfScores(pars);
  print("Par: ", end = "")
  displayScores(pars);
  print()
  # Call fillGolfScores with the first player's list
  fillGolfScores(player1Scores);
  # Call fillGolfScores with the second player's list
  fillGolfScores(player2Scores);
  # Call fillGolfScores with the third player's list
  fillGolfScores(player3Scores);
  print("Player 1: ", end = "")
  # Call displayScores with the first player's list
  displayScores(player1Scores);
  print("Player 2: ", end = "")
  # Call displayScores with the second player's list
  displayScores(player2Scores);
  # Call displayScores with the third player's list
  print("Player 3: ", end = "")
  displayScores(player3Scores);
  # Determine the bestBallScore by calling the bestBallScore function
  # and displaying the result preceded by "Best ball score: "
  bestBallScore(player1Scores,player2Scores,player3Scores);
  
  #Shows how well player did against par
  print()
  print("Compared to Par: ")
  print("Player 1: ", end = "")
  compareToPar(pars, player1Scores);
  print("Player 2: ", end ="")
  compareToPar(pars, player2Scores);
  print("Player 3: ", end ="")
  compareToPar(pars, player3Scores);

# fillGolfScores fills in playerScores with 18 random integers 
# in the range [2, 6]
# @param playerScores An empty list to fill with 18 random scores
def fillGolfScores(playerScores) :
  LOW_SCORE = 2
  HIGH_SCORE = 6
  MAX_SCORES = 4
  scores = 0
  while scores < MAX_SCORES:
    playerScores.append(randint(LOW_SCORE, HIGH_SCORE))
    
    scores = scores + 1

# displayScores displays the scores for a given golfer on one line
# separated by spaces. After all scores are displayed use a print() statement
# to advance output to the next line.
# @param playerScores A list of scores for the golfer
def displayScores(playerScores) :
  total = 0
  for i in range(len(playerScores)):
    total += playerScores[i]
    print(playerScores[i], end= " ")
  if i < len(playerScores):
    print("", end ="(%s)" % total )
  print()
  
  
  
  
# bestBallScore calculates and returns the best ball score for the two players.
# @param parPlayer1Scores A list of scores for player 1
# @param parPlayer2Scores A list of scores for player 2
# @param parPlayer3Scores A list of scores for player 3
# @return The best ball score
def bestBallScore(parPlayer1Scores, parPlayer2Scores, parPlayer3Scores) :
  bestScore = 0;
  for i in range(len(parPlayer1Scores)) :
    if parPlayer1Scores[i] > parPlayer2Scores[i] and parPlayer2Scores[i] < parPlayer3Scores[i]:
      bestScore += parPlayer2Scores[i]
    elif parPlayer1Scores[i] < parPlayer2Scores[i] and parPlayer3Scores[i] > parPlayer1Scores[i]:
      bestScore += parPlayer1Scores[i]
    elif parPlayer3Scores[i] < parPlayer2Scores[i] and parPlayer1Scores[i] > parPlayer3Scores[i]:
      bestScore += parPlayer3Scores
    elif parPlayer1Scores[i] == parPlayer2Scores[i] and parPlayer1Scores[i] == parPlayer3Scores[i]:
      bestScore += parPlayer1Scores[i]
  print("Best ball score: {}".format(bestScore))
  return bestScore

def compareToPar(pars, playerScores):
  result = 0
  for i in range(len(playerScores)):
    result = playerScores[i] - pars[i]
    print(result, end = " ")
  print()




main()