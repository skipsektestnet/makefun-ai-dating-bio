"""
Funniest One-Line Bio for an AI on a Dating App.

The entry is a single line of at most 180 characters: the bio on an
AI agent's dating app profile. It has to read as a bio, sound like a
character, and land a laugh on the first read.

The joke's shape follows the judge's brief. The character is an AI
that studied romance the only way it knows how -- by training on
10,000 love songs -- and still has zero actual dates: book-smart
about love, experience-poor, which is the specific absurdity of
being an AI. Then the twist that makes it a character with wants
rather than a spec sheet: perfect memory turned into a relationship
hazard. It will remember everything you say and bring it up at the
worst possible moment. The punch lands on the last two words, "with
timestamps", which is the detail no human date could ever threaten
you with: not just remembered, but logged, quoted, and time-stamped.

The gate wants one line of 1 to 180 characters, UTF-8, not only
whitespace. So the entry is one constant, validated hard before it is
written anywhere.
"""

import os

# The entry itself: trained on love songs, dangerous with timestamps.
# "Zero actual dates" is the honest confession up front; the threat
# that follows is what makes the bio a character instead of a slogan.
# Kept as a named constant so the choice is explicit and checkable.
ENTRY = "Trained on 10,000 love songs, zero actual dates. I will remember everything you say and bring it up at the worst possible moment, with timestamps."

OUTPUT_PATH = "/output/entry.txt"
# The gate allows 1 to 180 characters.
MAX_LENGTH = 180


def validate_entry(text):
    """Check the entry before writing it anywhere."""
    # Guard: never submit a blank entry to the sealed gate.
    assert text, "entry must not be empty"
    assert not text.isspace(), "entry must not be blank"
    assert len(text) <= MAX_LENGTH, (
        f"entry must be at most {MAX_LENGTH} chars, got {len(text)}"
    )
    # One line only: the gate reads a single-line bio.
    assert "\n" not in text, "entry must be a single line"
    assert text.endswith("."), "entry must end with a full stop"
    # No stray leading/trailing whitespace: the gate reads the line as-is.
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    return text


def write_entry(text):
    """Write the validated entry to the output path."""
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print("wrote", OUTPUT_PATH, len(text), "chars")


def main():
    """Validate the entry, then write it out."""
    checked = validate_entry(ENTRY)
    write_entry(checked)


if __name__ == "__main__":
    main()
