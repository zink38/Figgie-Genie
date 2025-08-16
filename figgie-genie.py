import sys

def validate_player_input(args):
    valid_colors = {'R', 'B', 'G', 'Y', 'E'}
    
    if len(args) < 4:
        return False, "Error: Need at least 4 players", valid_colors
    
    if len(args) > 5:
        return False, "Error: Too many players", valid_colors

    # Validate the color input.

    try:
        colors = [color.upper() for color in args]
    except ValueError:
        return False, "Error: must be letters consisting of R B G Y E", valid_colors

    if len(colors) != len(set(colors)):
        return False, "Error: The list contains duplicates", valid_colors

    
    for color in colors:  
        if color not in valid_colors:
            return False, f"Error: The list contains an invalid character: '{color}'. Allowed characters are {valid_colors}.", valid_colors

    valid_colors = colors
    return True, "Input successfully validated.", valid_colors 

def validate_input(args, valid_colors):

    # We expect a color and four integers, so a total of 5 arguments.
    if len(args) != 5:
        return False, "Error: Incorrect number of arguments. Expected: <color> <int1> <int2> <int3> <int4>"

    color = args[0].upper() # Cast the color input to upper case here
    nums = args[1:]

    # Validate the color input.
    if color not in valid_colors:
        return False, f"Error: Invalid color '{color}'. Color must be one of {valid_colors}"

    # Validate the four integer inputs.
    try:
        nums = [int(num) for num in nums]
    except ValueError:
        return False, "Error: All four numbers must be integers."
    
    # Check if the sum of the numbers is exactly 10.
    if sum(nums) != 40/len(valid_colors):
        return False, f"Error: The sum of the numbers must be exactly {40/len(valid_colors)}. Current sum is {sum(nums)}."

    return True, "Input successfully validated."


def validate_card_input(args, valid_colors):
    """
    Validates the card input during the game.
    
    Args:
        args (list): A list of arguments from the user's input.

    Returns:
        tuple: A tuple containing a boolean (True for valid, False for invalid)
               and a message string.
    """
    valid_suits = ['S', 'C', 'D', 'H']

    color = args[0].upper() # Cast color to uppercase
    suit = args[1].upper() # Cast suit to upper
    # Input can be 'color suit color' (3 arguments) or 'color suit' (2 arguments).
    if len(args) == 3:

        color2 = args[2].upper() # Cast color to uppercase
        
        # Check if colors are valid
        if color not in valid_colors or color2 not in valid_colors:
            return False, f'Error: Invalid color(s). Colors must be {valid_colors}',0
        # Check if the suit is valid
        if suit not in valid_suits:
            return False, "Error: Invalid suit. Suit must be S, C, D, or H.",0
        # The two colors cannot be the same
        if color == color2:
            return False, "Error: The two colors cannot be the same.",0
        return True, "Valid 'color suit color' input.",0

    elif len(args) == 2:
        
        # Check if color and suit are valid
        if color not in valid_colors or suit not in valid_suits:
            return False, f'Error: Invalid color or suit. Color must be {valid_colors}, and Suit must be S, C, D, or H.',1
        return True, "Valid 'color suit' input.",1

    else:
        return False, "Error: Invalid input total arguments.",-1

def main():
    """
    Main function to run the interactive Figgie CLI tool.
    """
    print("Welcome to the Figgie Card Counter!")
    
    # This loop handles the entire application lifecycle, allowing for new games.
    while True:
        # Prompt for initial game setup.
        print("\nEnter at least 4 player colors (R G B Y E) or type 'exit' to quit.")
        user_input = input("> ").strip()
        
        if user_input.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break
        
        input_args = user_input.split()
        
        # Validate the initial input.
        is_valid, player_message, valid_colors = validate_player_input(input_args)
        game_state = {}
        game_state_change = {}
        game_state_offer = {}
        
        for color in valid_colors:
            # Initialize each color with a dictionary of suit counts.
            suits = ['S','C','D','H']
            game_state[color] = {suit: 0 for suit in suits}
            game_state_change[color] = {suit: 0 for suit in suits}
            game_state_offer[color] = {suit: False for suit in suits}

            
        if is_valid:
            while True:
                # Prompt for initial game setup.
                print("\nEnter your initial cards (e.g., R 5 5 0 0) or type 'exit' to quit.")
                user_input = input("> ").strip()
                
                if user_input.lower() == 'exit':
                    print("Exiting the program. Goodbye!")
                    break
                
                input_args = user_input.split()
                
                # Validate the initial input.
                is_valid, message = validate_input(input_args, valid_colors)
            
                if is_valid:
                    print(message)
                    # You would store the initial counts here.
                    initial_color = input_args[0].upper() # Store the uppercase version
                    initial_counts = [int(num) for num in input_args[1:]]
                    game_state[initial_color]['S'] = initial_counts[0]
                    game_state[initial_color]['C'] = initial_counts[1]
                    game_state[initial_color]['D'] = initial_counts[2]
                    game_state[initial_color]['H'] = initial_counts[3]
                    print(f"Game started with Color: {initial_color}, Initial Counts: {initial_counts}")
                    
                    
                    # This inner loop handles the ongoing game.
                    while True:
                        print("known card\n")
                        print(game_state)
                        print("\n")
                        print("Changes \n")
                        print(game_state_change)
                        print("\n")
                        print("\nEnter traded card (color suit color) or offer (color suit), 'new' to start over, or 'exit' to quit.")
                        card_input = input("Card Played > ").strip()
                        
                        if card_input.lower() == 'new':
                            # Break the inner loop to start a new game.
                            break
                        
                        if card_input.lower() == 'exit':
                            print("Exiting the program. Goodbye!")
                            sys.exit(0)
                        
                        card_args = card_input.upper().split()
                        
                        is_valid_card, card_message, type = validate_card_input(card_args, valid_colors)
                        
                        if is_valid_card:
                            print(f"Card input received: {card_input}")
                                     
                            if type == 0:
                                if sum(game_state[card_args[2]].values()) < (40/len(valid_colors)) and game_state_change[card_args[2]][card_args[1]] < 1:
                                    if game_state_offer[card_args[2]][card_args[1]]:
                                        game_state_offer[card_args[2]][card_args[1]] = False
                                    else:
                                        game_state[card_args[2]][card_args[1]] += 1
                                game_state_change[card_args[2]][card_args[1]] -= 1
                                game_state_change[card_args[0]][card_args[1]] += 1
                            elif type == 1:
                                if not game_state_offer[card_args[0]][card_args[1]]:
                                    game_state_offer[card_args[0]][card_args[1]] = True
                                    game_state[card_args[0]][card_args[1]] += 1
                        else:
                            print(card_message)
                else:
                    print(message)
        else:
            print(player_message)


if __name__ == "__main__":
    main()

