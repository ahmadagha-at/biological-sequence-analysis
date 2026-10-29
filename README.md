# Biological Sequence Analysis
A collection of Python exercises for analyzing text and biological sequences.
## Assignment 1
### Exercise 1: Find Palindromes
`palindromes.py` reads a text file, finds words and number sequences that read the same forwards and backwards, counts how often each palindrome occurs, and writes the results to an output file. Matching is case-insensitive.
### Exercise 2: Find Restriction Sites
`restriction_sites.py` reads a DNA sequence from a FASTA file and searches for recognition sites of the restriction enzymes PpuMI, MspA1I, and MslI using regular expressions. It detects overlapping matches and writes each enzyme's name and the position of the first base after the cut to a tab-separated output file. Positions start at 1.
## Assignment 2
### Exercise 3: Sequence Dot Plot
`ex03_012314193.py` compares two sequences and visualizes matching regions in a dot plot using Matplotlib. It slides a window over both sequences and draws a dot at the center of each pair of identical windows. The two sequences and a positive odd window size are passed as command-line arguments. Matching is case-sensitive.
