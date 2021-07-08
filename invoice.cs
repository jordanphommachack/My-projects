

/**@Author Jordan Phommachack */

class Invoice
{
    private int quantity;
    private decimal pricePerItem;

    public string PartNumber { get; set; }
    public string PartDescription { get; set; }

   public Invoice()
    {
        PartNumber = "";
        PartDescription = "";
        Quantity = 0;
        PricePerItem = 0;
    }
    
    public Invoice(string partNumber, string partDescription, 
        int quantity, decimal pricePerItem)
    {
        PartNumber = partNumber;
        PartDescription = partDescription;
        Quantity = quantity;
        PricePerItem = pricePerItem;

    }

    public int Quantity
    {
        get
        {
            return quantity;
        }
        set
        {
            if (value >= 0)
                quantity = value;
        }
    }//end quantity
    public decimal PricePerItem
    {
        get
        {
            return pricePerItem;
        }
        set
        {
            if (value >= 0)
                pricePerItem = value;
        }
    }
    
    public decimal GetInvoiceAmount ()
    {
        return Quantity * PricePerItem;
    }
}

