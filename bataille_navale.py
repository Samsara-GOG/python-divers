#Converti de Python 2.7 à 3
#importation librairie pour nbre entier aléatoire
from random import randint

# initialisation de la liste
board = []

# Dimensions du terrain
for x in range(5):
  board.append(["O"] * 5)

# Type d'affichage de chaque case
def print_board(board):
  for row in board:
    print(" ".join(row))

# Génération du terrain
print_board(board)

# Placement aléatoire de la coordonnée au niveau row d'un bateau à 1 case de dimension
def random_row(board):
  return randint(0, len(board) - 1)

# Placement aléatoire de la coordonnée au niveau column d'un bateau à 1 case de dimension
def random_col(board):
  #besoin d'acceder à la première row pour y coller le debut de la colonne
  return randint(0, len(board[0]) - 1)

# attribution des coordonnées pour le bateau à 1 case
ship_row = random_row(board)
ship_col = random_col(board)
# coordonnees du bateau à 1 case pour debuggage
print(ship_row)
print(ship_col)

# Boucle générale pour tout ce qui va suivre ensuite, 1 iteration = 1 tour pour le jeu avec range(nbredetour)
for turn in range(4):
  print("Turn", turn + 1)   
# Bonne indentation de 4 espaces requis pour intégrer tout ce qui va suivre dans la boucle!
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

  # Si le tir touche un bateau
  if (guess_row == ship_row and guess_col == ship_col):
    print("Congratulations! You sunk my battleship!")
    break

  else:
    # Si çà touche ou pas selon les limites du terrain naval 
    if (guess_row < 0 or guess_row > 5) or (guess_col < 0 or guess_col > 5):
      print("Oops, that's not even in the ocean.")
    # si çà touche un endroit deja visee
    elif (board[guess_row][guess_col] == "X"):
      print("You guessed that one already.")
    else:
      # Tir sans atteindre de cible
      print("You missed my battleship!")
      # Croix à l'endroit du tir
      board[guess_row][guess_col] = "X"
    # Détermination du nombre de tours avant Game Over
    if turn == 3:
      print("Game Over")
  # Afficage du nombre de tour en cours
  print("Turn", turn + 1)  
  # Actualisation du terrain en fonction des tirs
  print_board(board)
  


"""
You can also add on to your Battleship! program to make it more complex and fun to play. Here are 
some ideas for enhancements—maybe you can think of some more!

    - Make multiple battleships: you’ll need to be careful because you need to make sure that you 
    don’t place battleships on top of each other on the game board. 
    You’ll also want to make sure that you balance the size of the board with the number of ships 
    so the game is still challenging and fun to play.

    - Make battleships of different sizes: this is trickier than it sounds. All the parts of the 
    battleship need to be vertically or horizontally touching and you’ll need to make sure you don’t 
    accidentally place part of a ship off the side of the board.

    - Make your game a two-player game.

    - Use functions to allow your game to have more features like rematches, statistics and more!

Some of these options will be easier after we cover loops in the next lesson. Think about 
coming back to Battleship! after a few more lessons and see what 
other changes you can make!
"""
