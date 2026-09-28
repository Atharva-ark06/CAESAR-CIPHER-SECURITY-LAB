from collections import Counter

from cipher_engine import CaesarCipher


def brute_force_decrypt(ciphertext: str) -> list[dict]:
    """
    Try every possible Caesar Cipher key.

    Returns all 26 possible plaintext candidates.
    """

    results = []

    for key in range(26):
        cipher = CaesarCipher(key)
        plaintext = cipher.decrypt(ciphertext)

        results.append({
            "key": key,
            "plaintext": plaintext,
        })

    return results


def frequency_analysis(text: str) -> dict:
    """
    Analyze alphabetic character frequency.
    """

    letters = [
        char.upper()
        for char in text
        if char.isalpha()
    ]

    if not letters:
        return {
            "total_letters": 0,
            "unique_letters": 0,
            "frequencies": {},
            "most_frequent": None,
        }

    counter = Counter(letters)
    total = len(letters)

    frequencies = {
        letter: {
            "count": count,
            "percentage": round((count / total) * 100, 2),
        }
        for letter, count in counter.most_common()
    }

    most_frequent = counter.most_common(1)[0]

    return {
        "total_letters": total,
        "unique_letters": len(counter),
        "frequencies": frequencies,
        "most_frequent": {
            "letter": most_frequent[0],
            "count": most_frequent[1],
            "percentage": round(
                (most_frequent[1] / total) * 100,
                2,
            ),
        },
    }


def verify_round_trip(
    plaintext: str,
    key: int,
) -> dict:
    """
    Encrypt and decrypt a message to verify
    that the original plaintext is recovered.
    """

    cipher = CaesarCipher(key)

    ciphertext = cipher.encrypt(plaintext)
    decrypted = cipher.decrypt(ciphertext)

    passed = decrypted == plaintext

    return {
        "plaintext": plaintext,
        "key": key % 26,
        "ciphertext": ciphertext,
        "decrypted": decrypted,
        "passed": passed,
    }