import requests
from time import sleep
import re

# Definirea listei de cuvinte cu costurile și ID-urile lor
player_words = [
    {"id": 1, "word": "Sandpaper", "cost": 8},
    {"id": 2, "word": "Oil", "cost": 10},
    {"id": 3, "word": "Steam", "cost": 15},
    {"id": 4, "word": "Acid", "cost": 16},
    {"id": 5, "word": "Gust", "cost": 18},
    {"id": 6, "word": "Boulder", "cost": 20},
    {"id": 7, "word": "Drill", "cost": 20},
    {"id": 8, "word": "Vacation", "cost": 20},
    {"id": 9, "word": "Fire", "cost": 22},
    {"id": 10, "word": "Drought", "cost": 24},
    {"id": 11, "word": "Water", "cost": 25},
    {"id": 12, "word": "Vacuum", "cost": 27},
    {"id": 13, "word": "Laser", "cost": 28},
    {"id": 14, "word": "Life Raft", "cost": 30},
    {"id": 15, "word": "Bear Trap", "cost": 32},
    {"id": 16, "word": "Hydraulic Jack", "cost": 33},
    {"id": 17, "word": "Diamond Cage", "cost": 35},
    {"id": 18, "word": "Dam", "cost": 35},
    {"id": 19, "word": "Sunshine", "cost": 35},
    {"id": 20, "word": "Mutation", "cost": 35},
    {"id": 21, "word": "Kevlar Vest", "cost": 38},
    {"id": 22, "word": "Jackhammer", "cost": 38},
    {"id": 23, "word": "Signal Jammer", "cost": 40},
    {"id": 24, "word": "Grizzly", "cost": 41},
    {"id": 25, "word": "Reinforced Steel Door", "cost": 42},
    {"id": 26, "word": "Bulldozer", "cost": 42},
    {"id": 27, "word": "Sonic Boom", "cost": 45},
    {"id": 28, "word": "Robot", "cost": 45},
    {"id": 29, "word": "Glacier", "cost": 45},
    {"id": 30, "word": "Love", "cost": 45},
    {"id": 31, "word": "Fire Blanket", "cost": 48},
    {"id": 32, "word": "Super Glue", "cost": 48},
    {"id": 33, "word": "Therapy", "cost": 48},
    {"id": 34, "word": "Disease", "cost": 50},
    {"id": 35, "word": "Fire Extinguisher", "cost": 50},
    {"id": 36, "word": "Satellite", "cost": 50},
    {"id": 37, "word": "Confidence", "cost": 50},
    {"id": 38, "word": "Absorption", "cost": 52},
    {"id": 39, "word": "Neutralizing Agent", "cost": 55},
    {"id": 40, "word": "Freeze", "cost": 55},
    {"id": 41, "word": "Encryption", "cost": 55},
    {"id": 42, "word": "Proof", "cost": 55},
    {"id": 43, "word": "Molotov Cocktail", "cost": 58},
    {"id": 44, "word": "Rainstorm", "cost": 58},
    {"id": 45, "word": "Viral Meme", "cost": 58},
    {"id": 46, "word": "War", "cost": 59},
    {"id": 47, "word": "Dynamite", "cost": 60},
    {"id": 48, "word": "Seismic Dampener", "cost": 60},
    {"id": 49, "word": "Propaganda", "cost": 60},
    {"id": 50, "word": "Explosion", "cost": 62},
    {"id": 51, "word": "Lightning", "cost": 65},
    {"id": 52, "word": "Evacuation", "cost": 65},
    {"id": 53, "word": "Flood", "cost": 67},
    {"id": 54, "word": "Lava", "cost": 68},
    {"id": 55, "word": "Reforestation", "cost": 70},
    {"id": 56, "word": "Avalanche", "cost": 72},
    {"id": 57, "word": "Earthquake", "cost": 74},
    {"id": 58, "word": "H-bomb", "cost": 75},
    {"id": 59, "word": "Dragon", "cost": 75},
    {"id": 60, "word": "Innovation", "cost": 75},
    {"id": 61, "word": "Hurricane", "cost": 76},
    {"id": 62, "word": "Tsunami", "cost": 78},
    {"id": 63, "word": "Persistence", "cost": 80},
    {"id": 64, "word": "Resilience", "cost": 85},
    {"id": 65, "word": "Terraforming Device", "cost": 89},
    {"id": 66, "word": "Anti-Virus Nanocloud", "cost": 90},
    {"id": 67, "word": "AI Kill Switch", "cost": 90},
    {"id": 68, "word": "Nanobot Swarm", "cost": 92},
    {"id": 69, "word": "Reality Resynchronizer", "cost": 92},
    {"id": 70, "word": "Cataclysm Containment Field", "cost": 92},
    {"id": 71, "word": "Solar Deflection Array", "cost": 93},
    {"id": 72, "word": "Planetary Evacuation Fleet", "cost": 94},
    {"id": 73, "word": "Antimatter Cannon", "cost": 95},
    {"id": 74, "word": "Planetary Defense Shield", "cost": 96},
    {"id": 75, "word": "Singularity Stabilizer", "cost": 97},
    {"id": 76, "word": "Orbital Laser", "cost": 98},
    {"id": 77, "word": "Time", "cost": 100}
]

# Dicționar pentru accesare rapidă după ID
words_by_id = {word["id"]: word for word in player_words}
words_by_name = {word["word"].lower(): word for word in player_words}

# Categorii pentru cuvinte
categories = {
    "nature": ["water", "fire", "boulder", "glacier", "steam", "oil", "drought", "gust", "sunshine",
               "lightning", "rainstorm", "lava", "flood", "earthquake", "avalanche", "hurricane", "tsunami"],
    "tools": ["sandpaper", "drill", "vacuum", "laser", "life raft", "bear trap", "hydraulic jack",
              "diamond cage", "dam", "kevlar vest", "jackhammer", "signal jammer", "reinforced steel door",
              "bulldozer", "fire blanket", "super glue", "fire extinguisher", "satellite", "seismic dampener"],
    "weapons": ["molotov cocktail", "dynamite", "explosion", "h-bomb", "dragon", "antimatter cannon", "orbital laser"],
    "concepts": ["vacation", "love", "therapy", "confidence", "innovation", "persistence", "resilience",
                 "time", "proof", "encryption", "propaganda", "war", "evacuation"],
    "biological": ["disease", "mutation", "grizzly", "viral meme", "reforestation", "anti-virus nanocloud", "nanobot swarm"],
    "tech": ["robot", "terraforming device", "ai kill switch", "reality resynchronizer",
             "cataclysm containment field", "solar deflection array", "planetary evacuation fleet",
             "planetary defense shield", "singularity stabilizer"]
}

# Baza de relații logice - ce învinge ce
counter_relations = {
    # Specific relations based on examples and logic
    "dam": ["flood", "water", "tsunami", "hurricane", "rainstorm", "river", "lake", "ocean", "sea", "wave"],
    "drought": ["water", "flood", "lake", "river", "ocean", "rain", "rainstorm", "plants", "crop", "farm", "agriculture"],
    "bear trap": ["bear", "grizzly", "animal", "wolf", "fox", "rabbit", "predator", "beast", "monster"],
    "fire extinguisher": ["fire", "molotov cocktail", "flame", "burning", "heat", "arson", "spark", "candle"],
    "fire blanket": ["fire", "flame", "burning", "spark", "heat", "candle"],
    "water": ["fire", "flame", "burning", "lava", "heat", "drought", "spark", "candle", "paper", "dust"],
    "fire": ["paper", "wood", "tree", "forest", "book", "candle", "ice", "cold", "freeze", "cloth", "cloth", "plastic"],
    "h-bomb": ["city", "country", "army", "tank", "missile", "fighter jet", "submarine", "military", "weapon",
               "building", "fortress", "bunker", "shelter", "vehicle", "aircraft", "ship", "any military vehicle or structure"],
    "robot": ["human", "manual labor", "repetitive task", "work", "factory", "production", "assembly"],
    "evacuation": ["disaster", "danger", "threat", "flood", "fire", "explosion", "earthquake", "emergency",
                   "catastrophe", "crisis", "pandemic", "any natural disaster"],
    "ai kill switch": ["ai", "robot", "algorithm", "system", "computer", "program", "software", "network",
                       "automation", "computer system"],
    "anti-virus nanocloud": ["virus", "infection", "disease", "malware", "computer virus", "hacker", "bacteria",
                             "pathogen", "contaminant", "flu", "pandemic"],
    "life raft": ["flood", "tsunami", "ocean", "sea", "river", "lake", "drowning", "shipwreck", "water disaster"],

    # Natural disasters and counters
    "seismic dampener": ["earthquake", "tremor", "vibration", "shaking", "shock", "seismic activity"],
    "planetary defense shield": ["asteroid", "meteor", "missile", "attack", "invasion", "comet", "space debris",
                                 "radiation", "solar flare", "cosmic ray", "alien attack"],
    "reality resynchronizer": ["glitch", "anomaly", "distortion", "paradox", "time loop", "alternative reality",
                               "matrix", "simulation", "illusion", "deception"],

    # Abstract concepts and their relations
    "love": ["hate", "war", "conflict", "anger", "fear", "sorrow", "loneliness", "despair", "aggression", "violence"],
    "resilience": ["challenge", "difficulty", "setback", "failure", "disaster", "pressure", "stress",
                   "crisis", "trauma", "any psychological or physical stress"],
    "persistence": ["obstacle", "barrier", "resistance", "opposition", "failure", "discouragement",
                    "rejection", "setback", "challenge", "defeat"],
    "innovation": ["obsolescence", "stagnation", "tradition", "outdated", "inefficiency", "old tech",
                   "conventional methods", "old-fashioned", "backward"],
    "time": ["rush", "deadline", "urgency", "impatience", "rock", "diamond", "mountain", "universe",
             "matter", "energy", "everything", "anything", "literally everything"],

    # Elements and their interactions
    "acid": ["metal", "rock", "stone", "iron", "steel", "bone", "shell", "limestone", "concrete", "marble",
             "any solid material that would dissolve in acid"],
    "boulder": ["window", "glass", "car", "human", "animal", "building", "structure", "fragile objects"],
    "laser": ["mirror", "metal", "rock", "diamond", "satellite", "target", "armor", "material", "tissue", "device"],
    "glacier": ["ship", "boat", "obstacle", "road", "pathway", "passage", "navigation", "transport"],
    "vacuum": ["dust", "air", "gas", "oxygen", "atmosphere", "particle", "debris", "pollution", "smoke"],

    # Technology counters
    "signal jammer": ["communication", "radio", "cell phone", "satellite", "gps", "wifi", "bluetooth",
                      "remote control", "wireless device", "drone", "any wireless technology"],
    "encryption": ["hacker", "spy", "surveillance", "monitoring", "data theft", "information leak",
                   "identity theft", "privacy invasion", "cyber attack"],
    "propaganda": ["truth", "fact", "information", "journalism", "skepticism", "critical thinking",
                   "free press", "unbiased reporting", "media literacy"],

    # High-cost counters for ultimate threats
    "orbital laser": ["building", "facility", "infrastructure", "vehicle", "target", "defense",
                      "installation", "equipment", "complex", "base"],
    "singularity stabilizer": ["black hole", "gravity well", "space-time distortion", "wormhole",
                               "quantum fluctuation", "singularity", "cosmic anomaly"],
    "planetary evacuation fleet": ["planetary disaster", "extinction event", "cataclysm", "global catastrophe",
                                   "planet killer", "world-ending threat", "apocalypse"],
    "cataclysm containment field": ["disaster", "catastrophe", "apocalypse", "extinction", "armageddon",
                                    "doomsday", "end of the world", "annihilation"],

    # Generic but useful relations
    "dynamite": ["rock", "mountain", "wall", "barrier", "boulder", "obstacle", "building", "structure",
                 "foundation", "dam", "bridge", "tunnel", "construction", "fortress"],
    "bulldozer": ["building", "structure", "obstacle", "wall", "tree", "vegetation", "rubble",
                  "barrier", "barricade", "fence", "small structure"],
    "kevlar vest": ["bullet", "projectile", "knife", "stab", "attack", "impact", "strike", "shot",
                    "physical attack", "ballistic threat"],
    "proof": ["accusation", "claim", "theory", "hypothesis", "assumption", "lie", "rumor", "falsehood",
              "misinformation", "disinformation", "conspiracy", "case", "argument"],
    "therapy": ["trauma", "depression", "anxiety", "mental health", "stress", "emotional pain",
                "psychological issue", "phobia", "grief", "distress", "any psychological condition"],
    "solar deflection array": ["heat", "solar flare", "radiation", "sunlight", "uv rays", "sun",
                               "solar radiation", "solar storm", "climate change", "global warming"],
    "neutralizing agent": ["acid", "toxin", "poison", "chemical", "contaminant", "pollutant",
                           "radiation", "harmful substance", "dangerous material"],
    "grizzly": ["human", "camper", "hiker", "fish", "salmon", "small animal", "prey", "threat"],
    "vacuum": ["air", "gas", "dust", "particle", "debris", "atmosphere", "oxygen"],
    "lightning": ["tree", "building", "structure", "electronics", "power grid", "outdoor activity"],
    "super glue": ["break", "crack", "fracture", "split", "separation", "broken object", "loose parts"],
    "jackhammer": ["concrete", "asphalt", "pavement", "stone", "rock", "foundation", "hard surface"],
    "freeze": ["liquid", "water", "flow", "movement", "action", "process", "system", "function"],
    "disease": ["population", "community", "crowd", "gathering", "health system"],
    "viral meme": ["reputation", "image", "popularity", "public opinion", "social media presence"],
    "sunshine": ["darkness", "gloom", "depression", "winter", "cold", "ice", "snow", "cloudy weather"],
    "reforestation": ["deforestation", "logging", "forest fire", "desertification", "soil erosion", "habitat loss"],
    "war": ["peace", "diplomacy", "stability", "cooperation", "negotiation"],
    "confidence": ["doubt", "uncertainty", "insecurity", "fear", "hesitation", "self-doubt"],
    "absorption": ["spill", "leak", "flood", "liquid", "outflow", "overflow", "emission"],
    "satellite": ["privacy", "secrecy", "hidden activity", "covert operation", "concealment"],

    # More specific counters
    "sandpaper": ["rough surface", "rust", "paint", "uneven edge", "splinter", "sharp edge"],
    "oil": ["friction", "rust", "squeak", "metal joints", "mechanical resistance", "stuck mechanism"],
    "steam": ["cold", "ice", "frozen", "chill", "rigid structure", "solid state", "wrinkle", "fold"],
    "gust": ["dust", "sand", "smoke", "fog", "light object", "paper", "leaf", "lightweight debris"],
    "drill": ["hard material", "wall", "rock", "metal", "obstacle", "barrier", "surface"],
    "vacation": ["stress", "burnout", "overwork", "exhaustion", "fatigue", "routine", "pressure"],
    "reinforced steel door": ["intruder", "break-in", "force entry", "thief", "attack", "invasion", "breach"],
    "sonic boom": ["glass", "fragile structure", "electronics", "concentration", "focus", "delicate object"],
    "mutation": ["poison", "toxin", "radiation", "genetic defect", "biological limitation", "disease"],
    "diamond cage": ["escape", "breakout", "evasion", "flight", "runaway", "getaway", "any escape attempt"],
    "hydraulic jack": ["weight", "heavy object", "pressure", "compression", "car", "vehicle", "load"],
}

# Categorii care învimng alte categorii
category_counters = {
    "weapons": ["nature", "biological", "tools"],
    "tech": ["nature", "weapons", "biological"],
    "concepts": ["tech", "weapons", "biological"],
    "nature": ["tools", "tech"],
    "biological": ["tools", "concepts"],
    "tools": ["nature", "biological"]
}

# Cuvinte cu putere mare (abstracte sau foarte puternice) care pot întotdeauna să fie ultimă opțiune
abstract_powerful_words = ["time", "innovation", "resilience", "persistence", "reality resynchronizer",
                           "singularity stabilizer", "planetary defense shield", "h-bomb", "orbital laser",
                           "antimatter cannon", "cataclysm containment field", "nanobot swarm", "terraforming device"]

# Funcție pentru a găsi categoria unui cuvânt
def find_category(word):
    word = word.lower()

    # Căutare exactă
    for category, words in categories.items():
        if word in words:
            return category

    # Căutare substring
    for category, words in categories.items():
        for category_word in words:
            if word in category_word or category_word in word:
                return category

    return None

# Funcție pentru a verifica dacă un cuvânt învinge direct alt cuvânt
def directly_counters(player_word, system_word):
    player_word = player_word.lower()
    system_word = system_word.lower()

    # Verificăm relații directe de contracarare
    if player_word in counter_relations:
        for pattern in counter_relations[player_word]:
            if pattern in system_word or system_word in pattern:
                return True

    # Verificăm și pentru cuvinte similare cu cuvântul jucătorului
    for counter, patterns in counter_relations.items():
        if counter in player_word or player_word in counter:
            for pattern in patterns:
                if pattern in system_word or system_word in pattern:
                    return True

    return False

# Funcția principală pentru a găsi cel mai bun cuvânt care contracarează cuvântul sistemului
def find_best_counter(system_word):
    system_word = system_word.lower()
    best_counters = []

    # 1. Verificăm contracarări directe
    for word in player_words:
        player_word = word["word"].lower()
        if directly_counters(player_word, system_word):
            best_counters.append(word)

    # 2. Dacă nu avem contracarări directe, verificăm pe baza categoriilor
    if not best_counters:
        system_category = find_category(system_word)
        if system_category:
            counter_categories = category_counters.get(system_category, [])
            for word in player_words:
                player_category = find_category(word["word"].lower())
                if player_category and player_category in counter_categories:
                    best_counters.append(word)

    # 3. Dacă tot nu avem nimic, încercăm cuvinte abstracte puternice
    if not best_counters:
        for word in player_words:
            if word["word"].lower() in abstract_powerful_words:
                best_counters.append(word)

    # 4. Dacă tot nu avem nimic, luăm cuvinte cu cost ridicat
    if not best_counters:
        for word in player_words:
            if word["cost"] >= 75:  # Alegem cuvinte puternice
                best_counters.append(word)

    # 5. Ultima soluție: cuvinte speciale pentru cazuri extreme
    if not best_counters:
        special_fallbacks = ["time", "resilience", "planetary defense shield", "singularity stabilizer"]
        for word in player_words:
            if word["word"].lower() in special_fallbacks:
                best_counters.append(word)

    # Dacă tot nu avem nimic, returnăm orice cuvânt (ce n-ar trebui să se întâmple, dar ca măsură de siguranță)
    if not best_counters:
        best_counters = player_words

    # Sortează pentru a găsi cel mai ieftin cuvânt care este eficient
    best_counters.sort(key=lambda x: x["cost"])

    return best_counters[0]

# Funcția principală de joc
def what_beats(system_word):
    counter = find_best_counter(system_word)
    return counter["id"]

# Funcția pentru jocul complet
def play_game(player_id, host):
    post_url = f"{host}/submit-word"
    get_url = f"{host}/get-word"
    status_url = f"{host}/status"

    print(f"Începem jocul cu ID-ul {player_id}")

    for round_id in range(1, 11):  # 10 runde
        round_num = -1
        # Așteptăm până când runda curentă este cea pe care o așteptăm
        while round_num != round_id:
            try:
                response = requests.get(get_url)
                data = response.json()
                sys_word = data['word']
                round_num = data['round']

                if round_num != round_id:
                    print(f"Așteptăm runda {round_id}, suntem la runda {round_num}...")
                    sleep(1)
            except Exception as e:
                print(f"Eroare la obținerea cuvântului: {e}")
                sleep(1)

        print(f"\nRunda {round_id}: Cuvântul sistemului este '{sys_word}'")

        # Obținem statusul rundei anterioare (după runda 1)
        if round_id > 1:
            try:
                status = requests.post(status_url, json={"player_id": player_id})
                status_data = status.json()
                print(f"Status runda anterioară: {status_data}")
            except Exception as e:
                print(f"Eroare la obținerea statusului: {e}")

        # Alegem cuvântul nostru
        chosen_word_id = what_beats(sys_word)
        chosen_word = words_by_id[chosen_word_id]["word"]
        chosen_cost = words_by_id[chosen_word_id]["cost"]

        print(f"Alegem cuvântul: '{chosen_word}' (ID: {chosen_word_id}, Cost: ${chosen_cost})")

        # Trimitem răspunsul
        try:
            data = {"player_id": player_id, "word_id": chosen_word_id, "round_id": round_id}
            response = requests.post(post_url, json=data)
            print(f"Răspuns server: {response.json()}")
        except Exception as e:
            print(f"Eroare la trimiterea cuvântului: {e}")

    print("\nJoc terminat!")

    # Obținem status final
    try:
        status = requests.post(status_url, json={"player_id": player_id})
        status_data = status.json()
        print(f"Status final: {status_data}")
    except Exception as e:
        print(f"Eroare la obținerea statusului final: {e}")

# Funcție pentru înregistrarea jucătorului
def register(player_id, host):
    register_url = f"{host}/register"
    data = {"player_id": player_id}

    try:
        response = requests.post(register_url, json=data)
        print(f"Înregistrare: {response.json()}")
        return response.json()
    except Exception as e:
        print(f"Eroare la înregistrare: {e}")
        return None

# Funcția main - exemplu de utilizare
if __name__ == "__main__":
    # Setează adresa serverului și ID-ul jucătorului
    HOST = ""  # Înlocuiește cu adresa reală a serverului
    PLAYER_ID = ""  # Înlocuiește cu ID-ul tău dorit

    # Înregistrează jucătorul
    # register(PLAYER_ID, HOST)

    # Pornește jocul
    # play_game(PLAYER_ID, HOST)

    # Pentru a testa local, poți rula următoarele:
    test_examples = [
        "Helicopter",
        "Candle", "Hammer", "Blueberries", "Flood", "Tank",
        "Rock", "Fighter Jet", "Peace", "War", "Bear",
        "Computer", "Virus", "Tree", "Fortress", "Army",
        "Climate Change", "Pandemic", "Robot Army", "Hacker",
        "Planetary Drought", "Solar Flare", "Meteor", "Alien Invasion",

        "Warzone", "Drum", "Fur", "Rain", "Flame Thrower",
        "Squirrel", "Snowflake", "Helicopter", "Spider", "Puddle",
        "Matches", "Power Line", "Firewood", "Demolition Site",
        "Collapse of Civilization", "Acorn", "Plastic Bag", "Ice Cube",
        "Bee", "Shovel", "Leaf Blower", "Nest", "Tornado Siren",
        "Riot Shield", "Button", "Supervolcano", "Matchstick", "Smoke",
        "Scissors", "Windmill", "Mud", "Bucket", "Heavy Machinery",
        "Toothpick", "Crayon", "Snake", "Mirror", "Ant", "Helmet",
        "Stick", "Axe", "Balloon", "Watchtower", "Evil SuperIntelligent AI",
        "Lantern"
    ]


    print("\n===== TEST LOCAL =====")
    for example in test_examples:
        counter = find_best_counter(example)
        print(f"Sistemul dă: '{example}' -> Cel mai bun răspuns: '{counter['word']}' (Cost: ${counter['cost']}, ID: {counter['id']})")