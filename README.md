# 🎯 Trivia Blast — Multiple Choice Edition

**Trivia Blast** is a Python terminal trivia game powered by the **API Ninjas Trivia API**. It fetches trivia questions from the internet, creates multiple-choice answers, and lets the player answer using **A, B, C, or D**.

## ✨ Features

* 🌐 Uses the **API Ninjas Trivia API** to get questions
* 🎲 Randomly shuffles the answer choices
* 🧠 Supports different trivia categories
* 📝 Creates three additional answer choices using category-based decoys
* ⌨️ Allows the player to answer directly in the terminal
* ❌ Handles invalid input
* 🔄 Automatically tries again if the API request fails
* 🚪 Allows the player to quit
* 🎉 Gives instant feedback after every answer

## 🛠️ Technologies Used

* **Python**
* **Requests**
* **Random**
* **API Ninjas Trivia API**

## 📦 Installation

### 1. Install Python

Make sure Python is installed on your computer.

You can check by running:

```bash
python --version
```

### 2. Install Requests

Open your terminal and run:

```bash
pip install requests
```

### 3. Get an API Ninjas API Key

Create an account at **API Ninjas** and get your own API key.

Then put your key into the Python program:

```python
API_KEY = "YOUR_API_KEY_HERE"
```

> ⚠️ **Security:** Never publish your real API key on GitHub. If you already uploaded a key publicly, generate a new one and replace it.

## ▶️ How to Run

Save the program as:

```text
trivia_blast.py
```

Then run:

```bash
python trivia_blast.py
```

You should see:

```text
Welcome to Trivia Blast Multiple Choice Edition!
(API Ninjas Driven)
```

A trivia question will then appear with four choices:

```text
----------------------------------------
Category: Geography
Question: What is the largest ocean on Earth?

  A. Atlantic Ocean
  B. Pacific Ocean
  C. Indian Ocean
  D. Arctic Ocean

Your Answer (A, B, C, or D):
```

Type your answer and press **Enter**.

## 🎮 How to Play

1. Read the trivia question.
2. Look at the four answer choices.
3. Type **A**, **B**, **C**, or **D**.
4. Press **Enter**.
5. The game tells you whether your answer is correct.
6. A new question is automatically loaded.

To quit, type:

```text
QUIT
```

## 🧩 How the Answer Choices Work

The API provides the **correct answer**, but the program creates the other three choices itself.

For example, if the category is `geography`, the program can select possible decoy answers from:

```python
"geography": [
    "Mount Everest",
    "The Nile River",
    "Pacific Ocean",
    "Canada",
    "Australia",
    "Brazil",
    "France",
    "Germany"
]
```

The program then randomly selects three decoys and combines them with the real answer.

Finally, all four choices are shuffled so the correct answer isn't always in the same position.

## 🔄 Error Handling

If the API request fails, the game doesn't crash. Instead, it displays the error and gives the player another chance:

```text
Error fetching trivia (Status 400): ...
Press Enter to try fetching another question...
```

This makes the game more reliable when there is a problem connecting to the API.

## 📚 Categories

The program includes custom answer pools for categories such as:

* 🎨 Art & Literature
* 🔬 Science & Nature
* 🌎 Geography
* 🍕 Food & Drink
* 📜 History & Holidays
* 🎬 Entertainment
* 🎮 Toys & Games
* 🎵 Music
* ➗ Mathematics
* 🏀 Sports & Leisure
* 🌐 General

## 🚀 Future Improvements

Here are some ideas I could add in future versions:

* 🏆 Add a score counter
* ❤️ Add lives
* ⏱️ Add a timer
* 📊 Add a final score screen
* 🔥 Add a streak system
* 🥇 Add difficulty levels
* 💾 Save high scores
* 🎨 Create a graphical version with PyQt5
* 👥 Add multiplayer mode
* 📈 Track correct and incorrect answers
* 🔊 Add sound effects

## 📁 Project Structure

```text
Trivia-Blast/
│
├── trivia_blast.py
└── README.md
```

## 🎯 Project Goal

I built this project to practice:

* Working with APIs
* Using Python's `requests` library
* Working with JSON data
* Using dictionaries and lists
* Randomizing data
* Handling user input
* Handling API errors
* Building a complete terminal-based game

## 🙌 Credits

Trivia questions are provided by the **API Ninjas Trivia API**.

This project was created as a Python programming project to practice working with APIs and building interactive games.
