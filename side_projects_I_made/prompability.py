import os
import numpy as np

def parse_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def parse_lines(lines):
    distribution = {}
    content = "".join(lines)
    pairs = content.split(", ")

    for pair in pairs:
        pair = pair.strip("()").split(":")
        if len(pair) == 2:
            term = pair[0].strip()
            probability = pair[1].strip()

            if term.startswith('(') and term.endswith(')'):
                term = term[1:-1]

            distribution[term] = float(probability)

    return distribution


def merge_distributions(distributions):
    merged_distribution = {}
    for distribution in distributions:
        for word, probability in distribution.items():
            if word in merged_distribution:
                merged_distribution[word].append(probability)
            else:
                merged_distribution[word] = [probability]
    return merged_distribution

def calculate_average_probability(distribution):
    average_probability = {}
    for word, probabilities in distribution.items():
        average_probability[word] = np.mean(probabilities)
    return average_probability

def calculate_average_deviation(distribution, average_probability):
    average_deviation = {}
    for word, probabilities in distribution.items():
        deviation = np.abs(probabilities - average_probability[word])
        average_deviation[word] = np.mean(deviation)
    return average_deviation

def calculate_occurrence_percentage(distribution, total_files):
    occurrence_percentage = {}
    for word, probabilities in distribution.items():
        occurrence_percentage[word] = len(probabilities) / total_files * 100
    return occurrence_percentage

def write_output(file_path, average_probability, average_deviation, occurrence_percentage, low_occurrence_terms):
    max_word_length = max(len(word) for word in average_probability.keys())

    with open(file_path, 'w') as file:
        file.write(f"{'Term':<{max_word_length}}\tAverage Probability\tAverage Deviation\tOccurrences\n")
        for word in average_probability.keys():
            probability = average_probability.get(word, 0.0)
            deviation = average_deviation.get(word, 0.0)
            occurrences = occurrence_percentage.get(word, 0.0)
            file.write(f"{word:<{max_word_length}}\t{probability:.15f}\t{deviation:.15f}\t{occurrences:.3f}\n")

        file.write("\nLow Occurrence Terms (less than 10%):\n")
        for term in low_occurrence_terms:
            file.write(f"{term}\n")


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
merged_distribution = merge_distributions(distributions)

# Calculate the average probability
average_probability = calculate_average_probability(merged_distribution)

# Calculate the average deviation
average_deviation = calculate_average_deviation(merged_distribution, average_probability)

# Calculate the occurrence percentage
occurrence_percentage = calculate_occurrence_percentage(merged_distribution, len(file_paths))

# Find the terms with low occurrence (less than 10%)
low_occurrence_terms = [word for word, percentage in occurrence_percentage.items() if percentage < 10]

# Write the output to a file
output_file_path = 'output.txt'
write_output(output_file_path, average_probability, average_deviation, occurrence_percentage, low_occurrence_terms)

print(f"Average Probability, Average Deviation, Occurrence Percentage, and Low Occurrence Terms have been calculated and saved to '{output_file_path}'.")
input("Press Enter to exit...")
