import mysql.connector
import math
import random

Connection = mysql.connector.connect(
    host="localhost",
    user=input("Give server username"),
    password=input("Give user password"),
    database="flight_game"
)


Types = {
    "balloonport": ("Balloonport", 1),
    "heliport": ("Heliport", range(40,60)),
    "seaplane_base": ("Seaplane Base", 1),
    "small_airport": ("Regional Airport", range(40,60)),
    "medium_airport": ("National Ariport", range(40,60)),
    "large_airport": ("International Airport", range(1000,4000))
}

PlayerData = {
    "Money": 0,
    "LoanDept": 0,
    "Airports": {}
}

KnownAirports = {}

def NewAirport(Name):
    Cursor = Connection.cursor()
    Cursor.execute(f"SELECT type, iso_region, iso_country, continent FROM airport WHERE name = '{Name}'")
    CursorData = Cursor.fetchone()
    print(CursorData)

    Type = Types[CursorData[0]]
    PriceRange = Type[1]
    Price = random.randint(PriceRange.start, PriceRange.stop) * 1000000

    KnownAirports[Name] = {
        "Name": Name,
        "Price": Price,

    }

    print("New created!")

    return KnownAirports[Name]
def GetAirport(Name):
    if Name in KnownAirports:
        return KnownAirports[Name]
    else:
        return NewAirport(Name)

#print(GetAirportPrice("Total Rf Heliport"))

print(GetAirport("Total Rf Heliport"))
print(GetAirport("Total Rf Heliport"))