DisasterDescription = {
    "Accident": "A random maintenance accident has happened!",
    "Tornado": "A tornado has caused havoc!",
    "Volcano": "Oh no! A volcano has erupted and has caused major destruction!",
    "Tsunami": "There has been a tsunami and water is overflowing!",
    "Earthquake": "An earthquake is shaking the ground!",
}

DisasterDamage = {
    "Accident": 1,
    "Tornado": 1,
    "Volcano": 4,
    "Tsunami": 2,
    "Earthquake": 3,
}

Continents = {
    "NA": ("North America", (("Accident", 0.5), ("Earthquake", 0.2),
                             ("Tornado", 0.3), ("Volcano", 0.07))),
    "EU": ("Europe", (("Accident", 0.5), ("Earthquake", 0.2), ("Tornado", 0.1))),
    "SA": ("South America", (("Accident", 0.5), ("Earthquake", 0.3),
                             ("Tsunami", 0.2), ("Tornado", 0.1), ("Volcano", 0.05))),
    "OC": ("Oceania", (("Accident", 0.5), ("Earthquake", 0.3),
                       ("Tsunami", 0.2), ("Volcano", 0.05))),
    "AS": ("Asia", (("Accident", 0.5), ("Earthquake", 0.3), ("Volcano", 0.05))),
    "AF": ("Africa", (("Accident", 0.5), ("Earthquake", 0.1),
                      ("Tornado", 0.1), ("Volcano", 0.07))),
    "AN": ("Antarctica", ("Accident", 0.6))

}