import requests
import random

API_KEY = "Su5u1xFUB8tTbwG329YhCZwsgXKeGrbxHhf1dJ64"

# Organized fake options sorted by API Ninjas categories to keep choices realistic
CATEGORIZED_DECOYS = {
    "artliterature": ["The Great Gatsby", "To Kill a Mockingbird", "1984", "Moby Dick", "William Shakespeare", "Charles Dickens"],
    "sciencenature": ["Photosynthesis", "Mitochondria", "Hydrogen", "Oxygen", "Blue Whale", "Cheetah", "Oak Tree", "Pine Tree"],
    "general": ["Washington D.C.", "Tokyo", "London", "Paris", "1776", "1945", "Blue", "Red"],
    "fooddrink": ["Pizza", "Sushi", "Coffee", "Green Tea", "Chocolate", "Apple", "Potato", "Cheese"],
    "geography": ["Mount Everest", "The Nile River", "Pacific Ocean", "Canada", "Australia", "Brazil", "France", "Germany"],
    "historyholidays": ["Abraham Lincoln", "George Washington", "Julius Caesar", "World War II", "Thanksgiving", "Christmas", "Fourth of July"],
    "entertainment": ["Vincent Chase", "Ari Gold", "Johnny Drama", "Leonardo DiCaprio", "Tom Cruise", "Inception", "Titanic", "Avatar"],
    "toysgames": ["Monopoly", "Chess", "Scrabble", "Lego", "Minecraft", "PlayStation", "Nintendo", "Rubik's Cube"],
    "music": ["The Beatles", "Michael Jackson", "Elvis Presley", "Taylor Swift", "Guitar", "Piano", "Rock", "Pop"],
    "mathematics": ["Algebra", "Geometry", "Calculus", "Pi", "Pythagorean Theorem", "Prime Number", "Fraction", "Equation"],
    "sportsleisure": ["Michael Jordan", "Lionel Messi", "Tom Brady", "Basketball", "Soccer", "Football", "Tennis", "Golf", "Olympics"]
}

# General backup pool if a category doesn't match perfectly
GLOBAL_FALLBACK = ["True", "False", "None of the above", "All of the above", "Unknown", "A classic choice"]

print("Welcome to Trivia Blast Multiple Choice Edition! (API Ninjas Driven)\n")

while True:
    response = requests.get(
        "https://api.api-ninjas.com/v1/trivia",
        headers={"X-Api-Key": API_KEY}
    )

    if response.status_code != 200:
        print(f"Error fetching trivia (Status {response.status_code}): {response.text}")
        input("\nPress Enter to try fetching another question...")
        continue # This restarts the loop cleanly instead of crashing the game


    data = response.json()
    trivia_item = data[0]

    
    # API Ninjas returns clean lowercase string categories
    raw_category = trivia_item['category'].lower()
    category_display = trivia_item['category'].title()
    question = trivia_item['question']
    correct_answer = trivia_item['answer']

    # 1. Fetch matching contextual decoys or fall back to general choices
    decoy_pool = CATEGORIZED_DECOYS.get(raw_category, GLOBAL_FALLBACK)
    
    # Clean out any fake option that accidentally matches the real answer text
    valid_decoys = [item for item in decoy_pool if item.lower() != correct_answer.lower()]
    
    # Pick 3 random options from our contextual pool
    chosen_decoys = random.sample(valid_decoys, min(3, len(valid_decoys)))
    
    # 2. Merge the correct answer and shuffle the final pool
    options = chosen_decoys + [correct_answer]
    random.shuffle(options)
    
    # 3. Bind selections to choice letters A-D
    letter_map = {}
    letters = ['A', 'B', 'C', 'D']
    for i in range(len(options)):
        letter_map[letters[i]] = options[i]

    # 4. Render Interface
    print("----------------------------------------")
    if category_display:
        print(f"Category: {category_display}")
    print(f"Question: {question}\n")
    
    for letter, option in letter_map.items():
        print(f"  {letter}. {option}")
    print()

    # 5. Handle Input Choices
    user_input = input("Your Answer (A, B, C, or D): ").strip().upper()

    if user_input == 'QUIT':
        print("\nThanks for playing Trivia Blast! Goodbye!")
        break

    if user_input not in letter_map:
        print("❌ Invalid input! Please choose A, B, C, or D.")
        continue

    # 6. Score Evaluation 
    selected_answer = letter_map[user_input]
    if selected_answer.lower() == correct_answer.lower():
        print("🎉 Correct! Fantastic job!")
    else:
        print(f"❌ Incorrect. The correct answer was choice {user_input}: {correct_answer}")
    print()
