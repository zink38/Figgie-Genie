import sys

def validate_input(args):
    """
    Validates the command-line arguments for the initial Figgie input.

    Args:
        args (list): A list of command-line arguments.

    Returns:
        tuple: A tuple containing a boolean (True for valid, False for invalid)
               and a message string.
    """
    # We expect a color and four integers, so a total of 5 arguments.
    if len(args) != 5:
        return False, "Error: Incorrect number of arguments. Expected: <color> <int1> <int2> <int3> <int4>"

    color = args[0]
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


def main():
    """
    Main function to run the interactive Figgie CLI tool.
    """
    print("Welcome to the Figgie Card Counter!")
    print("Enter your initial cards (e.g., R 5 5 0 0) or type 'exit' to quit.")

    while True:
        user_input = input("> ").strip()

        if user_input.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break
        
        # Split the input string into a list of arguments.
        input_args = user_input.split()
        
        # Perform validation on the provided input.
        is_valid, message = validate_input(input_args)
        
        # Print the result of the validation.
        if is_valid:
            print(message)
            print(f"Color: {input_args[0]}, Numbers: {input_args[1:]}")
            # You would place the card counting logic here.
        else:
            print(message)


if __name__ == "__main__":
    main()

R