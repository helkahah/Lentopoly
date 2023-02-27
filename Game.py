import World
import Airports
import GameActions


PlayerData = {
    "Money": 0,
    "LoanDept": 0,
    "Airports": {}
}

Cycle = 0

#print(GetAirportPrice("Total Rf Heliport"))

print(Airports.Get("Total Rf Heliport"))
print(Airports.Get("Total Rf Heliport"))

#Menu Functions

def PromptActions(Actions, *args):
    ActionCount = 1

    CurrentActions = {}

    for Key in Actions:
        print(ActionCount, Key)
        CurrentActions[ActionCount] = Key
        ActionCount += 1

    Action = int(input())

    print(GameActions.Actions[CurrentActions[Action]](args))



    return CurrentActions[Action]
def Menu_Buy():
    print("Test")


Menus = {
    "Buy": Menu_Buy,
    "Sell": None,
    "Loan": None,
}

while Cycle <= 20:
    Cycle += 1
    Action = PromptActions(
        [
            "Buy",
            "Sell",
            "Continue",
        ]
    )