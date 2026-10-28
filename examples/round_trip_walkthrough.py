"""Demonstrate encryption/decryption round-trip verification."""
from pprint import pprint
from cryptanalysis import verify_round_trip
if __name__=="__main__":
    pprint(verify_round_trip("Classroom example only",7))