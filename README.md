# MY CS50P PROJECT
![Static Badge](https://img.shields.io/badge/My_Name%3A-Shailesh_Ramteke-blue)

![Static Badge](https://img.shields.io/badge/Link_For-YouTube-blue)   <URL .com>
# Project title: "Guess it!"

## Project Description
This game, written in Python, is a quiz that asks the user to guess a number between 1 and 20. It counts the attempts made to get a correct answer and prints the result, along with the grade awarded. Time taken to guess the correct answer in seconds is also displayed.

## Project Explanation
"Guess it" is an interactive Python command-line game developed as my final project for CS50P as per the instructions given. User(the player) is asked to guess a randomly generated number by system between 1 and 20, receiving feedback on whether their guess is lower than the number  or higher than the number. The game tracks attempts and awards a performance rating with stars based on guess efficiency. Built with object-oriented principles, it uses pyfiglet for an ASCII art title and includes a robust test suite to ensure functionality. The project demonstrates input validation, error handling, and modular design, meeting CS50P's requirements for a well-tested, user-friendly program.

## How to run the program
- install dependencies: `$ pip install -r requirements.txt`
- Run program: `$ python project.py`
- Test program: `$ pytest test_project.py`

## Libraries used 
- pyfiglet (external)
- random   (inbuilt)
- datetime (inbuilt)


## Detailed Description
This game challenges players to guess a number between 1 and 20, randomly selected by the program. Key features include:

- ASCII Art Title: Displays "GUESS THE NUMBER" using pyfiglet with a slant font for visual appeal.
- Input Validation: Ensures guesses are integers between 1 and 20, with clear error messages for invalid inputs (e.g., non-numbers or out-of-range values).
- Feedback System: Guides players with messages like "Guess a higher Number...⬆️" or "Guess a lower Number...⬇️."
- Attempt Tracking: Counts guesses and displays the total upon winning.
- Performance Rating: Awards ratings based on attempts:
  - ≤ 2: "Excellent" (★★★★★)
  - 3–5: "Very Good" (★★★★)
  - 6–8: "Good" (★★★)
  - above 8: "Satisfactory" (★)
- The number of thumb-ups👍 along with the result are equal to number of attmpts made for right  answer.
- Time taken to complete the game is also displayed in the result. 
- Test Suite: test_project.py verifies input handling, guess checking, and gameplay logic using pytest.

### Files
- project.py: Contains the GuessGame class, input validation (get_guess), guess checking (check_guess), and gameplay loop (play).
- test_project.py: Tests key functions for valid inputs, edge cases, and correct game behavior.
- requirements.txt: Lists pyfiglet as the dependency.

### File Descriptions

- README.md: In this I Write about my project what my program does and how does it work 
- project.py: This is the main file of the project with one main function and three subfunctions.
- requirements.txt: in this all the requirement is been stored
- test_project.py: In this file all three the test cases for testing this project are covered. 

### Installation and Usage
1. Install dependencies: pip install -r requirements.txt
2. Run the game: python project.py
3. Enter guesses (1–20) and follow prompts until the player guess correctly.
4. Run tests: python -m pytest test_project.py
5. All invalid options are validated during accepting the input from player.

### Dependencies
- Python 3
- pyfiglet (install via pip install pyfiglet)

### Notes
- The game uses emojis (e.g. ❌, ✅, ⭐) for a fun, engaging experience.
- The test suite ensures robustness by handling invalid inputs and edge cases.
- Future enhancements could include difficulty levels or a replay option.


