import json

def beautify_json(input_file, output_file):
    # Read the JSON data from the input file
    with open(input_file, 'r') as infile:
        data = json.load(infile)

    # Beautify the JSON data with an indentation of 4 spaces
    beautified_json = json.dumps(data, indent=4)

    # Write the beautified JSON data to the output file
    with open(output_file, 'w') as outfile:
        outfile.write(beautified_json)

# Define the input and output file paths
input_file = 'random_stuff' #Filename where ugly json is located
output_file = 'random_stuff_output.json'

# Beautify the JSON file
beautify_json(input_file, output_file)

print(f"Beautified JSON has been written to {output_file}")