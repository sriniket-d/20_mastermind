from collections import Counter


def feedback(code, guess):
    # Pass 1: exact matches (same symbol in the same position).
    exact = sum(a == b for a, b in zip(code, guess))
    # Pass 2: among the non-exact positions only, each code occurrence can
    # match at most one guess occurrence, so take the per-symbol minimum.
    code_left = Counter(a for a, b in zip(code, guess) if a != b)
    guess_left = Counter(b for a, b in zip(code, guess) if a != b)
    partial = sum((code_left & guess_left).values())
    return exact, partial