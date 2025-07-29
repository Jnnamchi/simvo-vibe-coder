# Initial zoo data
zoo = [
    {
        "enclosure": "Savannah",
        "weather": "sunny",
        "animals": [
            {"name": "Leo", "species": "lion", "hunger": 7, "mood": "neutral"},
            {"name": "Zara", "species": "zebra", "hunger": 3, "mood": "neutral"}
        ]
    },
    {
        "enclosure": "Jungle",
        "weather": "rainy",
        "animals": [
            {"name": "Momo", "species": "monkey", "hunger": 6, "mood": "neutral"},
            {"name": "Tiki", "species": "toucan", "hunger": 2, "mood": "neutral"}
        ]
    }
]

# Feeding routine and mood update
for area in zoo:
    print(f"\nChecking enclosure: {area['enclosure']} ({area['weather']})")

    for animal in area["animals"]:
        print(f"  - {animal['name']} the {animal['species']} is at hunger level {animal['hunger']}")

        if animal["hunger"] > 5:
            print(f"    Feeding {animal['name']}... 🍖")
            animal["hunger"] -= 4  # Feeding reduces hunger

        # Mood depends on hunger and weather
        if animal["hunger"] <= 2:
            if area["weather"] == "sunny":
                animal["mood"] = "happy"
            else:
                animal["mood"] = "content"
        else:
            animal["mood"] = "grumpy"

        print(f"    Now {animal['name']} feels {animal['mood']} with hunger {animal['hunger']}")

# Final summary
print("\n--- End of Day Summary ---")
for area in zoo:
    for animal in area["animals"]:
        print(f"{animal['name']} the {animal['species']} is {animal['mood']} (Hunger: {animal['hunger']})")
