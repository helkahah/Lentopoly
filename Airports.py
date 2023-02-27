import mysql.connector
import math
import random
import World
import DatabaseUser

Connection = mysql.connector.connect(
    host="localhost",
    user=DatabaseUser.Username,
    password=DatabaseUser.Password,
    database="flight_game"
)

Types = {
    "balloonport": ("Balloonport", 1),
    "heliport": ("Heliport", range(40,60)),
    "seaplane_base": ("Seaplane Base", 1),
    "small_airport": ("Regional Airport", range(50,150)),
    "medium_airport": ("National Ariport", range(100,500)),
    "large_airport": ("International Airport", range(2000,4000))
}

KnownAirports = {}

def New(Name):
    Cursor = Connection.cursor()
    Cursor.execute(f"SELECT type, iso_region, iso_country, continent FROM airport WHERE name = '{Name}'")
    CursorData = Cursor.fetchone()

    Type = Types[CursorData[0]]
    PriceRange = Type[1]
    Price = random.randint(PriceRange.start, PriceRange.stop) * 1000000

    KnownAirports[Name] = {
        "Name": Name,
        "Price": Price,
        "Region": CursorData[1],
        "Country": CursorData[2],
        "Continent": World.Continents[CursorData[3]]
    }

    print("New created!")

    return KnownAirports[Name]

def Get(Name):
    if Name in KnownAirports:
        return KnownAirports[Name]
    else:
        return New(Name)
