import typer

"""Let's make a hangman game."""

print("Type the words and hit enter within the time limit!")
lives = 6 
words_level, vector = typer.pick_random_words("easy")
while lives > 0:
    user_letter = typer.get_user_input(20)
    vector,flag = typer.compare_position_word(user_letter, words_level, vector)
    lives = typer.decrease_lives(lives,flag)
print("Thanks for playing.")
