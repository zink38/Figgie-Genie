import sys

def validate_input(args):
    """
    Validates the initial Figgie input, which sets up the game.
    
    Args:
        args (list): A list of command-line arguments.

    Returns:
        tuple: A tuple containing a boolean (True for valid, False for invalid)
               and a message string.
    """
    # We expect a color and four integers, so a total of 5 arguments.
    if len(args) != 5:
        return False, "Error: Incorrect number of arguments. Expected: <color> <int1> <int2> <int3> <int4>"

    color = args[0].upper() # Cast the color input to upper case here
    nums = args[1:]

    # Validate the color input.
    valid_colors = ['R', 'G', 'B', 'Y']
    if color not in valid_colors:
        return False, f"Error: Invalid color '{color}'. Color must be one of {valid_colors}"

    # Validate the four integer inputs.
    try:
        nums = [int(num) for num in nums]
    except ValueError:
        return False, "Error: All four numbers must be integers."
    
    # Check if each number is within the valid range [0, 10].
    for num in nums:
        if not (0 <= num <= 10):
            return False, "Error: All numbers must be between 0 and 10 (inclusive)."

    # Check if the sum of the numbers is exactly 10.
    if sum(nums) != 10:
        return False, f"Error: The sum of the numbers must be exactly 10. Current sum is {sum(nums)}."

    return True, "Input successfully validated."


def validate_card_input(args):
    """
    Validates the card input during the game.
    
    Args:
        args (list): A list of arguments from the user's input.

    Returns:
        tuple: A tuple containing a boolean (True for valid, False for invalid)
               and a message string.
    """
    valid_colors = ['R', 'G', 'B', 'Y']
    valid_suits = ['S', 'C', 'D', 'H']

    # Input can be 'color suit color' (3 arguments) or 'color suit' (2 arguments).
    if len(args) == 3:
        color1 = args[0].upper() # Cast color to uppercase
        suit = args[1]
        color2 = args[2].upper() # Cast color to uppercase
        
        # Check if colors are valid
        if color1 not in valid_colors or color2 not in valid_colors:
            return False, "Error: Invalid color(s). Colors must be R, G, B, or Y."
        # Check if the suit is valid
        if suit not in valid_suits:
            return False, "Error: Invalid suit. Suit must be S, C, D, or H."
        # The two colors cannot be the same
        if color1 == color2:
            return False, "Error: The two colors cannot be the same."
        return True, "Valid 'color suit color' input."

    elif len(args) == 2:
        color = args[0].upper() # Cast color to uppercase
        suit = args[1]
        
        # Check if color and suit are valid
        if color not in valid_colors or suit not in valid_suits:
            return False, "Error: Invalid color or suit. Color must be R, G, B, or Y, and Suit must be S, C, D, or H."
        return True, "Valid 'color suit' input."

    else:
        return False, "Error: Invalid input format. Expected 'color suit color' or 'color suit'."

def main():
    """
    Main function to run the interactive Figgie CLI tool.
    """
    print("Welcome to the Figgie Card Counter!")
    
    # This loop handles the entire application lifecycle, allowing for new games.
    while True:
        # Prompt for initial game setup.
        print("\nEnter your initial cards (e.g., R 5 5 0 0) or type 'exit' to quit.")
        user_input = input("> ").strip()
        
        if user_input.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break
        
        input_args = user_input.split()
        
        # Validate the initial input.
        is_valid, message = validate_input(input_args)
        
        if is_valid:
            print(message)
            # You would store the initial counts here.
            initial_color = input_args[0].upper() # Store the uppercase version
            initial_counts = [int(num) for num in input_args[1:]]
            print(f"Game started with Color: {initial_color}, Initial Counts: {initial_counts}")
            
            # This inner loop handles the ongoing game.
            while True:
                print("\nEnter played cards (e.g., R S Y or Y H), 'new' to start over, or 'exit' to quit.")
                card_input = input("Card Played > ").strip()
                
                if card_input.lower() == 'new':
                    # Break the inner loop to start a new game.
                    break
                
                if card_input.lower() == 'exit':
                    print("Exiting the program. Goodbye!")
                    sys.exit(0)
                
                card_args = card_input.split()
                
                is_valid_card, card_message = validate_card_input(card_args)
                
                if is_valid_card:
                    print(f"Card input received: {card_input}")
                    # This is where you would update your card counts.
                    # For now, it just acknowledges the valid input.
                else:
                    print(card_message)
        else:
            print(message)


if __name__ == "__main__":
    main()

