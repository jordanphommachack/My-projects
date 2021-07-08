using System;

/** Class Die represents a simple Die object that can roll
 * and store the newly rolled random value between 1 and 6. */
public class Die
{
    public int Value { get; set; }
    private static Random roller = new Random();

    /** Roll the die by assigning a new random integer
     * between 1 and 6 as its value. */
    public static void Roll()
    {
        const int MAX_SIDE_VALUE = 6;
        Value = roller.Next(1, MAX_SIDE_VALUE + 1);
    }
}
