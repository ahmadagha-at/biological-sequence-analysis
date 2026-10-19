import sys
import re


# 1. Read the FASTA file: skip the header line starting with > and join the DNA sequence lines.
# 2. Search for the three recognition patterns using regular expressions.
# 3. For each match, calculate the position of the first base after the cut, using positions starting at 1.
# 4. Write the enzyme name and the position after the cut to the output file.

# Check that exactly two file names were provided.
if len(sys.argv) != 3:
    sys.exit("Usage: python restriction_sites.py input.fasta output.txt")

input_file = sys.argv[1]
output_file = sys.argv[2]

# Prevent overwriting the input file.
if input_file == output_file:
    sys.exit("Input and output must be different files.")

# Read the DNA and skip the FASTA header.
with open(input_file, encoding="utf-8-sig") as file:
    dna = ""

    for line in file:
        if not line.startswith(">"):
            dna += line.strip().upper()

# Enzyme name, recognition pattern, bases before the cut.
#The numbers tell us how many bases come before 
# the cut within each recognition pattern.  
enzymes = [
    ("PpuMI", r"[AG]GG[AT]CC[CT]", 2),
    ("MspA1I", r"C[AC]GC[GT]G", 3),
    ("MslI", r"CA[CT][ACGT]{4}[AG]TG", 5)
]

# Find all sites and write the results.
with open(output_file, "w", encoding="utf-8") as output:
    output.write("enzyme\tposition_after_cut\n")

    for name, pattern, offset in enzymes:
        for match in re.finditer(f"(?=({pattern}))", dna):
            position = match.start() + offset + 1
            output.write(f"{name}\t{position}\n")