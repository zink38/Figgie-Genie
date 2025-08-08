import csv
import itertools

# List of the 23 unique integer partitions of 10 into 4 parts.
# These represent the canonical suit distributions for a 10-card hand.
canonical_distributions = [
    (10, 0, 0, 0),
    (9, 1, 0, 0),
    (8, 2, 0, 0),
    (8, 1, 1, 0),
    (7, 3, 0, 0),
    (7, 2, 1, 0),
    (7, 1, 1, 1),
    (6, 4, 0, 0),
    (6, 3, 1, 0),
    (6, 2, 2, 0),
    (6, 2, 1, 1),
    (5, 5, 0, 0),
    (5, 4, 1, 0),
    (5, 3, 2, 0),
    (5, 3, 1, 1),
    (5, 2, 2, 1),
    (4, 4, 2, 0),
    (4, 4, 1, 1),
    (4, 3, 3, 0),
    (4, 3, 2, 1),
    (4, 2, 2, 2),
    (3, 3, 3, 1),
    (3, 3, 2, 2)
]

# A list to hold the final, expanded set of all unique distributions.
expanded_distributions = []

# Iterate through each canonical distribution.
for distribution in canonical_distributions:
    # Use itertools.permutations to get all possible orderings of the tuple.
    # The set() call automatically handles duplicates (e.g., for (9,1,0,0),
    # it correctly handles that (9,1,0,0), (9,0,1,0) etc. are unique, but it won't
    # repeat them).
    unique_permutations = set(itertools.permutations(distribution))

    # Add each unique permutation to our expanded list.
    for permutation in unique_permutations:
        expanded_distributions.append(list(permutation))

# Define the name of the output CSV file.
output_file = 'suit_distributions.csv'

# Write the data to the CSV file.
try:
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        
        # Write the header row.
        writer.writerow(['Suit 1', 'Suit 2', 'Suit 3', 'Suit 4'])
        
        # Write all the expanded distributions.
        writer.writerows(expanded_distributions)
    
    print(f"Successfully created '{output_file}' with {len(expanded_distributions)} unique distributions.")

except IOError as e:
    print(f"An error occurred while writing the file: {e}")

