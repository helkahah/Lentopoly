import mysql.connector
import math
import random
import World
import DatabaseUser

MoneyMultiplier = 100000

Connection = mysql.connector.connect(
    host="localhost",
    user=DatabaseUser.Username,
    password=DatabaseUser.Password,
    database="flight_game"
)
Types = {
    "balloonport": ("Balloonport", 1, range(4, 6), 0.3),
    "heliport": ("Heliport", range(400,600), range(200, 400), 150),
    "seaplane_base": ("Seaplane Base", 1, range(4, 6), 3),
    "small_airport": ("Regional Airport", range(500,1500), range(300, 800), 200),
    "medium_airport": ("National Ariport", range(1000,5000), range(800, 3800), 600),
    "large_airport": ("International Airport", range(20000,40000), range(18000, 30000), 15000)
}

KnownAirports = {}
def New(Name):
    Cursor = Connection.cursor()
    Cursor.execute(f"SELECT type, iso_region, iso_country, continent FROM airport WHERE name = '{Name}'")
    CursorData = Cursor.fetchone()

    Type = Types[CursorData[0]]
    PriceRange = Type[1]
    RevenueRange = Type[2]
    Maintenance = Type[3] * MoneyMultiplier
    Price = random.randint(PriceRange.start, PriceRange.stop) * MoneyMultiplier
    Revenue = random.randint(RevenueRange.start, RevenueRange.stop) * MoneyMultiplier
    SellPrice = Price * 0.7

    KnownAirports[Name] = {
        "Name": Name,
        "Price": Price,
        "Revenue": RevenueRange,
        "SellPrice": SellPrice,
        "RepairCost": Maintenance,
        "Region": CursorData[1],
        "Country": CursorData[2],
        "Continent": CursorData[3],
        "Damage": 0
    }

    print("New created!")

    return KnownAirports[Name]

def Get(Name):
    if Name in KnownAirports:
        return KnownAirports[Name]
    else:
        return New(Name)

def GetRandom():
    Cursor = Connection.cursor()
    Cursor.execute(f"SELECT name FROM airport WHERE NOT type = 'closed'")
    CursorData = Cursor.fetchall()

    return random.choice(CursorData)[0]

def Get(Name):
    if Name in KnownAirports:
        return KnownAirports[Name]
    else:
        return New(Name)
