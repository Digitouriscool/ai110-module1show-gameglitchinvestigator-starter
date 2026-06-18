import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic_utils import check_guess, get_range_for_difficulty, parse_guess

def test_secret_from_wider_difficulty_is_outside_easy_range():
    """Regression: switching difficulty kept the old secret, so a Normal-mode
    secret (1-100) like 25 could appear as the secret in Easy mode (1-20)."""
    easy_low, easy_high = get_range_for_difficulty("Easy")
    normal_low, normal_high = get_range_for_difficulty("Normal")

    stale_secret = easy_high + 1  # e.g. 21 — valid for Normal, out of bounds for Easy

    assert normal_low <= stale_secret <= normal_high, "stale secret must be valid for Normal"
    assert not (easy_low <= stale_secret <= easy_high), "stale secret must be invalid for Easy"


def test_guess_outside_easy_range_is_rejected():
    """parse_guess now validates against the difficulty range, so a guess
    valid under Normal (e.g. 25) is rejected when the difficulty is Easy (1-20)."""
    easy_low, easy_high = get_range_for_difficulty("Easy")

    ok, value, err = parse_guess("25", easy_low, easy_high)

    assert not ok
    assert value is None
    assert err is not None


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
