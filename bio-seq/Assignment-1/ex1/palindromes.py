import argparse
import re
from collections import Counter
from pathlib import Path

# 1. Check individual words and number sequences to see whether they are palindromes.
# 2. Ignore capitalization: Anna and anna are counted together.
# 3. Count how often each palindrome occurs.
# 4. Write the palindromes and their frequencies to an output file.


def find_palindromes(text):

    # Ignore capitalization: Anna and anna are counted together.
    text = text.casefold()

    # Check individual words and number sequences to see whether they are palindromes.
    tokens = re.findall(r"[^\W_]+", text)

    counts = Counter()

    for token in tokens:
        # the token is a palindrome if it reads the same forwards and backwards
        if token == token[::-1]:
            counts[token] += 1

    return counts


def main():

    #python palindromes.py input_file output_file
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file",)
    parser.add_argument("output_file",)
    #reads the command line arguments and returns them as an object
    args = parser.parse_args() 


    #turn the input and output file paths into Path objects
    input_path = Path(args.input_file)
    output_path = Path(args.output_file)

    if input_path.resolve() == output_path.resolve():
        parser.error(
            "Input and output must be different files."
        )

    try:
        #read the input file as text
        text = input_path.read_text(encoding="utf-8-sig")

        counts = find_palindromes(text)

        #write the palindromes and their frequencies to an output file
        with output_path.open("w", encoding="utf-8") as output:
            output.write("palindromes\tcount\n")

            #loop through sorted(counts.items()) that provides pairs of palindromes and their counts, sorted by the palindrome
            for palindrome, count in sorted(counts.items()):
                output.write(f"{palindrome}\t{count}\n")

    except (OSError, UnicodeError) as error:
        parser.exit(1, f"error: {error}\n")


if __name__ == "__main__":
    main()