from project import GuessGame, get_guess, check_guess, play

#  Test get_guess() user to enter only valid inputs ( a number between 1 and 20)


def test_get_guess():

    assert get_guess("7") == 7
    assert get_guess("25") is None
    assert get_guess("abc") is None

#  Test check_guess() function


def test_check_guess_correct():
    game = GuessGame()
    game._number = 10
    game._attempts = 0

    result = check_guess(10, game)
    assert result is True
    assert game._attempts == 1


#  Test play() logic without interactive input
def test_play_logic():
    game = GuessGame()
    game._number = 10
    game._attempts = 0

    # Simulate what play() does by calling check_guess manually
    guesses = [5, 15, 10]  # too low, too high, correct
    for guess in guesses:
        correct = check_guess(guess, game)
        if correct:
            break

    # After simulation, attempts should be 3
    assert game._attempts == 3
