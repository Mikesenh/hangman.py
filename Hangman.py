# TODO: Import the random module
import random

hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# TODO: Create a list that contains 15 words (with varying lengths) as strings (use this to randomly 
# create the word_to_guess
word_list = ["coyote", "deer", "eagle","ferret", "mule", "python", "shark","sheep", "spider", "toad","pigeon", "tiger", "wombat","zebra", "swan"]
word_to_guess = random.sample(word_list, k=1)
word_to_guess = str(word_to_guess)
#removing extra text
word_to_guess = word_to_guess[2:]
word_to_guess = word_to_guess[:-2]
print(" word to guess is : " + word_to_guess)
end_word_show = word_to_guess
word_to_guess = list(word_to_guess)


# TODO: Define a function called `create_initial_hint` that takes one parameter:
# word_to_guess ( a list that represents the word to guess, for example: ['b','l','a','c','k']   )
# after processing the input the function should return the initial hint (for example
# given the above input the function should return  ['_','_','_','_','_'] )
def create_initial_hint(word_to_guess):
    word_to_guess_blank = list(word_to_guess)
    for numbers, letters in enumerate(word_to_guess):
        word_to_guess_blank[numbers] = ' _ '
    #word_to_guess_blank = "".join(word_to_guess_blank)
    #print(word_to_guess_blank)
    return word_to_guess_blank

word_to_guess_blank = create_initial_hint(word_to_guess)
hint_keeper = word_to_guess_blank

# TODO: Define a function called `create_hint` that takes three parameters:
# word_to_guess ( a list that represents the word to guess, for example: ['b','l','a','c','k']   )
# hint( a list that represents the hint so far, for example:    ['b','_','a','_','_'] )
# guess ( a string that represents the guess, for example: 'c'
# after processing the input the function should return the hint (for example given 
# the above input the function should return ['b','_','a','c','_'])

def create_hint(word_to_guess,hint_keeper,guess_input):
    player_is = ""
    for numbers, letters in enumerate(word_to_guess):
        if guess_input == letters:
            guess_input_right = guess_input
            hint_keeper[numbers] = guess_input_right
            player_is = 'right'
    hint_shower = " ".join(hint_keeper)
    return hint_shower

def right_wrong(word_to_guess,hint_keeper,guess_input):
    player_is = ""
    for numbers, letters in enumerate(word_to_guess):
        if guess_input == letters:
            guess_input_right = guess_input
            hint_keeper[numbers] = guess_input_right
            player_is = 'right'
    hint_shower = " ".join(hint_keeper)
    return player_is


# TODO After creating the above functions and verifying they work create the rest of the program using,
# among other things, a while loop
continue_game = True
body_count = 0
inverse_body_count = 6
print(hangman[body_count])

while continue_game:
    guess_input = input("What is your guess? ")
    guess_input = guess_input.lower()
    hint_shower = create_hint(word_to_guess,hint_keeper,guess_input)
    player_is = right_wrong(word_to_guess,hint_keeper,guess_input)
    if hint_keeper == word_to_guess:
        print("Congratz You Won!")
        continue_game = False
    if player_is == 'right':
        print(hangman[body_count])
        print("You guessed right. Here is your progress: " + hint_shower)
        player_is == ""
    else:
        body_count += 1
        inverse_body_count -= 1
        inverse_body_count = str(inverse_body_count)
        print(hangman[body_count])
        print("Sorry wrong guess. " + inverse_body_count + " Lives Left! Here is your progress: " + hint_shower)
        inverse_body_count = int(inverse_body_count)
    if body_count > 5:
        print("You Lost! The Word Was: " + end_word_show + " . Good Luck, Next Time!")
        continue_game = False


