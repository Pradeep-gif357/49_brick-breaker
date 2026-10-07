# Brick Breaker Game

A simple **Brick Breaker / Breakout-style game** developed using **Python and Pygame**.

The player controls a paddle at the bottom of the screen and uses it to bounce a ball and destroy all the bricks. The game includes collision detection, scoring, lives, difficulty levels, replay functionality, and sound effects.

---

## 1. Project Overview

The **Brick Breaker Game** is a 2D arcade game where the player controls a paddle to keep a ball from falling below the screen.

The main objective is to destroy all the bricks using the bouncing ball.

### Main Features

- Paddle movement using keyboard
- Ball movement and bouncing
- Wall collision detection
- Paddle collision detection
- Brick collision detection
- Brick destruction
- Score system
- Life system
- Win condition
- Game-over condition
- Final score display
- Easy, Medium, and Hard difficulty levels
- Replay option
- Sound effects
- Smooth gameplay using Pygame

---

# 2. Technologies Used

- **Python 3.13**
- **Pygame**
- Object-Oriented Programming concepts
- Collision detection
- Keyboard input handling

---

# 3. Requirements

Before running the project, make sure Python is installed.

Recommended Python version:

```text
Python 3.10 or higher
```

The project was tested using:

```text
Python 3.13
```

The required Python package is:

```text
pygame
```

---

# 4. Project Structure

```text
49_brick-breaker-main
│
├── main.py
├── requirements.txt
├── README.md
│
└── game
    ├── __init__.py
    ├── ball.py
    ├── brick.py
    ├── paddle.py
    └── game_engine.py
```

### File Description

#### `main.py`

The main entry point of the game.

It handles:

- Pygame initialization
- Game window creation
- Difficulty selection
- Game loop
- Keyboard events
- Replay
- Exit option

#### `game/game_engine.py`

Contains the main game logic.

It handles:

- Ball movement
- Paddle movement
- Brick collision
- Wall collision
- Score
- Lives
- Win condition
- Game-over condition
- Difficulty settings
- Sound effects
- Game rendering

#### `game/ball.py`

Contains the `Ball` class.

It controls:

- Ball position
- Ball radius
- Ball velocity
- Ball movement
- Ball rectangle used for collision detection

#### `game/paddle.py`

Contains the `Paddle` class.

It controls:

- Paddle position
- Paddle size
- Paddle speed
- Paddle movement
- Screen boundary restrictions

#### `game/brick.py`

Contains the `Brick` class.

It controls:

- Brick position
- Brick size
- Brick status
- Brick collision rectangle

#### `requirements.txt`

Contains the required Python package:

```text
pygame
```

---

# 5. Installation

## Step 1: Open Command Prompt

Open **Command Prompt** or a terminal.

Go to the project folder.

Example:

```cmd
cd C:\Users\PRADEEP\Downloads\49_brick-breaker-main\49_brick-breaker-main
```

---

## Step 2: Install Pygame

If using Python 3.13:

```cmd
py -3.13 -m pip install pygame
```

Or install using the requirements file:

```cmd
py -3.13 -m pip install -r requirements.txt
```

---

# 6. Running the Game

After installing Pygame, run:

```cmd
py -3.13 main.py
```

The difficulty selection menu will appear.

```text
1 - Easy
2 - Medium
3 - Hard
Q - Exit
```

---

# 7. Game Controls

### Paddle Movement

Move the paddle using:

```text
Left Arrow  → Move Left
Right Arrow → Move Right
```

You can also use:

```text
A → Move Left
D → Move Right
```

### Other Controls

```text
1 → Easy
2 → Medium
3 → Hard
Q → Exit
```

After the game ends:

```text
ENTER → Replay
SPACE → Replay
ESC → Exit
```

---

# 8. Game Rules

The player controls the paddle at the bottom of the screen.

The ball moves around the screen and interacts with:

- Walls
- Paddle
- Bricks

When the ball hits a brick, the brick is destroyed and the player's score increases.

If the ball falls below the paddle, the player loses a life.

The game ends when:

### Win

All bricks are destroyed.

### Game Over

The player loses all available lives.

---

# 9. Task 1 - Improved Collision Detection

The original game always changed the vertical direction of the ball when it hit a brick.

This caused incorrect behavior when the ball hit the **left or right side** of a brick.

### Problem

Previously:

```text
Ball hits any part of brick
        ↓
Vertical velocity changes
```

This was incorrect for side collisions.

### Solution

The updated collision system checks which side of the brick was hit.

If the ball hits the:

```text
Left / Right side
        ↓
Horizontal velocity changes
```

If the ball hits the:

```text
Top / Bottom side
        ↓
Vertical velocity changes
```

This makes the ball movement more realistic.

### Collision Logic

```text
Left/Right collision → vx = -vx

Top/Bottom collision → vy = -vy
```

The previous ball position is also used to determine the collision direction.

---

# 10. Task 2 - Game Over and Win Screen

The game now displays a proper game-over or win screen.

## Win Screen

When all bricks are destroyed:

```text
YOU WIN!

Score: <final score>

Press ENTER or SPACE to continue
```

## Game Over Screen

When the player loses all lives:

```text
GAME OVER

Score: <final score>

Press ENTER or SPACE to continue
```

The game stops updating while the result screen is displayed.

The final score is shown to the player.

---

# 11. Task 3 - Replay and Difficulty Levels

The game now supports multiple difficulty levels.

The player can select:

```text
1 - Easy
2 - Medium
3 - Hard
```

## Easy

Easy mode provides slower gameplay and a larger paddle.

```text
Ball Speed: 3
Paddle Width: 120
Paddle Speed: 8
```

## Medium

Medium mode provides balanced gameplay.

```text
Ball Speed: 4
Paddle Width: 100
Paddle Speed: 7
```

## Hard

Hard mode provides faster gameplay and a smaller paddle.

```text
Ball Speed: 6
Paddle Width: 80
Paddle Speed: 6
```

### Difficulty Comparison

| Difficulty | Ball Speed | Paddle Width | Paddle Speed |
|---|---:|---:|---:|
| Easy | 3 | 120 | 8 |
| Medium | 4 | 100 | 7 |
| Hard | 6 | 80 | 6 |

---

# 12. Replay System

After winning or losing, the player can restart the game.

Press:

```text
ENTER
```

or

```text
SPACE
```

The difficulty selection menu appears again.

The player can then select a new difficulty.

For example:

```text
Game Over
     ↓
ENTER
     ↓
Difficulty Menu
     ↓
3 - Hard
     ↓
New Game
```

The player can also exit using:

```text
ESC
```

or:

```text
Q
```

---

# 13. Task 4 - Sound Effects

Sound feedback has been added to improve the gameplay experience.

The game provides sounds for important events.

### Brick Hit

A sound is played when the ball destroys a brick.

```text
Ball → Brick
       ↓
Brick destroyed
       ↓
Sound
```

### Paddle / Wall Hit

A sound is played when the ball hits the paddle or wall.

### Win

A different sound is played when the player destroys all bricks.

### Game Over

A game-over sound is played when the player loses all lives.

---

# 14. Sound Implementation

The game generates the sound effects using Pygame.

External audio files are not required.

The sounds are generated during runtime.

This makes the project easier to run because additional `.wav` or `.mp3` files are not required.

---

# 15. Scoring System

The player's score increases when a brick is destroyed.

Example:

```text
Brick destroyed
      ↓
Score increases
```

The final score is displayed on the win or game-over screen.

---

# 16. Life System

The player starts with:

```text
3 Lives
```

When the ball falls below the paddle:

```text
Life - 1
```

For example:

```text
Lives: 3
Ball falls
Lives: 2

Ball falls
Lives: 1

Ball falls
Lives: 0
      ↓
GAME OVER
```

---

# 17. Win Condition

The player wins when all bricks have been destroyed.

The game checks whether any bricks are still alive.

When there are no remaining bricks:

```text
All bricks destroyed
        ↓
YOU WIN
```

The final score is then displayed.

---

# 18. Game Flow

The complete game flow is:

```text
Start Program
      ↓
Difficulty Menu
      ↓
Select Difficulty
      ↓
Start Game
      ↓
Move Paddle
      ↓
Ball Moves
      ↓
Collision Detection
      ↓
Brick Destroyed?
   ↓          ↓
  Yes         No
   ↓          ↓
Score +1    Continue
      ↓
All Bricks Destroyed?
   ↓              ↓
  Yes             No
   ↓              ↓
 YOU WIN      Continue Game
                   ↓
             Ball Falls?
              ↓       ↓
             Yes      No
              ↓       ↓
          Lose Life  Continue
              ↓
          Lives = 0?
           ↓      ↓
          Yes     No
           ↓      ↓
      GAME OVER  Continue
           ↓
      Replay / Exit
```

---

# 19. Collision Detection

The game uses rectangle-based collision detection provided by Pygame.

The main objects involved are:

```text
Ball
Paddle
Brick
Wall
```

The ball's previous and current positions are used to determine the direction of brick collisions.

This prevents the ball from always bouncing vertically.

---

# 20. Object-Oriented Structure

The project uses separate classes for different game objects.

### Ball

```text
Ball
 ├── x
 ├── y
 ├── radius
 ├── vx
 └── vy
```

### Paddle

```text
Paddle
 ├── x
 ├── y
 ├── width
 ├── height
 └── speed
```

### Brick

```text
Brick
 ├── x
 ├── y
 ├── width
 ├── height
 └── alive
```

This makes the project easier to understand and maintain.

---

# 21. Expected Behavior

The completed game should provide:

- Smooth paddle movement
- Ball bouncing from walls
- Ball bouncing from the paddle
- Correct brick collision
- Brick destruction
- Score increase
- Life reduction when the ball falls
- Game-over screen
- Win screen
- Final score
- Easy difficulty
- Medium difficulty
- Hard difficulty
- Replay option
- Exit option
- Sound feedback

---

# 22. Testing Checklist

Before submission, verify the following.

### Task 1

- [ ] Ball hits left side of brick correctly
- [ ] Ball hits right side of brick correctly
- [ ] Ball hits top/bottom of brick correctly
- [ ] Brick disappears after being hit
- [ ] Score increases

### Task 2

- [ ] Game-over screen appears
- [ ] Win screen appears
- [ ] Final score is displayed
- [ ] Game waits for user input

### Task 3

- [ ] Easy mode works
- [ ] Medium mode works
- [ ] Hard mode works
- [ ] Difficulty changes gameplay
- [ ] Replay works
- [ ] Exit works

### Task 4

- [ ] Brick-hit sound works
- [ ] Paddle/wall sound works
- [ ] Win sound works
- [ ] Game-over sound works

---

# 23. Troubleshooting

## Pygame is not installed

Run:

```cmd
py -3.13 -m pip install pygame
```

## Game does not start

Make sure you are inside the folder containing:

```text
main.py
```

Check using:

```cmd
dir
```

You should see:

```text
main.py
requirements.txt
README.md
game
```

Then run:

```cmd
py -3.13 main.py
```

## Python version problem

Check the Python version:

```cmd
py -3.13 --version
```

Expected:

```text
Python 3.13.x
```

---

# 24. Project Objective

The objective of this project is to develop a simple but functional Brick Breaker game while learning important programming concepts such as:

- Python programming
- Pygame
- Classes and objects
- Game loops
- Keyboard input
- Collision detection
- Conditional statements
- Variables and data management
- Game states
- Difficulty management
- Sound effects

---

# 25. Conclusion

The Brick Breaker Game has been enhanced with improved collision detection, game-over and win screens, replay functionality, multiple difficulty levels, and sound effects.

The final project provides a complete playable Brick Breaker experience while demonstrating important concepts in Python game development using Pygame.

---

# 26. Submission Requirements

For submission, provide:

1. **10-second video before modifications**
2. **10-second video after modifications**
3. **Complete Chat/LLM conversation link or history**
4. **Complete project source code**

The final project should include:

```text
main.py
requirements.txt
README.md
game/
```

---

# 27. How to Run the Final Project

Use the following commands:

```cmd
cd C:\Users\PRADEEP\Downloads\49_brick-breaker-main\49_brick-breaker-main
```

Install the required package:

```cmd
py -3.13 -m pip install pygame
```

Run the game:

```cmd
py -3.13 main.py
```

Enjoy the game! 🎮
