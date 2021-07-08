/** class Item represents an item with a name, price, and quantity. */
public class Item
{
    public string Name { get; set; }
    public decimal Price { get; set; }
    public int Quantity { get; set; }

    public Item(string newName, decimal newPrice, int newQuantity)
    {
        Name = newName;
        Price = newPrice;
        Quantity = newQuantity;
    }

    public static bool operator > (Item left, Item right)
    {
        return left.Price > right.Price;
    }
    public static bool operator < (Item left, Item right)
    {
        return left.Price < right.Price;
    }
}
