import re

def convert_spelled_digits(input_string):
    # Define a dictionary to map spelled digits to their numerical values
    digit_mapping = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    # Use a regular expression to find spelled digits and replace them with numerical values
    for spelled_digit, numerical_digit in digit_mapping.items():
        input_string = re.sub(spelled_digit, numerical_digit, input_string)

    # Remove non-digit characters
    input_string = re.sub(r'\D', '', input_string)

    return input_string

def process_output(output_string):
    # Check if the output is a single digit
    if len(output_string) == 1:
        # Repeat the digit to make it a two-digit number
        output_string *= 2
    elif len(output_string) > 2:
        # If more than two digits, combine the first and last digits
        output_string = output_string[0] + output_string[-1]

    return output_string

# Read the content of a file
file_path = 'Day_01.txt'  # Replace with the actual file path

# Initialize a variable to accumulate the sums
total_sum = 0

with open(file_path, 'r') as file:
    # Process each line separately
    for line in file:
        # Convert spelled-out digits to numerical values and remove non-digit characters
        line = convert_spelled_digits(line.strip())
        
        # Apply the process_output function to each line
        output_string = process_output(line)
        
        # Store two-digit numbers in a list
        two_digit_numbers = [int(output_string[i:i+2]) for i in range(0, len(output_string), 2) if len(output_string[i:i+2]) == 2]

        # Sum the two-digit numbers and accumulate the total
        # total_sum += sum(two_digit_numbers)

# Print the total sum for all lines
print(two_digit_numbers)
