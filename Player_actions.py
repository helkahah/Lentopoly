import PlayerData
import Airports
def Upkeep():
    print(PlayerData.Airports)
    for i in PlayerData.Airports():
        print[i]
        check = input('Would you like to pay the upkeep for this airport? yes or no')
        #if check == "yes" and PlayerData.Money>= Airports.Get(i).upkeep

#Upkeep()
def BuyAirport(Name):
    print('poo')

def SellAirport(Name):
    '''
    money = money + sellprice
    return money
    '''

def TakeLoan():
    action = input('Do you want to take a loan? yes or no: ')
    if action == "yes":
        loan = float(input('How much: '))
        PlayerData.Money = PlayerData.Money + loan
        PlayerData.Debt = PlayerData.Debt + loan
        print(PlayerData.Money)
        print(PlayerData.Debt)

#TakeLoan()


def PayDebt():
    if PlayerData.Debt >0:
        check = input('Do you want to pay your debt? yes or no: ')
        if check == "yes":
            on = True
            while on:
                paid = input('How much do you want to pay: ')
                if paid <= PlayerData.Money:
                    print(f'You have paid', paid, '€ of your Debt')
                    PlayerData.Money = PlayerData.Money - float(paid)
                    PlayerData.Debt = PlayerData.Debt - float(paid)
                    print(f'you have', PlayerData.Debt, '€ left to pay.')
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
PayDebt()


