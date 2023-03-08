import time

import GamePassive
import World
import Airports
import PlayerData
import PlayerActions
import Menu

Cycle = 0

AirportMarket = {}

while Cycle <= 20:
    Cycle += 1

    for i in range(0,5):
        AirportMarket[i] = Airports.GetRandom()
    def Menu_Buy(Name):

        MenuActions = {}

        for Airport in AirportMarket:
            MenuActions[AirportMarket[Airport]] = PlayerActions.BuyAirport
        MenuActions["Return"] = "Stop"

        Menu.Prompt(MenuActions)
    def Menu_Sell(Name):
        MenuActions = {}

        for Airport in PlayerData.Airports:
            MenuActions[Airport] = PlayerActions.SellAirport
        MenuActions["Return"] = "Stop"

        Menu.Prompt(MenuActions)

    def Menu_Repair(Name):
        MenuActions = {}

        for Airport in PlayerData.Airports:
            MenuActions[Airport] = PlayerActions.Repair
        MenuActions["Return"] = "Stop"

        Menu.Prompt(MenuActions)

    def Status(Empty):
        Menu.Space()
        print("Here is your status:")
        print("Money:",PlayerData.Money)
        print("Loan:", PlayerData.Loan)
        print("Debt:", PlayerData.Debt)
        print("Owned Airports:", PlayerData.Airports)
        print()
        input("Press Enter to continue")

    Menu.Prompt({
        "Buy Airports": Menu_Buy,
        "Sell Airports": Menu_Sell,
        "Take Loan": PlayerActions.TakeLoan,
        "Pay Debt": PlayerActions.PayDebt,
        "Airport Repairs": Menu_Repair,
        "My Status": Status,
        "Continue": "Stop"
    })

    Menu.Space()
    GamePassive.Run()

Menu.Space()

print("Congratulations you finished the game!")

Score = 0
Score += PlayerData.Profit
Score -= PlayerData.Debt

print("Your final score was... ")

time.sleep(1)

print("Drumroll...")

time.sleep(2)

print(Score)
