# This script is designed to tally the occurrences of unique strings from a hardcoded list and write the results to an output file. 
# It is particularly useful for analyzing class specs from World of Warcraft encounters. You can customize the list of strings to analyze different specs.

# How to use this script:

# 1. Install Python:
#    - Go to the official Python website: https://www.python.org/
#    - Download and install the latest version of Python for your operating system.
#    - During installation, make sure to check the box that says "Add Python to PATH".

# 2. Save the Script:
#    - Copy the script into a text editor and save it with a .py extension, for example, count_specs.py.

# 3. Run the Script:
#    - Open a terminal or command prompt.
#    - Navigate to the directory where you saved the script.
#    - Run the script using the command: python count_specs.py

# 4. Check the Output:
#    - After running the script, check the current directory for a file named output.txt. This file will contain the counts of each unique string, sorted in descending order by their occurrences.

# Example Output:
# Count: 8, String: BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkUgUIJJRaEIiQKSLkEUQCAAAAAA
# Count: 4, String: BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkIIFSSSkCBiIki0CJBFkAAAAAAA
# Count: 4, String: BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkUgUIJJRKEIiQKSLkEUQCAAAAAA
# Count: 4, String: BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkIIFSSSkGBiIki0CJBFkAAAAAAA
# Count: 3, String: BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkUg0IJJRaEIiQKSLkEUQCAAAAAA
# Count: 2, String: BIQAAAAAAAAAAAAAAAAAAAAAAgEkEAAAAAAAAAAAAgQKOAJJt0ikkERigUIJJRKEgIki0CJBFkAAAAAAA
# Count: 2, String: BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkIIFSSSkSEgIki0CJBFkAAAAAAA
# Count: 2, String: BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkIINSSSkGBiIki0CJBFkAAAAAAA
# Count: 1, String: BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkUgUIJJRaRAiQKSLkEUQCAAAAAA
# Count: 1, String: BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkASjkkEpEBiIki0CJBFkAAAAAAA
# Count: 1, String: BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkASLSyBSkCBiIki0CJBFkAAAAAAA
# Count: 1, String: BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkIINSSSkGBCSkSLtQSAkAAAAAAA
# Count: 1, String: BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkUCOQJSiEpQgICpItQSQBJAAAAAAA
# Count: 1, String: BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDEJJtISSSEJCShkkEpRgICpItQSQBJAAAAAAA
# Count: 1, String: BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkIIFSSCpEBiIki0CJBFkAAAAAAA
# Count: 1, String: BIQAAAAAAAAAAAAAAAAAAAAAAgEkEAAAAAAAAAAAAgQKOAJJt0ikkERSBShkkEpRAiQKSLkEUQCAAAAAA
# Count: 1, String: BIQAAAAAAAAAAAAAAAAAAAAAAgEkEAAAAAAAAAAAAgQKOAJJt0ikkERigUIJJRKRAiQItQSQBJAAAAAAA
# Count: 1, String: BIQAAAAAAAAAAAAAAAAAAAAAAgEkEAAAAAAAAAAAAgQKOAJJt0ikkERC4AFSSSkmEIiQKSLkEUQCAAAAAA
# Count: 1, String: BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkIIFSSSkCBiIkSLCJBFkAAAAAAA
# Count: 1, String: BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkmDQSSLtIJJRkUgUIJJRKRgICp0iQCUQCAAAAAA
# Count: 1, String: BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkUgDUIJJRKRASCpItQSQBJAAAAAAA
# Count: 1, String: BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkUgUIJJRaSgICpItQCUQCAAAAAA
# Count: 1, String: BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIOQKOAJJt0OgkkERigUIJJRKEIiQatIkEUQCAAAAAA
# Count: 1, String: BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkIIFSSSkWEgIki0CJBFkAAAAAAA
# Count: 1, String: BIQAAAAAAAAAAAAAAAAAAAAAAgEkEAAAAAAAAAAAAgQKOAJJt0ikkEBQJFSSSkGhIiQKSLkEUQCAAAAAA
# Count: 1, String: BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkUCOQJSiEpRgICpItQSQBJAAAAAAA
# Count: 1, String: BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkIIFSiEpQIiIki0CJBFkAAAAAAA
# Count: 1, String: BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkIFShkIRaRgICpItQSQBJAAAAAAA
# Count: 1, String: BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRQJFShkkEpEBIJki0CJBFkAAAAAAA
# Count: 1, String: BIQAAAAAAAAAAAAAAAAAAAAAAgEkEAAAAAAAAAAAAgQKOAJJt0ikkERigUIJJRKSggQKSLkEAJAAAAAAA
# Total lines: 51

# Customizing the Script:
# To analyze different specs, replace the hardcoded list of strings (strings) with your own list of class specs from World of Warcraft encounters. 
# You can gather these specs from websites like Warcraft Logs: https://www.warcraftlogs.com/

# Import necessary modules
from collections import Counter
import os

def main():
    # Hard coded list of strings
    # Example strings represent Shadow Priests on Mythic Igira the Cruel
    strings = [
        # Shadow Priests on Mythic Igira the Cruel
        "BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkUgUIJJRaRAiQKSLkEUQCAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgEkEAAAAAAAAAAAAgQKOAJJt0ikkERigUIJJRKEgIki0CJBFkAAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkIIFSSSkCBiIki0CJBFkAAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkUgUIJJRaEIiQKSLkEUQCAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkASjkkEpEBiIki0CJBFkAAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkIIFSSSkSEgIki0CJBFkAAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkUgUIJJRaEIiQKSLkEUQCAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkASLSyBSkCBiIki0CJBFkAAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkIINSSSkGBCSkSLtQSAkAAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkUgUIJJRKEIiQKSLkEUQCAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkUgUIJJRKEIiQKSLkEUQCAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkIIFSSSkCBiIki0CJBFkAAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkUgUIJJRaEIiQKSLkEUQCAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkUCOQJSiEpQgICpItQSQBJAAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDEJJtISSSEJCShkkEpRgICpItQSQBJAAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkIIFSSSkGBiIki0CJBFkAAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkIIFSSCpEBiIki0CJBFkAAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkIIFSSSkGBiIki0CJBFkAAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgEkEAAAAAAAAAAAAgQKOAJJt0ikkERSBShkkEpRAiQKSLkEUQCAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkUgUIJJRaEIiQKSLkEUQCAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkUgUIJJRaEIiQKSLkEUQCAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkIIFSSSkGBiIki0CJBFkAAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgEkEAAAAAAAAAAAAgQKOAJJt0ikkERigUIJJRKRAiQItQSQBJAAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgEkEAAAAAAAAAAAAgQKOAJJt0ikkERigUIJJRKEgIki0CJBFkAAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkUg0IJJRaEIiQKSLkEUQCAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgEkEAAAAAAAAAAAAgQKOAJJt0ikkERC4AFSSSkmEIiQKSLkEUQCAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkUgUIJJRaEIiQKSLkEUQCAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkIIFSSSkCBiIkSLCJBFkAAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkmDQSSLtIJJRkUgUIJJRKRgICp0iQCUQCAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkUgDUIJJRKRASCpItQSQBJAAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkIIFSSSkSEgIki0CJBFkAAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkUgUIJJRaSgICpItQCUQCAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIOQKOAJJt0OgkkERigUIJJRKEIiQatIkEUQCAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkIIFSSSkCBiIki0CJBFkAAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkIIFSSSkWEgIki0CJBFkAAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgEkEAAAAAAAAAAAAgQKOAJJt0ikkEBQJFSSSkGhIiQKSLkEUQCAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkIINSSSkGBiIki0CJBFkAAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkUgUIJJRaEIiQKSLkEUQCAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkIIFSSSkGBiIki0CJBFkAAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkUgUIJJRaEIiQKSLkEUQCAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkIINSSSkGBiIki0CJBFkAAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkUg0IJJRaEIiQKSLkEUQCAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkUCOQJSiEpRgICpItQSQBJAAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkUgUIJJRKEIiQKSLkEUQCAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkUg0IJJRaEIiQKSLkEUQCAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkIIFSiEpQIiIki0CJBFkAAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkUgUIJJRKEIiQKSLkEUQCAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkIFShkIRaRgICpItQSQBJAAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRkIIFSSSkCBiIki0CJBFkAAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgAJBAAAAAAAAAAAAIkiDQSSLtIJJRQJFShkkEpEBIJki0CJBFkAAAAAAA",
        "BIQAAAAAAAAAAAAAAAAAAAAAAgEkEAAAAAAAAAAAAgQKOAJJt0ikkERigUIJJRKSggQKSLkEAJAAAAAAA"
    ]

    # Counting occurrences of each string
    count = Counter(strings)

    # Sorting by count in descending order
    sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)

    # Prepare the path for the output file in the current directory
    output_path = os.path.join(os.getcwd(), "output.txt")

    # Use with statement to open and write to the file
    with open(output_path, 'w') as writer:
        # Printing out the number of matches for each string into the file
        for item in sorted_count:
            writer.write(f"Count: {item[1]}, String: {item[0]}\n")
        
        # Print the total number of lines in the strings collection
        writer.write(f"Total lines: {len(strings)}\n")

    # Optionally, you can also print a message to the console to indicate that the operation was successful
    print(f"Results have been written to {output_path}")

if __name__ == "__main__":
    main()
