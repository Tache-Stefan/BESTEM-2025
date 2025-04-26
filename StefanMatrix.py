import json
from word_dict import all_categories

relationship_rules = {
    # Elements and their interactions
    "Fire": {"Water": -0.9, "Earth": 0.4, "Air": 0.7, "Combustible": 0.9},
    "Water": {"Fire": 0.9, "Earth": -0.3, "Air": 0.2, "Aquatic": 0.9, "Hydrodynamics": 0.8},
    "Air": {"Fire": 0.4, "Earth": 0.5, "Water": 0.3, "Atmospheric": 0.9},
    "Earth": {"Fire": -0.4, "Water": 0.5, "Air": -0.2, "Terrestrial": 0.9, "Geology": 0.8},

    # Weather related
    "Weather": {"Meteorology": 0.9, "Climatology": 0.8, "Natural Disaster": 0.7,
                "Technology": -0.5, "Construction": -0.6, "Protection": -0.4},
    "Meteorology": {"Weather": 0.9, "Climatology": 0.8, "Atmospheric": 0.7},
    "Climatology": {"Weather": 0.7, "Environment": 0.6, "Ecology": 0.5},

    # Disasters
    "Disaster": {"Survival": -0.8, "Protection": -0.7, "Construction": -0.9,
                 "Weather": 0.6, "Natural Disaster": 0.9, "Destruction": 0.8, "Escape": -0.8},
    "Natural Disaster": {"Disaster": 0.9, "Weather": 0.7, "Destruction": 0.8,
                         "Survival": -0.7, "Protection": -0.6, "Escape": -0.7},

    # Combat related
    "Attack": {"Defense": -0.9, "Combat": 0.9, "Warfare": 0.8, "Weapon": 0.9,
               "Force": 0.8, "Destruction": 0.7},
    "Defense": {"Attack": 0.9, "Protection": 0.9, "Barrier": 0.9, "Fortification": 0.9,
                "Shielding": 0.9, "Survival": 0.7, "Resilience": 0.6},
    "Combat": {"Warfare": 0.9, "Attack": 0.8, "Defense": 0.7, "Weapon": 0.8,
               "Strategy": 0.7, "Force": 0.8},
    "Warfare": {"Combat": 0.9, "Attack": 0.8, "Defense": 0.7, "Strategy": 0.8,
                "Destruction": 0.7, "Weapon": 0.9},

    # Protection related
    "Protection": {"Defense": 0.9, "Barrier": 0.8, "Shielding": 0.9, "Fortification": 0.8,
                   "Survival": 0.7, "Resilience": 0.7},
    "Barrier": {"Protection": 0.8, "Defense": 0.7, "Shielding": 0.8, "Obstacle": 0.9},
    "Fortification": {"Protection": 0.9, "Defense": 0.8, "Barrier": 0.7, "Construction": 0.8},
    "Shielding": {"Protection": 0.9, "Defense": 0.8, "Barrier": 0.7},

    # Weapons and destruction
    "Weapon": {"Attack": 0.9, "Warfare": 0.8, "Combat": 0.9, "Destruction": 0.8,
               "Force": 0.7, "Explosive": 0.8, "Ballistic": 0.9},
    "Explosive": {"Weapon": 0.8, "Destruction": 0.9, "Fire": 0.7, "Force": 0.8},
    "Ballistic": {"Weapon": 0.9, "Force": 0.8, "Kinetics": 0.7},
    "Destruction": {"Construction": -0.9, "Attack": 0.7, "Force": 0.8, "Demolition": 0.9,
                    "Disaster": 0.7, "Explosive": 0.8},
    "Demolition": {"Destruction": 0.9, "Construction": -0.9, "Force": 0.7},

    # Construction and architecture
    "Construction": {"Architecture": 0.9, "Urban Planning": 0.8, "Technology": 0.7,
                     "Destruction": -0.9, "Demolition": -0.8},
    "Architecture": {"Construction": 0.9, "Urban Planning": 0.8, "Art": 0.7},
    "Urban Planning": {"Architecture": 0.8, "Construction": 0.7, "Public Health": 0.6,
                       "Environment": 0.5},

    # Science and technology
    "Science": {"Technology": 0.9, "Research": 0.9, "Knowledge": 0.9,
                "Physics": 0.8, "Chemistry": 0.8, "Biology": 0.8},
    "Technology": {"Science": 0.8, "Electronics": 0.9, "Machine": 0.9, "Industry": 0.8,
                   "Artificial Intelligence": 0.7, "Nanotechnology": 0.7},
    "Electronics": {"Technology": 0.9, "Machine": 0.8, "Cybernetics": 0.7},
    "Machine": {"Technology": 0.9, "Electronics": 0.8, "Industry": 0.7},
    "Cybernetics": {"Technology": 0.8, "Electronics": 0.7, "Artificial Intelligence": 0.6},
    "Artificial Intelligence": {"Technology": 0.9, "Cybernetics": 0.8, "Mind": 0.7,
                                "Cognition": 0.6},
    "Nanotechnology": {"Technology": 0.9, "Science": 0.8, "Quantum Physics": 0.7},
    "Quantum Physics": {"Science": 0.9, "Physics": 0.9, "Energy": 0.8, "Space": 0.7},

    # Nature and environment
    "Nature": {"Environment": 0.9, "Plant": 0.9, "Animal": 0.9, "Ecology": 0.8,
               "Weather": 0.7, "Geology": 0.7},
    "Environment": {"Nature": 0.9, "Ecology": 0.8, "Pollution": -0.9, "Climate": 0.7},
    "Ecology": {"Environment": 0.9, "Nature": 0.8, "Plant": 0.7, "Animal": 0.7},
    "Plant": {"Nature": 0.9, "Botany": 0.9, "Ecology": 0.8, "Agriculture": 0.7},
    "Animal": {"Nature": 0.9, "Zoology": 0.9, "Ecology": 0.8, "Biological": 0.8},
    "Botany": {"Plant": 0.9, "Nature": 0.8, "Biological": 0.7},
    "Zoology": {"Animal": 0.9, "Nature": 0.8, "Biological": 0.7},
    "Pollution": {"Environment": -0.9, "Nature": -0.8, "Public Health": -0.7},

    # Physical sciences
    "Physical": {"Force": 0.8, "Energy": 0.8, "Movement": 0.7, "Kinetics": 0.7},
    "Force": {"Physical": 0.8, "Energy": 0.7, "Movement": 0.8, "Gravity": 0.9},
    "Energy": {"Physical": 0.8, "Force": 0.7, "Thermodynamics": 0.9, "Renewable Energy": 0.8},
    "Thermodynamics": {"Energy": 0.9, "Heat": 0.9, "Fire": 0.8},
    "Hydrodynamics": {"Water": 0.9, "Movement": 0.8, "Force": 0.7},
    "Gravity": {"Force": 0.9, "Space": 0.8, "Cosmology": 0.7},
    "Kinetics": {"Movement": 0.9, "Force": 0.8, "Physical": 0.7},
    "Movement": {"Kinetics": 0.8, "Physical": 0.7, "Travel": 0.7, "Escape": 0.6},

    # Space and cosmos
    "Space": {"Cosmology": 0.9, "Astrophysics": 0.9, "Time": 0.8, "Gravity": 0.8,
              "Space Travel": 0.7},
    "Cosmology": {"Space": 0.9, "Astrophysics": 0.8, "Time": 0.7},
    "Astrophysics": {"Space": 0.9, "Cosmology": 0.8, "Physics": 0.7},
    "Time": {"Space": 0.8, "Physics": 0.7, "Cosmology": 0.6},
    "Space Travel": {"Space": 0.9, "Technology": 0.8, "Travel": 0.7},

    # Psychology and mind
    "Psychological": {"Mind": 0.9, "Emotion": 0.9, "Cognition": 0.8, "Mental Process": 0.8,
                      "Psychology": 0.9},
    "Emotion": {"Psychological": 0.9, "Mind": 0.8, "Mental Process": 0.7},
    "Mind": {"Psychological": 0.9, "Cognition": 0.9, "Mental Process": 0.8,
             "Psychology": 0.8},
    "Cognition": {"Mind": 0.9, "Mental Process": 0.8, "Psychology": 0.7},
    "Mental Process": {"Mind": 0.9, "Cognition": 0.8, "Psychology": 0.7},
    "Psychology": {"Psychological": 0.9, "Mind": 0.8, "Sociology": 0.7},

    # Biological sciences
    "Biological": {"Animal": 0.8, "Plant": 0.8, "Genetics": 0.9, "Anatomy": 0.9,
                   "Mutation": 0.7},
    "Genetics": {"Biological": 0.9, "Mutation": 0.8, "Genetic Mutation": 0.9},
    "Anatomy": {"Biological": 0.9, "Physical": 0.7, "Surgery": 0.8},
    "Mutation": {"Genetics": 0.9, "Biological": 0.8, "Genetic Mutation": 0.9,
                 "Adaptation": 0.7},
    "Genetic Mutation": {"Mutation": 0.9, "Genetics": 0.9, "Adaptation": 0.7},

    # Survival and resilience
    "Survival": {"Resilience": 0.9, "Adaptation": 0.8, "Endurance": 0.8, "Escape": 0.7,
                 "Healing": 0.7},
    "Resilience": {"Survival": 0.8, "Endurance": 0.9, "Adaptation": 0.8, "Tenacity": 0.9},
    "Endurance": {"Resilience": 0.9, "Survival": 0.8, "Tenacity": 0.8},
    "Adaptation": {"Resilience": 0.8, "Survival": 0.7, "Evolution": 0.9, "Mutation": 0.7},
    "Tenacity": {"Resilience": 0.9, "Endurance": 0.8, "Persistence": 0.9},
    "Persistence": {"Tenacity": 0.9, "Resilience": 0.8, "Endurance": 0.7},
    "Escape": {"Movement": 0.9, "Survival": 0.8, "Evasion": 0.9},
    "Evasion": {"Escape": 0.9, "Movement": 0.8, "Strategy": 0.7},

    # Health and healing
    "Healing": {"First Aid": 0.9, "Surgery": 0.8, "Public Health": 0.7, "Biological": 0.7},
    "First Aid": {"Healing": 0.9, "Surgery": 0.7, "Survival": 0.8},
    "Surgery": {"Healing": 0.8, "First Aid": 0.7, "Anatomy": 0.9},
    "Public Health": {"Healing": 0.8, "Society": 0.7, "Urban Planning": 0.6},

    # Industry and resources
    "Industry": {"Technology": 0.8, "Machine": 0.8, "Mining": 0.7, "Agriculture": 0.6},
    "Agriculture": {"Plant": 0.9, "Industry": 0.7, "Food": 0.9, "Environment": 0.6},
    "Mining": {"Industry": 0.8, "Geology": 0.7, "Earth": 0.7},
    "Renewable Energy": {"Energy": 0.9, "Technology": 0.8, "Environment": 0.7},

    # Mythology and culture
    "Mythical": {"Folklore": 0.9, "Divinity": 0.8, "Human": 0.7},
    "Folklore": {"Mythical": 0.9, "Human": 0.7, "Anthropology": 0.8},
    "Divinity": {"Mythical": 0.9, "Folklore": 0.7, "Human": 0.6},
    "Anthropology": {"Human": 0.9, "Sociology": 0.8, "Folklore": 0.7},
    "Human": {"Anthropology": 0.8, "Sociology": 0.7, "Psychology": 0.7,
              "Biological": 0.7}
}


# Function to build the full confrontation matrix
def build_confrontation_matrix(categories, relationship_rules):
    # Initialize the matrix with zeros
    matrix = {cat: {other_cat: 0.0 for other_cat in categories} for cat in categories}

    # Fill in known relationships from rules
    for category, relationships in relationship_rules.items():
        if category in categories:
            for related_cat, value in relationships.items():
                if related_cat in categories:
                    matrix[category][related_cat] = value

                    # Make relationships reciprocal but inversed if not already defined
                    if related_cat in relationship_rules:
                        if category not in relationship_rules[related_cat]:
                            # Invert relationship (not perfect but gives a reasonable approximation)
                            # Positive relationships stay positive but weaker, negative flip to positive
                            if value > 0:
                                matrix[related_cat][category] = value * 0.8
                            else:
                                matrix[related_cat][category] = -value * 0.9

    # Add some logical strength/weakness relationships between parent categories
    for cat1 in categories:
        for cat2 in categories:
            # Skip if relationship already defined
            if matrix[cat1][cat2] != 0:
                continue

            # Element interactions (simplified)
            if cat1 in ["Fire", "Water", "Air", "Earth"] and cat2 in ["Fire", "Water", "Air", "Earth"]:
                if (cat1 == "Fire" and cat2 == "Water") or (cat1 == "Water" and cat2 == "Fire"):
                    matrix[cat1][cat2] = -0.8 if cat1 == "Fire" else 0.8
                elif (cat1 == "Air" and cat2 == "Earth") or (cat1 == "Earth" and cat2 == "Air"):
                    matrix[cat1][cat2] = 0.5 if cat1 == "Air" else -0.5

            # Attack/Defense relationships
            if cat1 in ["Attack", "Combat", "Warfare", "Weapon"] and cat2 in ["Defense", "Protection", "Barrier",
                                                                              "Fortification"]:
                matrix[cat1][cat2] = -0.7
            if cat2 in ["Attack", "Combat", "Warfare", "Weapon"] and cat1 in ["Defense", "Protection", "Barrier",
                                                                              "Fortification"]:
                matrix[cat1][cat2] = 0.7

            # Construction/Destruction
            if cat1 in ["Construction", "Architecture"] and cat2 in ["Destruction", "Demolition"]:
                matrix[cat1][cat2] = -0.8
            if cat2 in ["Construction", "Architecture"] and cat1 in ["Destruction", "Demolition"]:
                matrix[cat1][cat2] = -0.8

    return matrix


# Build the confrontation matrix
confrontation_matrix = build_confrontation_matrix(all_categories, relationship_rules)

# Convert to JSON format similar to your example
json_matrix = json.dumps(confrontation_matrix, indent=2)

# Print a sample of the matrix (first 5 categories and their first 5 relationships)
print("Sample of the confrontation matrix:")
for i, cat in enumerate(list(confrontation_matrix.keys())[:5]):
    print(f"{cat}:", end=" ")
    relations = list(confrontation_matrix[cat].items())[:5]
    for rel_cat, value in relations:
        if value != 0:
            print(f"{rel_cat}: {value:.1f}", end=", ")
    print("...")

# Save the matrix to a file
with open("full_confrontation_matrix.json", "w") as f:
    f.write(json_matrix)

print("\nFull matrix saved to 'full_confrontation_matrix.json'")
