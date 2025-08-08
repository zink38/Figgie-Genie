import csv
import itertools

# Define the canonical deck composition and hand size.
deck_composition_tuple = (12, 10, 10, 8)
hand_size = 10

# Generate all unique permutations of the deck composition.
# The set() call handles duplicate permutations (e.g., (10, 10) in the tuple).
unique_deck_compositions = set(itertools.permutations(deck_composition_tuple))

# A list to hold the final, combined set of all valid distributions.
all_valid_distributions = []

# Iterate through each unique deck composition.
for current_deck_composition in unique_deck_compositions:
    # Use nested loops to generate all possible combinations of suit counts.
    for s1 in range(hand_size + 1):
        for s2 in range(hand_size + 1):
            for s3 in range(hand_size + 1):
                s4 = hand_size - s1 - s2 - s3

                # Check if the generated distribution is valid.
                if (s4 >= 0 and
                    s1 <= current_deck_composition[0] and
                    s2 <= current_deck_composition[1] and
                    s3 <= current_deck_composition[2] and
                    s4 <= current_deck_composition[3]):
                    
                    # If the distribution is valid, add it to our list.
                    # We also save the deck composition for reference.
                    all_valid_distributions.append([
                        current_deck_composition,
                        s1, s2, s3, s4
                    ])

# Define the name of the output CSV file.
output_file = 'complete_suit_distributions.csv'

# Write the data to the CSV file.
try:
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        
        # Write the header row.
        writer.writerow([
            'Deck Composition (Suit1, Suit2, Suit3, Suit4)',
            'Hand Suit 1', 'Hand Suit 2', 'Hand Suit 3', 'Hand Suit 4'
        ])
        
        # Write all the combined valid distributions.
        for row in all_valid_distributions:
            writer.writerow([str(row[0]), row[1], row[2], row[3], row[4]])
    
    print(f"Successfully created '{output_file}' with {len(all_valid_distributions)} total distributions.")

except IOError as e:
    print(f"An error occurred while writing the file: {e}")

