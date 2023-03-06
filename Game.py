import World
import Airports
import GameActions
import PlayerData
import Menu

Cycle = 0

while Cycle <= 20:
    Cycle += 1
    def Menu_Buy():
        print("What do you want to buy?")
    def Menu_Sell():
        print("What do you want to sell?")

    Menu({
        "Buy": Menu_Buy,
        "Sell": Menu_Sell,
        "Continue": "Stop"
    })

    print("Passive!")

