gameboard = [[" "," "," "],[" "," "," "],[" "," "," "]]

def did_i_win(player):
  for i in range(3):
    if gameboard[i][0] == gameboard[i][1] == gameboard[i][2] == player:
      return True
    if gameboard[0][i] == gameboard[1][i] == gameboard[2][i] == player:
      return True
  if gameboard[0][0] == gameboard[1][1] == gameboard[2][2] == player:
    return True
  if gameboard[0][2] == gameboard[1][1] == gameboard[2][0] == player:
    return True
  return False

def print_board():
  for row in gameboard:
    print("|".join(row))

print_board()
current_player = "X"
moves_made = 0

while True:
  move = input("Player %s, enter your move (row and column 0-2): " % current_player)
  try:
    row, col = map(int, move.split())
  except ValueError:
    print("Invalid input. Enter two numbers separated by a space.")
    continue
  if not (0 <= row <= 2 and 0 <= col <= 2):
    print("Row and column must be between 0 and 2.")
    continue
  if gameboard[row][col] != " ":
    print("That spot is already taken. Try again.")
    continue

  gameboard[row][col] = current_player
  moves_made += 1
  print_board()

  if did_i_win(current_player):
    print("Player %s wins!" % current_player)
    break
  if moves_made == 9:
    print("The game is a draw.")
    break

  current_player = "O" if current_player == "X" else "X"
