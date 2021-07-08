using System;
/**
 * @author Jordan Phommachack
 */

class Car
{
    public string Make { get; set; }

    public int Mileage { get; set; }

    public Car()
    {
        Make = "";
        Mileage = 0;
    }

    public Car(string newMake, int newMileage)
    {
        newMake = Make;
        newMileage = Mileage;
    }

        
}

