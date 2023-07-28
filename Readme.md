# AI project - (Guess the Number Game)

## Introduction

This Python script is a simple guessing game called "Guess the Number" In this game, the user thinks of a number within a specified range, and the AI attempts to guess the number by making educated guesses based on the user's feedback.

#### Contributers to this project

1. Roy BCS-01-0814/2022
2. Alyakbar BCS-03-0003/2022
3. Martin BCS-03-0002/2022
4. Stephen BCS-03-4177/2022
5. Omenke BSCIT-01-0413/2022

---

### How to Play The Game

1. The game starts by displaying a welcome message, introducing the user to the game.
2. The user is prompted to think of a number between a lower and an upper bound (inclusive).
3. The AI will then make its first guess within the defined range.
4. The user provides feedback to the AI by responding with one of the following options:

   <b>'H':</b> The guess is too high.

   <b>'L':</b> The guess is too low.

   <b>'C':</b> The AI guessed correctly.

5. Based on the user's response, the AI will adjust its guessing strategy to narrow down the range for the next guess and continue the guessing process.
6. The game will repeat the guessing and feedback process until the AI correctly guesses the user's number.

Snap:
![game guess](https://github.com/alyakbar/AI-Project/assets/30528167/3fb031df-61b4-4626-a6e0-b2e1124c8914)

---

### Running The Guess Game

Requirements:

- `Python 3.x`
- `Git`

#### Cloning & Running Script:

Open your terminal and type:

` git clone https://github.com/alyakbar/AI-Project`

Change directory to AI-Project where the script is:
` cd AI-Project`

Run the script using the command:

`python guess_the_numbe.py.`

---

### Features in this Guess Game:

- **AI Guessing**: The AI is capable of making guesses to determine the number the user is thinking of.

- **Feedback Mechanism**: The user can provide feedback to the AI's guess, helping it to adjust its subsequent guesses. Feedback options include:

  'H': The guess is too high.

  'L': The guess is too low.

  'C': The AI guessed correctly.

- **User-Friendly Interface**: The game presents a user-friendly interface with clear instructions and messages to guide the user through the gameplay.

- **Time Delay**: The game uses time delays to enhance the user experience, providing brief pauses between messages to improve readability.

- **Dynamic Range Adjustment**: The AI dynamically adjusts the guessing range based on the user's feedback to narrow down the possible numbers, improving its chances of guessing correctly.

- **Game Completion**: The game concludes when the AI successfully guesses the user's number and displays the correct guess along with a victory message.
- **Error Handling**: The game handles invalid user inputs during feedback, prompting the user to re-enter a valid option until the correct input is provided.

- **Difficulty Levels**: Users are have the capability to choose the game mode on different levels i.e. Easy, Medium & Hard levels.

- **Guess Limit**: We've also added a means in which users can define the number of Guesses to make the game a bit fun and challenging.

### Contribution:

Added a new variable to track the number of guesses the AI has made.
guess_count

- Explain what you're working on by adding an issue before making any changes.
