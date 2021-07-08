using System;

/**
 * @author Jordan Phommachack
 * Class Player represents a player with a name and a cup of dice to roll.
 * It also tracks the number of wins  */
class Player
{
    //** ADD fields and properties here
    public string Name { get; set; }
    public int Wins { get; set; }
    private Die[] cup;
    /** ADD code for the Constructor
    * @param newName The name of the player
    * @param cupSize The number of dice contained in the cup */
    public Player(string newName, int cupSize)
    {
        Name = newName;
        cup = new Die[cupSize];
        for (int i = 0; i < cup.Length; i++)
        {
            cup[i] = new Die();
        }
    }

    /** RollDice rolls the dice for the player 
		 *  ADD code to complete the method. */
    public void RollDice()
    {
        for (int i = 0; i < cup.Length; i++)
        {
            Die.Roll();
        }
    }

    /** ShowDice shows the values of all dice on one line with space 
  * delimiters. After showing, output is advanced to the next line.
	* ADD code to complete the method. */
    public void ShowDice()
    {
        for (int i = 0; i < cup.Length; i++)
        {
            Console.Write(cup[i] + " ");
            Console.WriteLine();
        }
    }

    /**
  * GetScore determines the total score of the dice in the cup. Each 
  * score added is either the value of the die or 10 points if the die
  * value matches the bonus value.
  * @param bonusValue The value that will earn 10 points.
  * @return the total score
	* ADD code to complete the method. */
    public int GetScore(int bonusValue)
    {
        int totalScore = 0;
        for (int i = 0; i < cup.Length; i++)
        {
            if (cup[i] == bonusValue)
            {

            }
        }
    }

} // end player
