import typer

"""Let's make a hangman game."""

print("Type the letter to guess the word and press enter within the time limit!")
lives = 6 
user_level = typer.choose_user_level()
words_level, vector = typer.pick_random_words(user_level)
while lives > 0:
    user_letter = typer.get_user_input(5)
    vector,flag = typer.compare_position_word(user_letter, words_level, vector)
    lives = typer.decrease_lives(lives,flag, words_level)
    typer.show_user_screen(vector, lives)
    
print("Thanks for playing.")
