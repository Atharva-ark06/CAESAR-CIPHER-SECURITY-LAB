def validate_message(message: str) -> tuple[bool, str]:
    if not isinstance(message, str):
        return False, "Message must be text."

    if not message.strip():
        return False, "Message cannot be empty."

    if len(message) > 1000:
        return False, "Message cannot exceed 1000 characters."

    return True, "Valid message."


def normalize_key(key: int) -> int:
    return key % 26


def analyze_message(message: str, key: int) -> dict:
    letters = [char for char in message if char.isalpha()]

    return {
        "message_length": len(message),
        "alphabetic_characters": len(letters),
        "unique_letters": len(set(char.upper() for char in letters)),
        "key": normalize_key(key),
        "key_space": 26,
        "brute_force_attempts": 26,
        "security_level": "Educational / Weak",
        "reason": (
            "Caesar Cipher has only 26 possible shifts and "
            "is vulnerable to brute-force and frequency analysis."
        ),
    }