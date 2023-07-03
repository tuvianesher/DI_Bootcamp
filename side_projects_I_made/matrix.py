import os
import numpy as np
import pandas as pd

def parse_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def parse_lines(lines):
    distribution = {}
    for line in lines:
        line = line.strip().split(', ')
        for i in range(len(line) - 1):
            term1 = line[i].split(':')[0].strip()
            for j in range(i + 1, len(line)):
                term2 = line[j].split(':')[0].strip()
                if term1 != term2:
                    if term1 in distribution:
                        if term2 in distribution[term1]:
                            distribution[term1][term2] += 1
                        else:
                            distribution[term1][term2] = 1
                    else:
                        distribution[term1] = {term2: 1}
                    if term2 in distribution:
                        if term1 in distribution[term2]:
                            distribution[term2][term1] += 1
                        else:
                            distribution[term2][term1] = 1
                    else:
                        distribution[term2] = {term1: 1}
    return distribution

# Folder path for text files
folder_path = 'prompts'

# Get the list of text files in the folder
file_paths = [
    os.path.join(folder_path, file_name)
    for file_name in os.listdir(folder_path)
    if file_name.endswith('.txt')
]

# Read and parse the text files
distributions = []
for file_path in file_paths:
    lines = parse_file(file_path)
    distribution = parse_lines(lines)
    distributions.append(distribution)

# Merge the distributions
merged_distribution = {}
for distribution in distributions:
    for term1, terms in distribution.items():
        if term1 in merged_distribution:
            for term2, count in terms.items():
                if term2 in merged_distribution[term1]:
                    merged_distribution[term1][term2] += count
                else:
                    merged_distribution[term1][term2] = count
        else:
            merged_distribution[term1] = terms

# Create the co-occurrence matrix
terms = list(merged_distribution.keys())
num_terms = len(terms)
co_occurrence_matrix = np.zeros((num_terms, num_terms))

for i, term1 in enumerate(terms):
    for j, term2 in enumerate(terms):
        if term2 in merged_distribution[term1]:
            co_occurrence_matrix[i, j] = merged_distribution[term1][term2]

# Normalize the matrix row-wise to ensure row probabilities sum up to 1
row_sums = co_occurrence_matrix.sum(axis=1, keepdims=True)
co_occurrence_matrix /= row_sums

# Create a pandas DataFrame from the co-occurrence matrix
df = pd.DataFrame(co_occurrence_matrix, index=terms, columns=terms)

# Save the DataFrame to an Excel spreadsheet
output_file_path = 'co_occurrence_matrix.xlsx'
df.to_excel(output_file_path)

print(f"Co-occurrence matrix has been saved to '{output_file_path}' as an Excel spreadsheet.")
