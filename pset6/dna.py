import csv
import sys

def main():
    # Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: {} + file.csv + file.txt".format(sys.argv[0]))
        sys.exit(1)
    # Read database file into a variable
    data = []
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        next(reader)
        for row in reader:
            data.append(row)

    #Read DNA sequence file into a variable
    sequence = ""
    with open(sys.argv[2], "r") as file:
        reader = csv.reader(file)
        for str in reader:
            sequence = str
            
    sequence = sequence[0]

    #Find longest match of each STR in DNA sequence
    
    for dict in data[:1]:
        keys = list(dict.keys())
    
    run = []
    for key in keys[1:]:
        longest_run = longest_match(sequence, key)
        run.append(longest_run)
    
    #Check database for matching profiles
    
    for dict in data:
        values = list(dict.values())    
        if values[1:] == run:
             print(values[0])
             return    

    print("no match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1
            
            # If there is no match in the substring
            else:
                break
        
        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return str(longest_run)


main()
