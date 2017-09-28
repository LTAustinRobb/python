#Tic Tac Toe

board =[0,1,2,
        3,4,5,
        6,7,8]

def show():
  print board[0],'|',board[1],'|',board[2]
  print "----------"
  print board[3],'|',board[4],'|',board[5]
  print "----------"
  print board[6],'|',board[7],'|',board[8]

def p1turn():

  input = raw_input("Player 1 Select a spot: ")
  input = int(input)

  if board[input] != 'x' and board[input] != 'o':
    board[input] = 'x'
  else:
    print "This spot is taken"
    p1turn()

def p2turn():

  input2 = raw_input("Player 2 Select a spot: ")
  input2 = int(input2)

  if board[input2] != 'x' and board[input2] != 'o':
    board[input2] = 'o'
  else:
    print "This spot is taken"
    p2turn()

show()
while True:
  p1turn()
  show()
  p2turn()
  show()



