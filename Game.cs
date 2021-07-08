using System;
using System.IO;

/** 
 * @author Jordan Phommachack
 * class Game represents a dice game between two players. Each player rolls
 * dice a given number of turns. The dice are added up each turn. For each
 * die face value that matches the bonus value, a certain extra amount of
 * points are awarded. The number of wins are tallied for each player. */
class Game
{
    //** ADD fields and properties here 
    private string player1;
    private string player2;
    public int BonusValue { get; set; }
    public int NumRounds { get; set; }

    /** Constructor, already completed */
    public Game(string configFile)
    {
        SetData(configFile);
    }

    /**
    * SetData sets game data that is read from a config file
    * @param configFile The name of the file to read (it includes the extension)
    *                   This file is located in the Visual Studio source code
    *                   folder. 
		* ADD code to complete the method. */
    public void SetData(string configFile)
    {
        string filePath = @"..\..\";
        string fileName = "config.txt";
        StreamReader inFile = new StreamReader(filePath + fileName);

        NumRounds = Convert.ToInt32(inFile.ReadLine());
        inFile.Close();
    } // end SetData

    /** Play runs the dice game 
		 * ADD code to complete the method.*/
    public void Play()
    {
        RollDice();
    } // end Play
} // end class
