# word_costs.json content:
word_costs = {
    "Sandpaper": 8,
    "Oil": 10,
    "Steam": 15,
    "Acid": 16,
    "Gust": 18,
    "Boulder": 20,
    "Drill": 20,
    "Vacation": 20,
    "Fire": 22,
    "Drought": 24,
    "Water": 25,
    "Vacuum": 27,
    "Laser": 28,
    "Life Raft": 30,
    "Bear Trap": 32,
    "Hydraulic Jack": 33,
    "Diamond Cage": 35,
    "Dam": 35,
    "Sunshine": 35,
    "Mutation": 35,
    "Kevlar Vest": 38,
    "Jackhammer": 38,
    "Signal Jammer": 40,
    "Grizzly": 41,
    "Reinforced Steel Door": 42,
    "Bulldozer": 42,
    "Sonic Boom": 45,
    "Robot": 45,
    "Glacier": 45,
    "Love": 45,
    "Fire Blanket": 48,
    "Super Glue": 48,
    "Therapy": 48,
    "Disease": 50,
    "Fire Extinguisher": 50,
    "Satellite": 50,
    "Confidence": 50,
    "Absorption": 52,
    "Neutralizing Agent": 55,
    "Freeze": 55,
    "Encryption": 55,
    "Proof": 55,
    "Molotov Cocktail": 58,
    "Rainstorm": 58,
    "Viral Meme": 58,
    "War": 59,
    "Dynamite": 60,
    "Seismic Dampener": 60,
    "Propaganda": 60,
    "Explosion": 62,
    "Lightning": 65,
    "Evacuation": 65,
    "Flood": 67,
    "Lava": 68,
    "Reforestation": 70,
    "Avalanche": 72,
    "Earthquake": 74,
    "H-bomb": 75,
    "Dragon": 75,
    "Innovation": 75,
    "Hurricane": 76,
    "Tsunami": 78,
    "Persistence": 80,
    "Resilience": 85,
    "Terraforming Device": 89,
    "Anti-Virus Nanocloud": 90,
    "AI Kill Switch": 90,
    "Nanobot Swarm": 92,
    "Reality Resynchronizer": 92,
    "Cataclysm Containment Field": 92,
    "Solar Deflection Array": 93,
    "Planetary Evacuation Fleet": 94,
    "Antimatter Cannon": 95,
    "Planetary Defense Shield": 96,
    "Singularity Stabilizer": 97,
    "Orbital Laser": 98,
    "Time": 100,
}

# mini knowledge base
beats = {
    "fire": ["Water", "Fire Extinguisher", "Fire Blanket"],
    "lion": ["Grizzly", "Bear Trap"],
    "gun": ["Kevlar Vest", "Reinforced Steel Door"],
    "flood": ["Dam"],
    "lava": ["Freeze"],
    "war": ["Peace", "Love", "Propaganda"],
    "earthquake": ["Seismic Dampener"],
    "tsunami": ["Terraforming Device"],
    "disease": ["Anti-Virus Nanocloud", "Therapy"],
    "explosion": ["Cataclysm Containment Field", "Seismic Dampener"],
    "hurricane": ["Solar Deflection Array"],
    "dragon": ["Robot", "Laser", "Orbital Laser"],
    "drought": ["Rainstorm"],
    "vacuum": ["Reality Resynchronizer"],
    "mutation": ["Neutralizing Agent"],
    "viral meme": ["Viral Meme", "Signal Jammer"],
    "fire blanket": ["Fire"],
}

def choose_word(system_word):
    system_word = system_word.lower()

    candidates = beats.get(system_word, [])
    available = []

    for word in candidates:
        if word in word_costs:
            available.append((word, word_costs[word]))

    if not available:
        print("No direct counter, picking cheapest general option...")
        # pick the lowest cost word overall (as backup strategy)
        cheapest_word = min(word_costs.items(), key=lambda x: x[1])
        return cheapest_word[0]

    # pick cheapest winning word
    cheapest_counter = min(available, key=lambda x: x[1])
    return cheapest_counter[0]


# ============ USAGE EXAMPLE ==============
while True:
    system_word = input("\nSystem word? (or 'q' to quit) ")
    if system_word.lower() == 'q':
        break
    choice = choose_word(system_word)
    print(f"AI chooses: {choice}")
