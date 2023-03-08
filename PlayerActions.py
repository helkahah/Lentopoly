import time

import PlayerData
import Airports
import Menu
def BuyAirport(Name):
    Airport = Airports.Get(Name)
    Price = Airport["Price"]
    Revenue = Airport["Revenue"]
    SellPrice = Airport["SellPrice"]
    RepairCost = Airport["RepairCost"]
    Region = Airport["Region"]
    Country = Airport["Country"]
    Continent = Airport["Continent"]

    Menu.Space()

    print(f"The airport",Name,"has these stats:")

    print(f"Region:",Region)
    print(f"Country:",Country)
    print(f"Continent:",Continent)
    print()
    print(f"Sell price:", SellPrice)
    print(f"Cost for repairs:", RepairCost)
    print(f"Monthly Revenue:", Revenue)
    print(f"Price:", Price)
    print()
    while True:
        print(f"You have", PlayerData.Money, "€ in your bank")
        choice = input("Do you want to buy this airport? yes or no")
        if choice == "yes":
            if PlayerData.Money >= Price:
                PlayerData.Airports.append(Name)
                PlayerData.Money -= Price
                print()
                print(f'You now own', Name)
                return
            else:
                print("You don't have enough money to buy this")
                return
        elif choice == "no":
            print(f"You chose not to buy", Name)
            return
        else:
            print("Me no understando")

def SellAirport(Name):
    Airport = Airports.Get(Name)
    SellPrice = Airport["SellPrice"]
    choice = input(f"Do you want to sell {Name} for {SellPrice}€? yes or no")
    while True:
        if choice == "yes":
            if Name in PlayerData.Airports:
                PlayerData.Money += SellPrice
                PlayerData.Airports.remove(Name)
                print("You have", PlayerData.Money, "€ in your bank.")
            else:
                print("You've already sold this airport!")

            return
        elif choice == "no":
            print("You chose not to sell", Name)
            return
        else:
            print("Are you trying to annoy me?")


def Repair(Name):
    Airport = Airports.Get(Name)

    Damage = Airport["Damage"]
    RepairCost = Airport["RepairCost"] * Damage

    print(f"{Name} airport's damage level is {Damage}. Do you want to repair the airport for {RepairCost}?")

    def LocalRepair(Empty):
        if PlayerData.Money >= RepairCost:
            Airport["Damage"] = 0
            PlayerData.Money -= RepairCost
            print(Name,"was repaired! Its damage level is no 0.")

    Menu.Prompt({
        "Yes":LocalRepair,
        "No":"Stop"
    })
def TakeLoan(Empty):
    while True:
        action = input('Do you want to take a loan? yes or no: ')
        if action == "yes":
            loan = float(input('How much: '))
            PlayerData.Loan += loan
            PlayerData.Money += loan
            PlayerData.Debt += loan
            print(f'You have received', loan, '€')
            return
        elif action == "no":
            return
        else:
            print("I didn't understand that, try again.")
def PayDebt(Empty):
    if PlayerData.Debt >0:
        check = input('Do you want to pay your debt? yes or no: ')
        if check == "yes":
            while True:
                paid = float(input('How much do you want to pay: '))
                if paid <= PlayerData.Money:
                    print(f'You have paid', paid, '€ of your Debt')
                    PlayerData.Money -= float(paid)
                    PlayerData.Debt -= float(paid)
                    print(f'you have', PlayerData.Debt, '€ left to pay.')
                    if PlayerData.Debt == 0:
                        PlayerData.Loan == 0
                        print('You have paid off your loan, congrats!')
                        return
                    else:
                        return
                elif paid == "cancel":
                    print('Game will continue')
                    return
                else:
                    print(f'You have', PlayerData.Money, '€ in your wallet')
                    print('Try again or type "cancel" to cancel paying your debt')
        else:
            print('Game will continue')
            return
    else:
        return



