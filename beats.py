def load_player_words():
    """Load the player words and their costs from the JSON file."""
    # Define the words directly in the code to avoid JSON parsing issues
    return {
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
        "Time": 100
    }

def find_counter(system_word, player_words):
    """Find the best counter to the system word from the player's available words."""
    # Knowledge base of word relationships - which word beats which
    # This is where you would define all your counter relationships
    counters = {
        "wood": ["sandpaper", "oil", "acid", "drill", "fire"],
        "metal": ["sandpaper", "acid", "drill"],
        "plastic": ["sandpaper", "acid", "drill", "fire"],
        "paint": ["sandpaper", "acid", "fire"],
        "glass": ["sandpaper"],
        "cooking": ["oil", "acid", "vacation", "fire"],
        "food": ["oil", "acid", "fire"],
        "hair": ["oil", "acid", "gust", "fire"],
        "leather": ["oil", "acid", "fire"],
        "dirt": ["steam"],
        "wrinkles": ["steam"],
        "clothes": ["steam", "acid", "fire"],
        "bacteria": ["steam", "acid", "fire"],
        "ice": ["steam", "acid", "drill", "fire", "drought"],
        "rock": ["acid", "drill"],
        "stain": ["acid"],
        "smoke": ["gust"],
        "candle": ["acid", "gust", "fire"],
        "leaves": ["acid","gust", "fire", "drought"],
        "tree": ["boulder", "drill", "fire", "drought"],
        "human": ["acid", "boulder", "fire", "drought"],
        "wall": ["drill"],
        "stress": ["vacation"],
        "wallet": ["vacation"],
        "routine": ["vacation"],
        "mood": ["vacation"],
        "paper": ["fire"],
        "oxygen": ["fire"],
        "river": ["drought"],
        "grass": ["drought"],

        # Natural elements and phenomena
        "fire": ["water", "fire extinguisher", "fire blanket"],
        "water": ["dam", "freeze", "absorption", "drought"],
        "air": ["vacuum", "gust"],
        "earth": ["earthquake", "drill", "jackhammer"],
        "lightning": ["seismic dampener", "grounding", "kevlar vest"],
        "earthquake": ["seismic dampener", "evacuation"],
        "hurricane": ["cataclysm containment field", "evacuation", "planetary defense shield"],
        "tsunami": ["cataclysm containment field", "evacuation", "planetary defense shield"],
        "flood": ["dam", "evacuation", "absorption"],
        "drought": ["water", "rainstorm"],
        "avalanche": ["evacuation", "cataclysm containment field"],
        "lava": ["water", "evacuation", "freeze"],
        "glacier": ["fire", "heat", "lava", "sunshine"],
        "sunshine": ["cloud", "solar deflection array"],

        # Technology and weapons
        "robot": ["ai kill switch", "emp", "signal jammer", "water"],
        "laser": ["mirror", "kevlar vest", "planetary defense shield"],
        "signal": ["signal jammer", "noise"],
        "bomb": ["evacuation", "kevlar vest", "planetary defense shield"],
        "h-bomb": ["planetary evacuation fleet", "planetary defense shield"],
        "dynamite": ["water", "evacuation", "kevlar vest"],
        "explosion": ["kevlar vest", "planetary defense shield", "evacuation"],
        "satellite": ["signal jammer", "antimatter cannon", "orbital laser"],
        "virus": ["anti-virus nanocloud", "neutralizing agent"],
        "disease": ["anti-virus nanocloud", "neutralizing agent"],
        "nanobot swarm": ["emp", "neutralizing agent", "ai kill switch"],
        "orbital laser": ["planetary defense shield", "solar deflection array"],
        "antimatter cannon": ["planetary defense shield", "singularity stabilizer"],

        # Animals and nature
        "bear": ["bear trap", "dragon"],
        "grizzly": ["bear trap", "dragon"],
        "dragon": ["h-bomb", "antimatter cannon", "orbital laser"],

        # Abstract concepts
        "war": ["peace", "love", "propaganda"],
        "peace": ["war", "propaganda"],
        "propaganda": ["proof", "truth", "viral meme"],
        "fear": ["love", "confidence", "therapy"],
        "time": ["reality resynchronizer", "singularity stabilizer"],
        "innovation": ["persistence", "resilience"],
        "encryption": ["ai kill switch", "quantum computer"],
        "love": ["heartbreak", "reality"],
        "confidence": ["doubt", "proof"],
        "mutation": ["neutralizing agent", "anti-virus nanocloud"],
        "persistence": ["resilience", "time"],
        "resilience": ["time", "singularity stabilizer"],

        # Physical objects
        "boulder": ["jackhammer", "drill", "dynamite", "laser"],
        "steel": ["acid", "laser", "jackhammer"],
        "reinforced steel door": ["jackhammer", "hydraulic jack", "laser", "acid"],
        "bulldozer": ["bog", "emp", "ai kill switch"],
        "sandpaper": ["diamond", "oil"],
        "diamond cage": ["laser", "acid", "jackhammer"],
        "oil": ["fire", "absorption", "neutralizing agent"],
        "steam": ["freeze", "vacuum"],
        "acid": ["neutralizing agent", "water", "absorption"],
        "vacuum": ["air", "pressure", "leak"],

        # Destructive events
        "cataclysm": ["cataclysm containment field", "planetary evacuation fleet"],
        "apocalypse": ["planetary evacuation fleet", "singularity stabilizer"],
        "singularity": ["singularity stabilizer"],

        # Terraforming and planetary changes
        "terraforming": ["time", "persistence", "reality resynchronizer"],
        "reality": ["reality resynchronizer", "singularity stabilizer"],

        # Adding more common counters
        "heat": ["water", "ice", "freeze"],
        "cold": ["fire", "heat", "sunshine"],
        "pain": ["therapy", "love", "time"],
        "anger": ["love", "therapy", "time"],
        "depression": ["therapy", "love", "sunshine"],
        "chaos": ["order", "structure", "singularity stabilizer"],
        "order": ["chaos", "entropy", "time"],
        "death": ["life", "time", "resilience"],
        "life": ["death", "disease", "time"],
        "technology": ["emp", "time", "singularity"],
        "nature": ["terraforming device", "time"],
        "darkness": ["light", "sunshine"],
        "light": ["darkness", "vacuum"],
        "sound": ["vacuum", "signal jammer"],
        "silence": ["sound", "sonic boom"],
        "power": ["resistance", "resilience"],
        "weakness": ["strength", "confidence"],
        "hate": ["love", "therapy"],
        "hunger": ["food", "persistence"],
        "thirst": ["water", "persistence"],
        "knowledge": ["ignorance", "propaganda"],
        "ignorance": ["knowledge", "proof"],
        "space": ["time", "singularity stabilizer"],
        "solar": ["solar deflection array", "planetary defense shield"]
    }

    # Convert system word to lowercase for case-insensitive matching
    system_word_lower = system_word.lower()

    # Look for direct counter matches
    best_counter = None
    lowest_cost = float('inf')

    # Create a lowercase mapping of player words for case-insensitive matching
    player_words_lower = {word.lower(): (word, cost) for word, cost in player_words.items()}

    # Check if the system word has defined counters
    if system_word_lower in counters:
        for counter in counters[system_word_lower]:
            if counter in player_words_lower:
                original_word, cost = player_words_lower[counter]
                if cost < lowest_cost:
                    lowest_cost = cost
                    best_counter = original_word

    # If no direct counter found, try some general fallbacks
    # These are words that can counter many different threats
    if best_counter is None:
        best_counter, lowest_cost = find_similar_counter(system_word, player_words, counters)

    # Return tuple of counter and cost
    if best_counter:
        return best_counter, lowest_cost
    else:
        return "No counter found", -50  # Penalty for no counter

def find_similar_counter(system_word, player_words, counters):
    """
    Find a counter based on word similarity when no direct match exists
    in the knowledge base.
    """
    # We'll use a basic word similarity approach that includes:
    # 1. Character-level similarity (Levenshtein distance)
    # 2. Semantic field similarity (words in related categories)

    import difflib

    system_word_lower = system_word.lower()
    best_counter = None
    lowest_cost = float('inf')
    best_similarity = -1

    # 1. Try to find similar words in our knowledge base
    known_words = list(counters.keys())
    similarities = difflib.get_close_matches(system_word_lower, known_words, n=3, cutoff=0.6)

    # 2. If we found similar words, check their counters
    if similarities:
        potential_counters = set()
        for similar_word in similarities:
            potential_counters.update(counters[similar_word])

        # 3. Check if any potential counters are in player's words
        player_words_lower = {word.lower(): (word, cost) for word, cost in player_words.items()}
        for counter in potential_counters:
            if counter in player_words_lower:
                original_word, cost = player_words_lower[counter]
                if cost < lowest_cost:
                    lowest_cost = cost
                    best_counter = original_word

    # 4. If still no match, try word similarity directly with player's words
    if best_counter is None:
        # Semantic categories - group words by general concepts
        semantic_categories = {
            "protection": ["shield", "defense", "kevlar", "evacuation", "resilience"],
            "destruction": ["bomb", "explosion", "earthquake", "h-bomb", "dynamite"],
            "water": ["flood", "tsunami", "rainstorm", "dam"],
            "fire": ["lava", "heat", "fire"],
            "tech": ["robot", "laser", "satellite", "ai", "switch", "jammer"],
            "nature": ["glacier", "reforestation", "dragon", "bear"],
            "abstract": ["time", "love", "persistence", "innovation", "propaganda"]
        }

        # Find which semantic category the system word might belong to
        system_word_category = None
        for category, words in semantic_categories.items():
            if any(term in system_word_lower for term in words):
                system_word_category = category
                break

        # If we found a category, prioritize counters from opposite categories
        opposite_categories = {
            "protection": "destruction",
            "destruction": "protection",
            "water": "fire",
            "fire": "water",
            "tech": "nature",
            "nature": "tech",
            "abstract": "tech"
        }

        # Find all player words, sorted by cost
        player_items = sorted(player_words.items(), key=lambda x: x[1])

        # If we have a category, try to find words from opposing category first
        if system_word_category and system_word_category in opposite_categories:
            opposite = opposite_categories[system_word_category]
            for word, cost in player_items:
                word_lower = word.lower()
                # Check if this word belongs to the opposite category
                if any(term in word_lower for term in semantic_categories.get(opposite, [])):
                    return word, cost

        # Last resort: direct string similarity with player words
        player_word_list = [word.lower() for word in player_words.keys()]
        most_different = None
        max_difference = -1

        # Find the word most different from the system word (as a counter)
        for word in player_word_list:
            # Calculate normalized Levenshtein distance
            similarity = difflib.SequenceMatcher(None, system_word_lower, word).ratio()
            difference = 1 - similarity  # Convert similarity to difference

            if difference > max_difference:
                max_difference = difference
                most_different = word

        # Get the original word and cost
        if most_different:
            for original_word, cost in player_words.items():
                if original_word.lower() == most_different:
                    return original_word, cost

    # Return the best counter if found
    if best_counter:
        return best_counter, lowest_cost

    # If all else fails, return the cheapest word
    cheapest_word = min(player_words.items(), key=lambda x: x[1])
    return cheapest_word[0], cheapest_word[1]

def main():
    # Load player words
    player_words = load_player_words()

    while True:
        # Get system word from input
        system_word = input("Enter the system's word (or 'quit' to exit): ").strip()
        if system_word.lower() == 'quit':
            print("Thanks for playing!")
            break

        # Find counter
        counter, cost = find_counter(system_word, player_words)

        # Display result
        if counter == "No counter found":
            print(f"No counter found! Penalty: {cost}")
        else:
            print(f"Counter: {counter}, Cost: {cost}")

if __name__ == "__main__":
    main()