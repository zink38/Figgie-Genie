import csv

# Define the new canonical deck composition.
deck_composition = [12, 10, 10, 8]
hand_size = 10

# A list to hold all the valid suit distributions.
valid_distributions = []

# Use nested loops to generate all possible combinations of suit counts.
# The loops iterate from 0 to the hand size.
for s1 in range(hand_size + 1):
    for s2 in range(hand_size + 1):
        for s3 in range(hand_size + 1):
            s4 = hand_size - s1 - s2 - s3

            # Check if the generated distribution is valid.
            # 1. The sum must equal the hand size.
            # 2. Each suit count must be non-negative.
            # 3. Each suit count must not exceed the number of cards of that suit in the deck.
            if (s4 >= 0 and
                s1 <= deck_composition[0] and
                s2 <= deck_composition[1] and
                s3 <= deck_composition[2] and
                s4 <= deck_composition[3]):
                
                # If the distribution is valid, add it to our list.
                valid_distributions.append([s1, s2, s3, s4])

# Define the name of the output CSV file.
output_file = 'suit_distributions.csv'

# Write the data to the CSV file.
try:
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        
        # Write the header row.
        writer.writerow(['Suit 1 (12 cards)', 'Suit 2 (10 cards)', 'Suit 3 (10 cards)', 'Suit 4 (8 cards)'])
        
        # Write all the valid distributions.
        writer.writerows(valid_distributions)
    
    print(f"Successfully created '{output_file}' with {len(valid_distributions)} unique distributions.")

except IOError as e:
    print(f"An error occurred while writing the file: {e}")

