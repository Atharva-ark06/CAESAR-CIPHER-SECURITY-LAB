"""Print candidate decryptions for a toy ciphertext."""
from cryptanalysis import brute_force_decrypt
if __name__=="__main__":
    for candidate in brute_force_decrypt("KHOOR"):
        print(f"key={candidate['key']:2}: {candidate['plaintext']}")