
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic Hangman word-guessing game using Python strings, loops, and user input. Students will practice string manipulation, control flow, and simple game state management.

## 📝 Tasks

### 🛠️	Build the Hangman Game

#### Description
Implement a command-line Hangman game. The program should pick a secret word and let the player guess letters until they either discover the word or run out of allowed incorrect attempts.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list of words
- Accept single-letter guesses (case-insensitive) and update the displayed progress (e.g., P _ _ T _ N)
- Show letters already guessed and ignore repeated guesses (do not penalize again)
- Track and display the number of incorrect guesses remaining
- End the game when the word is fully guessed or attempts are exhausted
- Display a clear win or lose message and reveal the secret word when the game ends
- Use functions to organize the code (e.g., separate functions for input, state update, and rendering)

#### Example
```
Secret word: PYTHON
Current: _ _ _ _ _ _
Guessed: 
Attempts remaining: 6

Enter a letter: p
Current: P _ _ _ _ _
Guessed: P
Attempts remaining: 6

Enter a letter: z
Z is not in the word.
Current: P _ _ _ _ _
Guessed: P, Z
Attempts remaining: 5
```

### 🛠️	Optional Challenge: Difficulty & Word File

#### Description
Add an optional difficulty setting (e.g., Easy/Medium/Hard) that controls allowed attempts or word length, or load words from an external text file.

#### Requirements
Completed program should:

- Support at least two difficulty levels that affect game rules (attempts or word choices)
- Or load the word list from a text file `words.txt` in the assignment folder
- Include brief usage instructions in the code README or comments

