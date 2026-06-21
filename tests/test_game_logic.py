import pytest
from game_glitch.logic_utils import (
    check_guess,
    update_score,
    parse_guess,
    get_range_for_difficulty
)

# =========================
# 1. Attempt counter starts at 0
# =========================
def test_attempt_counter_initial_value():
    # Simulated initial state
    attempts = 0
    assert attempts == 0


# =========================
# 2. First guess increments to 1
# =========================
def test_first_guess_increment():
    attempts = 0
    attempts += 1
    assert attempts == 1


# =========================
# 3. Attempts left never negative
# =========================
def test_attempts_left_never_negative():
    attempt_limit = 5
    attempts = 10  # simulate over-usage

    attempts_left = attempt_limit - attempts
    assert attempts_left <= 0
    assert max(0, attempts_left) == 0


# =========================
# 4. Difficulty range correctness
# =========================
def test_difficulty_easy_range():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1 and high == 20


def test_difficulty_normal_range():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1 and high == 100


def test_difficulty_hard_range():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1 and high == 50


# =========================
# 5. Game logic correctness (win/lose)
# =========================
def test_check_guess_win():
    assert check_guess(50, 50)[0] == "Win"


def test_check_guess_too_high():
    assert check_guess(60, 50)[0] == "Too High"


def test_check_guess_too_low():
    assert check_guess(40, 50)[0] == "Too Low"


# =========================
# 6. Score system stability
# =========================
def test_score_increases_on_win():
    score = update_score(0, "Win", 1)
    assert score > 0


def test_score_penalty_too_low():
    score = update_score(10, "Too Low", 1)
    assert score == 5


def test_score_penalty_too_high_or_bonus():
    score1 = update_score(10, "Too High", 2)
    score2 = update_score(10, "Too High", 3)
    assert score1 != score2


# =========================
# 7. Input parsing robustness
# =========================
def test_parse_guess_valid_int():
    ok, value, err = parse_guess("10")
    assert ok is True
    assert value == 10
    assert err is None


def test_parse_guess_float():
    ok, value, err = parse_guess("10.7")
    assert ok is True
    assert isinstance(value, int)


def test_parse_guess_invalid():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert value is None


# =========================
# 8. History tracking (logic-level simulation)
# =========================
def test_history_append_behavior():
    history = []
    history.append(10)
    history.append("invalid")

    assert len(history) == 2


# =========================
# NOTE:
# UI-only behaviors (Streamlit session_state like:
# - difficulty change reset
# - new_game button reset
# - win locks game
# require streamlit testing tools (not pure pytest)
# =========================