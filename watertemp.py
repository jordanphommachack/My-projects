#@Author Jordan Phommachack
SOLID = 32
LIQUID = 33
GAS = 212
answer = "Y"
while answer.upper() == "Y":
    temp = float(input("Degrees Fahrenheit: "))
    if temp <= SOLID:
        print("Solid")
    elif temp > SOLID and temp < GAS:
        print("Liquid")
    elif temp >= GAS:
        print("Gas")
    answer = input("Again? Y or N ")   
    
        