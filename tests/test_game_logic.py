from logic_utils import check_guess, get_attempt_limit, get_hint_message

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_repeated_guesses_use_numeric_secret():
    # AI helped me turn the mixed-type secret bug into a repeatable regression test.
    secret = 50

    assert check_guess(60, secret) == "Too High"
    assert check_guess(40, secret) == "Too Low"
    assert check_guess(secret, secret) == "Win"


def test_hint_message_matches_outcome():
    assert get_hint_message("Too High") == "📈 Go HIGHER!"


def test_attempt_limit_matches_difficulty():
    assert get_attempt_limit("Easy") == 6
    assert get_attempt_limit("Normal") == 8
    assert get_attempt_limit("Hard") == 5
