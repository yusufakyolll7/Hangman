hangman_pics = [
    """
     ------
    |     |
    |
    |
    |
    |
    |
    |
    |
    --------
    """,
    """
     ------
    |     |
    |     O
    |
    |
    |
    |
    |
    |
    --------
    """,
    """
     ------
    |     |
    |     O
    |     |
    |
    |
    |
    |
    |
    --------
    """,
    """
     ------
    |     |
    |     O
    |    /|
    |
    |
    |
    |
    |
    --------
    """,
    """
     ------
    |     |
    |     O
    |    /|\
    |
    |
    |
    |
    |
    --------
    """,
    """
     ------
    |     |
    |     O
    |    /|\
    |    /
    |
    |
    |
    |
    --------
    """,
    """
     ------
    |     |
    |     O
    |    /|\
    |    / \
    |
    |
    |
    |
    --------
    """
]

import random
word_list=["python", "developer", "hangman", "coding", "programming", "algorithm"]

def get_random_word(word_list):
    return random.choice(word_list)

def display_word_state(secret_word,guessed_list):
    return " ".join([letter if letter in guessed_list else "_" for letter in secret_word])

def get_player_guess():
    while True:
        guess=input("Make a guess: ").lower()
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Invalid entry.Please guess a single letter")

def update_guessed_letters(guessed_letters, player_guess):
    if player_guess not in guessed_letters:
        guessed_letters.append(player_guess)

def hangman_game():
    secret_word = get_random_word(word_list)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = len(hangman_pics) - 1

    print("Welcome to Hangman")

    while incorrect_guesses < max_incorrect_guesses:
        print(hangman_pics[incorrect_guesses])
        print(display_word_state(secret_word,guessed_letters))
        player_guess = get_player_guess()

        if player_guess in secret_word:
            update_guessed_letters(guessed_letters,player_guess)
        else:
            incorrect_guesses += 1
            print(f"Wrong guess! You have {max_incorrect_guesses - incorrect_guesses } chance left.")

        if all(letter in guessed_letters for letter in secret_word):
            print(f"Congratulations!You find the word : {secret_word}")
            break
    else:
        print(hangman_pics[incorrect_guesses])
        print(f"Game Over! You lost! The word was : {secret_word}")

hangman_game()

