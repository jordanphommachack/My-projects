using System;

/**
 * @Authors Thomas Bauer, Jordan Phommachack
 **/
class Soda : Item
{
  public bool HasCaffeine { get; set; }

  public Soda() : base()
  {
    HasCaffeine = false;
  }

  public Soda(string newName, decimal newPrice, int newQuantity,
      bool hasCaffeine) : base(newName, newPrice, newQuantity)
  {
    HasCaffeine = hasCaffeine;
  }

  public override void Display()
  {
    base.Display();
    if (HasCaffeine)
    {
      Console.Write(" (caffeine)");
    }
    else
    {
      Console.Write(" (no caffeine)");
    }
  }

  public override string ToString()
  {
    return string.Format("{0},{1}", base.ToString(), HasCaffeine);
  }
}
