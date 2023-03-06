import World
import Airports
import GameActions
import PlayerData
import Menu

Cycle = 0

while Cycle <= 20:
    Cycle += 1
    def Menu_Buy(Name, Shared):
        print("What do you want to buy?")
    def Menu_Sell(Name, Shared):
        print(Name, Shared)
        print("What do you want to sell?")

    Menu.Prompt({
        "Buy Airports": Menu_Buy,
        "Sell Airports": Menu_Sell,
        "Continue": "Stop"
    }, "Test")

    print("Passive!")

