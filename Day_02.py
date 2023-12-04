import re

# Contents of bag
# 12 red cubes, 13 green cubes, and 14 blue cubes

def parse_color_quantity_pairs(color_quantity_pairs):
    color_quantity_dict = {}
    for pair in color_quantity_pairs:
        parts = re.split(r'(\d+)', pair.strip())
        parts = [part for part in parts if part]

        if len(parts) == 2:
            quantity, color = parts
            color_quantity_dict[color] = int(quantity)
        elif len(parts) == 1:
            color = parts[0]
            color_quantity_dict[color] = 1
        else:
            raise ValueError(f"Invalid color_quantity_pair: {pair}")

    return color_quantity_dict

def check_possible_combination(game_info, target_string):
    target_pairs = parse_color_quantity_pairs(re.findall(r'(\d*\s*\w+)', target_string))
    cumulative_counts = {}

    for turn in game_info:
        turn_dict = parse_color_quantity_pairs(re.findall(r'(\d*\s*\w+)', turn))

        for color, quantity in turn_dict.items():
            cumulative_counts[color] = cumulative_counts.get(color, 0) + quantity

    for target_color, target_quantity in target_pairs.items():
        if cumulative_counts.get(target_color, 0) != target_quantity:
            return False

    return True

# Read the content of the file
file_path = 'Day_02.txt'

# Initialize an empty list to store the game data
games = []

with open(file_path, 'r') as file:
    # Process each line separately
    for line in file:
        # Split the line based on semicolons to separate games
        game_data = line.strip().split(';')

        # Process each game's data
        game_info = []
        for game in game_data:
            # Split each game's data based on commas to separate items
            items = game.split(',')
            
            # Extract color and quantity information
            color_quantity_pairs = [item.strip().split() for item in items]
            game_info.append(color_quantity_pairs)

        # Append the game information to the list of games
        games.append(game_info)

# Print the resulting list of games
for i, game in enumerate(games, start=1):
    print(f"Game {i}:")
    for turn in game:
        print(f"  {turn}")


# Specify the target string
target_string = "12 red cubes, 13 green cubes, and 14 blue cubes"

# Check each game against the target string
for i, game in enumerate(games, start=1):
    result = check_possible_combination(game, target_string)
    print(f"Game {i}: {'Possible' if result else 'Not possible'}")
