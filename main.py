
import numpy as np


def checkWin(player):

    countRow = 0
    countClm = 0
    countDiag = 0

    if (player == 1):

        for row in board:
            countRow = 0
            for element in row:
                if (element == 1):
                    countRow += 1
                elif (element == 2 or element == 0):
                    countRow = 0
                if countRow >= 5:
                    return True

        for j in range(8):
            countClm = 0
            for r in list(board[:, j]):
                if (r == 1):
                    countClm += 1
                elif (r == 2 or r == 0):
                    countClm = 0
                if countClm >= 5:
                    return True

        for i in range(8):
            countDiag = 0
            for diag in list(np.diag(board, i)):
                if (diag == 1):
                    countDiag += 1
                elif (diag == 2 or diag == 0):
                    countDiag = 0

                if countDiag >= 5:
                    return True



    elif (player == 2):

        for row in board :
            for element in row:
                if(element == 2):
                    countRow+=1
                elif(element == 1 or element == 0):
                    countRow = 0
                if countRow >= 5:
                    return  True

        for j in range(8):
            for r in list(board[:, j]):

                if (r == 2):
                    countClm += 1
                elif (r == 1 or r == 0):
                    countClm = 0
                if countClm >= 5:
                    return True

        for i in range(8):
            countDiag = 0
            for diag in list(np.diag(board, i)):
                if (diag == 2):
                    countDiag += 1
                elif (diag == 1 or diag == 0):
                    countDiag = 0

                if countDiag >= 5:
                    return True

    return False


def printBoard():
    for i in range(8):
        print("|", end="")
        for j in range(8):
            if board[i][j] == 1:
                print(player1, end="|")
            elif board[i][j] == 2:
                print(player2, end="|")
            else:
                print(" ", end="|")
        print()
    print()
    print("---------------")



userEntry = int(input("Enter:\n1. manual entry for both ■’s moves and □’s moves:\n2. manual entry for ■’s moves & automatic moves for □\n3. manual entry for □’s moves & automatic moves for ■\n"))

if userEntry == 1:
    board = np.zeros((8, 8), dtype=int)
    player1 = "■"
    player2 = "□"
    newB = board.copy()
    print("Welcome to Magnetic Cave!")
    printBoard()
    while True:
        while True:
            row = int(input("Player1:Enter the row of the brick(0-7):"))
            clm = int(input("Player1:Enter the column of the brick(0-7):"))
            print(board[row][clm])
            if board[row][clm] != 0:
                print("That cell is already occupied! Try again.")
            elif clm == 0 or clm == 7 or board[row][clm - 1] != 0 or board[row][clm + 1] != 0:
                board[row][clm] = 1
                break
            else:
                print("You can only place your brick on the left or right wall, or next to another brick! Try again.")
        if (np.count_nonzero(board) == 64):
            print("Tie!!!!!!!")
            break
        if checkWin(1) == True:
            print("Player1 won")
            break
        printBoard()

        while True:
            row = int(input("Player2:Enter the row of the brick(0-7): "))
            clm = int(input("Player2:Enter the column of the brick(0-7):"))

            if board[row][clm] != 0:
                print("That cell is already occupied! Try again.")
            elif clm == 0 or clm == 7 or board[row][clm - 1] != 0 or board[row][clm + 1]:
                board[row][clm] = 2
                break
            else:
                print("You can only place your brick on the left or right wall, or next to another brick! Try again.")
        if (np.count_nonzero(board) == 64):
            print("Tie!!!!!!!")
            break
        if checkWin(2) == True:
            print("Player2 won")
            break
        printBoard()
    printBoard()
elif userEntry == 2:
    board = np.zeros((8 , 8) , dtype=int)
    player1 = "■"
    player2 = "□"
    class Node:
        def __init__(self, state ):
            self.state = state

            self.children = []
            player1 = "■"
            player2 = "□"

        def initialState(self):
            self.board = np.zeros((8, 8), dtype=int)

        def get_possible_movesMax(self, node):

            for i in range(8):
                for j in range(8):
                    newBoard = node.state.copy()
                    newNode = Node(state=newBoard)

                    if newNode.state[i][j] == 0 and (j == 0 or j == 7 or newNode.state[i][j - 1] != 0 or newNode.state[i][j + 1] != 0) and newNode.terminalState() == 3:
                        newNode.state[i][j] = 1
                        self.children.append(newNode)

        def get_possible_movesMin(self , node):
            for i in range(8):
                for j in range(8):
                    newBoard = node.state.copy()
                    newNode = Node(state=newBoard)

                    if newNode.state[i][j] == 0 and (j == 0 or j == 7 or newNode.state[i][j - 1] != 0 or newNode.state[i][j + 1] != 0) and newNode.terminalState() == 3:
                        newNode.state[i][j] = 2
                        self.children.append(newNode)

        def checkWin(self ,player):
            countRow = 0
            countClm = 0
            countDiag = 0

            if (player == 1):

                for i in range(8):
                    for clo in list(self.state[i]):
                        if (clo == 1):
                            countRow += 1
                        elif (clo == 2 or clo == 0):
                            countRow = 0

                        if countRow >= 5:
                            print(countRow)
                            return True

                for j in range(8):
                    for r in list(self.state[:, j]):
                        if (r == 1):
                            countClm += 1
                        elif (r == 2 or r == 0):
                            countClm = 0
                        if countClm >= 5:
                            print(countClm)
                            return True

                for i in range(8):
                    for diag in list(np.diag(self.state, i)):
                        if (diag == 1):
                            countDiag += 1
                        elif (diag == 2 or diag == 0):
                            countDiag = 0

                        if countDiag >= 5:
                            return True


            elif (player == 2):

                for i in range(8):
                    for clo in list(self.state[i]):
                        if (clo == 2):
                            countRow += 1
                        elif (clo == 1 or clo == 0):
                            countRow = 0

                        if countRow >= 5:
                            return True

                for j in range(8):
                    for r in list(self.state[:, j]):

                        if (r == 2):
                            countClm += 1
                        elif (r == 1 or r == 0):
                            countClm = 0
                        if countClm >= 5:
                            return True

                for i in range(8):
                    countDiag = 0
                    for diag in list(np.diag(self.state, i)):
                        if (diag == 2):
                            countDiag += 1
                        elif (diag == 1 or diag == 0):
                            countDiag = 0

                        if countDiag >= 5:
                            return True

            return False
        def terminalState(self ):
            if(np.count_nonzero(self.state) == 64):
                return 0
            if(self.checkWin(1)):
                return 1
            if(self.checkWin(2)):
                return -1
            return 3
        def evaluate(self):
            my_score = 0
            opp_score = 0

            count_my_row = [0] * 8
            count_opp_row = [0] * 8
            count_my_col = [0] * 8
            count_opp_col = [0] * 8

            # Evaluate consecutive bricks in rows and columns
            for i in range(8):
                for j in range(8):
                    if self.state[i][j] == 1:
                        count_my_row[i] += 1
                        count_my_col[j] += 1
                        count_opp_row[i] = 0
                        count_opp_col[j] = 0
                    elif self.state[i][j] == 2:
                        count_opp_row[i] += 1
                        count_opp_col[j] += 1
                        count_my_row[i] = 0
                        count_my_col[j] = 0
                    else:
                        count_my_row[i] = 0
                        count_my_col[j] = 0
                        count_opp_row[i] = 0
                        count_opp_col[j] = 0

                    if count_my_row[i] >= 5:
                        my_score += 1
                    elif count_opp_row[i] >= 5:
                        opp_score += 1

                    if count_my_col[j] >= 5:
                        my_score += 1
                    elif count_opp_col[j] >= 5:
                        opp_score += 1

            # Evaluate consecutive bricks in diagonals
            for i in range(4):
                count_my_diag = 0
                count_opp_diag = 0
                for j in range(8 - i):
                    if self.state[i + j][j] == 1:
                        count_my_diag += 1
                        count_opp_diag = 0
                    elif self.state[i + j][j] == 2:
                        count_opp_diag += 1
                        count_my_diag = 0
                    else:
                        count_my_diag = 0
                        count_opp_diag = 0

                    if count_my_diag >= 5:
                        my_score += 1
                    elif count_opp_diag >= 5:
                        opp_score += 1

            for i in range(1, 5):
                count_my_diag = 0
                count_opp_diag = 0
                for j in range(8 - i):
                    if self.state[j][i + j] == 1:
                        count_my_diag += 1
                        count_opp_diag = 0
                    elif self.state[j][i + j] == 2:
                        count_opp_diag += 1
                        count_my_diag = 0
                    else:
                        count_my_diag = 0
                        count_opp_diag = 0

                    if count_my_diag >= 5:
                        my_score += 1
                    elif count_opp_diag >= 5:
                        opp_score += 1

            return my_score - opp_score

        def printBoard(self):
            player1 = "■"
            player2 = "□"
            for i in range(8):
                print("|", end="")
                for j in range(8):
                    if self.state[i][j] == 1:
                        print(player1, end="|")
                    elif self.state[i][j] == 2:
                        print(player2, end="|")
                    else:
                        print(" ", end="|")
                print()
            print()
            print("---------------")




    board = np.zeros((8,8) , dtype = int)
    initialState = board

    root = Node(state=initialState)
    root.get_possible_movesMax(root)
    def limited_depth_first_search(node, depth_limit, current_depth, maximizing_player):

        if current_depth == depth_limit or node.terminalState() == 0 or node.terminalState() == 1 or node.terminalState()==-1:
            return node

        elif maximizing_player:
            max_eval = float('-inf')
            best_child = None
            node.get_possible_movesMax(node)

            for child in node.children:

                eval_score = limited_depth_first_search(child, depth_limit, current_depth + 1, False).evaluate()

                if eval_score > max_eval:
                    max_eval = eval_score
                    best_child = child

            #best_child.printBoard()
            return best_child
        else:
            min_eval = float('inf')
            best_child = None
            node.get_possible_movesMin(node)
            for child in node.children:
                eval_score = limited_depth_first_search(child, depth_limit, current_depth + 1, True).evaluate()


                if eval_score < min_eval:
                    min_eval = eval_score
                    best_child = child
            #best_child.printBoard()
            return best_child



    initialState = board.copy()



    isEnd = False
    print("Welcome to Magnetic Cave!")
    printBoard()
    while True:
        newBoard = board.copy()
        root = Node(state=newBoard)
        numberBricks = 0
        for i in range(8):
            numberBricks+= list(board[i]).count(1)

        while True:


            newB = limited_depth_first_search(root , numberBricks+3, numberBricks , True).state

            for c in root.children:

                if((newB == c.state).all()):
                    board = c.state.copy()
                    break
            break

        if (np.count_nonzero(board) == 64):
            print("Tie!!!!!!!")
            break
        if checkWin(1) == True:
            print("Player1 won")
            break

        printBoard()
        while True:
            row = int(input("Player2:Enter the row of the brick(0-7): "))
            clm = int(input("Player2:Enter the column of the brick(0-7):"))

            if board[row][clm] != 0 :
                print("That cell is already occupied! Try again.")
            elif clm ==0 or clm == 7 or board[row][clm-1] != 0 or board[row][clm+1]:
                board[row][clm] = 2
                break
            else:
                print("You can only place your brick on the left or right wall, or next to another brick! Try again.")
        if (np.count_nonzero(board) == 64):
            print("Tie!!!!!!!")
            break
        if checkWin(2) == True:
            print("Player2 won")
            break
        printBoard()

    printBoard()










#if The player want to play second:
elif userEntry == 3:
    board = np.zeros((8, 8), dtype=int)
    player1 = "■"
    player2 = "□"


    class Node:
        def __init__(self, state):
            self.state = state

            self.children = []
            player1 = "■"
            player2 = "□"

        def initialState(self):
            self.board = np.zeros((8, 8), dtype=int)



        def get_possible_movesMax(self, node):
            for i in range(8):
                for j in range(8):
                    if node.state[i][j] == 0 and (
                            j == 0 or j == 7 or node.state[i][j - 1] != 0 or node.state[i][j + 1] != 0):
                        newBoard = node.state.copy()
                        newBoard[i][j] = 2
                        newNode = Node(state=newBoard)
                        self.children.append(newNode)

        def get_possible_movesMin(self, node):
            for i in range(8):
                for j in range(8):
                    if node.state[i][j] == 0 and (
                            j == 0 or j == 7 or node.state[i][j - 1] != 0 or node.state[i][j + 1] != 0):
                        newBoard = node.state.copy()
                        newBoard[i][j] = 1
                        newNode = Node(state=newBoard)
                        self.children.append(newNode)

        def checkWin(self ,player):
            countRow = 0
            countClm = 0
            countDiag = 0

            if (player == 1):

                for i in range(8):
                    countRow = 0
                    for clo in list(self.state[i]):
                        if (clo == 1):
                            countRow += 1
                        elif (clo == 2 or clo == 0):
                            countRow = 0

                        if countRow >= 5:
                            print(countRow)
                            return True

                for j in range(8):
                    countClm = 0
                    for r in list(self.state[:, j]):
                        if (r == 1):
                            countClm += 1
                        elif (r == 2 or r == 0):
                            countClm = 0
                        if countClm >= 5:
                            print(countClm)
                            return True

                for i in range(8):
                    countDiag = 0
                    for diag in list(np.diag(self.state, i)):
                        if (diag == 1):
                            countDiag += 1
                        elif (diag == 2 or diag == 0):
                            countDiag = 0

                        if countDiag >= 5:
                            return True


            elif (player == 2):

                for i in range(8):
                    countRow = 0
                    for clo in list(self.state[i]):
                        if (clo == 2):
                            countRow += 1
                        elif (clo == 1 or clo == 0):
                            countRow = 0

                        if countRow >= 5:
                            return True

                for j in range(8):
                    countClm = 0
                    for r in list(self.state[:, j]):

                        if (r == 2):
                            countClm += 1
                        elif (r == 1 or r == 0):
                            countClm = 0
                        if countClm >= 5:
                            return True

                for i in range(8):
                    countDiag = 0
                    for diag in list(np.diag(self.state, i)):
                        if (diag == 2):
                            countDiag += 1
                        elif (diag == 1 or diag == 0):
                            countDiag = 0

                        if countDiag >= 5:
                            return True

            return False

        def terminalState(self):
            if (np.count_nonzero(self.state) == 64):
                return 0
            if (self.checkWin(2)):
                return 1
            if (self.checkWin(1)):
                return -1
            return 3

        def evaluate(self):
            my_score = 0
            opp_score = 0

            count_my_row = [0] * 8
            count_opp_row = [0] * 8
            count_my_col = [0] * 8
            count_opp_col = [0] * 8

            # Evaluate consecutive bricks in rows, columns, and diagonals
            for i in range(8):
                for j in range(8):
                    if self.state[i][j] == 2:
                        count_my_row[i] += 1
                        count_my_col[j] += 1
                        count_opp_row[i] = 0
                        count_opp_col[j] = 0
                    elif self.state[i][j] == 1:
                        count_opp_row[i] += 1
                        count_opp_col[j] += 1
                        count_my_row[i] = 0
                        count_my_col[j] = 0
                    else:
                        count_my_row[i] = 0
                        count_my_col[j] = 0
                        count_opp_row[i] = 0
                        count_opp_col[j] = 0

                    if count_my_row[i] >= 5:
                        my_score += 1
                    elif count_opp_row[i] >= 5:
                        opp_score += 2

                    if count_my_col[j] >= 5:
                        my_score += 1
                    elif count_opp_col[j] >= 5:
                        opp_score += 2

            for i in range(4):
                count_my_diag = 0
                count_opp_diag = 0
                for j in range(8 - i):
                    if self.state[i + j][j] == 2:
                        count_my_diag += 1
                        count_opp_diag = 0
                    elif self.state[i + j][j] == 1:
                        count_opp_diag += 1
                        count_my_diag = 0
                    else:
                        count_my_diag = 0
                        count_opp_diag = 0

                    if count_my_diag >= 5:
                        my_score += 1
                    elif count_opp_diag >= 5:
                        opp_score += 2

            for i in range(1, 5):
                count_my_diag = 0
                count_opp_diag = 0
                for j in range(8 - i):
                    if self.state[j][i + j] == 2:
                        count_my_diag += 1
                        count_opp_diag = 0
                    elif self.state[j][i + j] == 1:
                        count_opp_diag += 1
                        count_my_diag = 0
                    else:
                        count_my_diag = 0
                        count_opp_diag = 0

                    if count_my_diag >= 5:
                        my_score += 1
                    elif count_opp_diag >= 5:
                        opp_score += 2

            return my_score - opp_score

        def printBoard(self):
            player1 = "■"
            player2 = "□"
            for i in range(8):
                print("|", end="")
                for j in range(8):
                    if self.state[i][j] == 1:
                        print(player1, end="|")
                    elif self.state[i][j] == 2:
                        print(player2, end="|")
                    else:
                        print(" ", end="|")
                print()
            print()
            print("---------------")

        def checkWin(self, player):

            countRow = 0
            countClm = 0
            countDiag = 0

            if (player == 1):

                for i in range(8):
                    countRow = 0
                    for clo in list(self.state[i]):
                        if (clo == 1):
                            countRow += 1
                        elif (clo == 2 or clo == 0):
                            countRow = 0

                if countRow >= 5:
                    return True

                for j in range(8):
                    countClm = 0
                    for r in list(self.state[:, j]):
                        if (r == 1):
                            countClm += 1
                        elif (r == 2 or r==0):
                            countClm = 0
                if countClm >= 5:
                    return True

                for i in range(8):
                    countDiag = 0
                    for diag in list(np.diag(board, i)):
                        if (diag == 1):
                            countDiag += 1
                        elif (diag == 2 or diag ==0 ):
                            countDiag = 0

                if countDiag >= 5:
                    return True


            elif (player == 2):

                for i in range(8):
                    countRow = 0
                    for clo in list(self.state[i]):
                        if (clo == 2):
                            countRow += 1
                        elif (clo == 1 or clo == 0):
                            countRow = 0

                if countRow >= 5:
                    return True

                for j in range(8):
                    countClm = 0
                    for r in list(self.state[:, j]):
                        if (r == 2):
                            countClm += 1
                        elif (r == 1 or r == 0):
                            countClm = 0
                if countClm >= 5:
                    return True

                for i in range(8):
                    countDiag = 0
                    for diag in list(np.diag(board, i)):
                        if (diag == 2):
                            countDiag += 1
                        elif (diag == 1 or diag == 0):
                            countDiag = 0

                if countDiag >= 5:
                    return True
            return False


    board = np.zeros((8, 8), dtype=int)
    initialState = board

    root = Node(state=initialState)
    root.get_possible_movesMax(root)


    def limited_depth_first_search(node, depth_limit, current_depth, maximizing_player):
        if current_depth == depth_limit or node.terminalState() != 3:
            return node

        if maximizing_player:
            max_eval = float('-inf')
            best_child = None
            node.get_possible_movesMax(node)

            for child in node.children:
                eval_score = limited_depth_first_search(child, depth_limit, current_depth + 1, False).evaluate()

                if eval_score > max_eval:
                    max_eval = eval_score
                    best_child = child

            return best_child
        else:
            min_eval = float('inf')
            best_child = None
            node.get_possible_movesMin(node)

            for child in node.children:
                eval_score = limited_depth_first_search(child, depth_limit, current_depth + 1, True).evaluate()

                if eval_score < min_eval:
                    min_eval = eval_score
                    best_child = child

            return best_child


    initialState = board.copy()

    isEnd = False
    print("Welcome to Magnetic Cave!")
    while True:

        while True:
            row = int(input("Player2:Enter the row of the brick(0-7): "))
            clm = int(input("Player2:Enter the column of the brick(0-7):"))

            if board[row][clm] != 0:
                print("That cell is already occupied! Try again.")
            elif clm == 0 or clm == 7 or board[row][clm - 1] != 0 or board[row][clm + 1]:
                board[row][clm] = 1
                break
            else:
                print("You can only place your brick on the left or right wall, or next to another brick! Try again.")
        if checkWin(1) == True:
            print("Player1 won")
            break
        if (np.count_nonzero(board) == 64):
            print("Tie!!!!!!!")
            break
        printBoard()



        while True:

            isEnd = False
            newBoard = board.copy()
            root = Node(state=newBoard)
            numberBricks = 0
            for i in range(8):
                numberBricks += list(board[i]).count(1)
            print(numberBricks)
            newB = limited_depth_first_search(root, numberBricks + 3, numberBricks, True).state

            for c in root.children:

                if ((newB == c.state).all()):
                    board = c.state.copy()
                    break
            break


        if (np.count_nonzero(board) == 64):
            print("Tie!!!!!!!")
            break
        if checkWin(2) == True:
            print("Player2 won")
            break



        printBoard()

    printBoard()