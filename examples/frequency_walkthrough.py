"""Show letter-frequency statistics for synthetic sample text."""
from pprint import pprint
from cryptanalysis import frequency_analysis
if __name__=="__main__":
    pprint(frequency_analysis("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"))