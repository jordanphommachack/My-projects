# @author Jordan Phommachack
# This program creates a list of random exam scores, drops the lowest score,
# and computes the average of all scores before and after the drop.

def main() :

    # Create an empty list named examScores
    examScores = []
  
    # Call fillScores to fill the examScores list. You can first test with
    # scores.txt and then with scores2.txt
    fillScores(examScores,"scores.txt")
  
    # Write one line of code that displays the scores stored in
    # examScores. (The list brackets show automatically when this is done)
    print(examScores)
  
    # Write code that shows (prints) the average of all scores in examScores
    # formatted to two digits after the decimal point and preceded by
    # the heading "Average: " This code should still work even if the
    # list size were to change.
    # Hint: This is very simple if using the built-in list functions
    #       and could be accomplished with one line of code. 
    print("Average: %.2f" % (sum(examScores)/len(examScores)))
  
    # Call dropScore to drop the lowest score from examScores
    dropScore(examScores)

    # Write one line of code that shows the scores stored in
    # examScores. (The list brackets show automatically when this is done)
    print(examScores)

    # Write code that shows the average of all scores in examScores
    # formatted to two digits after the decimal point and preceded by
    # the heading "Average: " This code should still work even if the
    # list size were to change.
    # Hint: This is very simple if using the built-in list functions
    #       and could be accomplished with one line of code.  
    print("Average: %.2f" % (sum(examScores)/len(examScores)))
  

# fillScores fills parExamScores with integer scores from a file
# @param parExamScores An empty list to fill with scores
# @param filename The name of the file containing the scores
def fillScores(parExamScores, fileName):
    inFile = open("scores.txt", "r")
    parExamScores = inFile.read().split()
    inFile.close()

# dropScore removes the lowest score from the list
# @param parExamScores A list containing the scores
def dropScores(parExamScores):
    parExamScores.sort()
    parExamScores.remove(1)

main()