import PlayerData
import Airports
import World
import random

def Disaster(Airport):
    Continent = Airport["Continent"]
    Disaster = random.choice(World.Continents[Continent][1])
    DisasterChance = Disaster[1]
    Random = random.uniform(0, 1)
    if Random <= DisasterChance:
        if Airport["Damage"] < 5:
            Airport["Damage"] += World.DisasterDamage[Disaster[0]]
            print(World.DisasterDescription[Disaster[0]])
            print(f"Your airport", Airport["Name"], "has received damage and now its damage level is ", Airport["Damage"])
def Run():
    PlayerData.Debt += PlayerData.Loan * 0.04
    print()
    for AirportName in PlayerData.Airports:
        Airport = Airports.Get(AirportName)
        Disaster(Airport)
        Profit = random.randint(Airport["Revenue"].start, Airport["Revenue"].stop) * Airports.MoneyMultiplier
        if Airport["Damage"] > 0:
            NetProfit = Profit / Airport["Damage"]
            print("Your airport", Airport["Name"], "has earned", NetProfit)
            PlayerData.Money += NetProfit
            PlayerData.Profit += NetProfit
        else:
            print("Your airport", Airport["Name"], "has earned", Profit)
            PlayerData.Money += Profit
            PlayerData.Profit += Profit
        print()

