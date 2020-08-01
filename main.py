#HANGMAN GAME - PYTHON 

def hangman(word):  
  wrong = 0
  stages = ["",
            "_____________            ",
            "|           |            ",
            "|           |            ",
            "|           O            ",
            "|          /|\           ",
            "|           |            ",
            "|_________ / \ __________"
            ]
  remaining_letters = list(word)
  board = ["_"] * len(word)
  won = False
  print("Welcome to hangman :)")
  

  while wrong < len(stages) - 1:
    print("\n")
    letter_guess = "Please guess a letter "
    char = input(letter_guess)
    if char in remaining_letters:
      char_index = remaining_letters.index(char)
      board[char_index] = char
      remaining_letters[char_index] = '$'
    else:
      wrong = wrong + 1
    print((" ".join(board)))
    e = wrong +1
    print("\n".join(stages[0:e]))
    if "_" not in board:
      print("You win!")
      print(" ".join(board))
      won = True
      break
  if not won:
    print("You Lost The Word Was", word)
    print("\n".join(stages[0:wrong]))
hangman("hello")
  




