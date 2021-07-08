using System;
/** 
 * @author Jordan Phommachak
 */
class Building
{
    private int numFloors;
    private int squareFeet;

    public int NumFloors
    {
        get { return numFloors; }
        set
        {
            if (value >= 0)
                this.numFloors = value;
        }
    }

    public int SquareFeet
    {
        get { return squareFeet; }
        set
        {
            if (value >= 0)
                this.squareFeet = value;
        }
    }

    public Building()
    {
        squareFeet = numFloors = 0;
    }

    public Building(int newSquareFeet, int newNumFloors)
    {
        squareFeet = newSquareFeet;
        numFloors = newNumFloors;
    }

    public override string ToString()
    {
        return $"Square feet: {squareFeet}\nNumber of Floors: {numFloors}";
    }
}
    

