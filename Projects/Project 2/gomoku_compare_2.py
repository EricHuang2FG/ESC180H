#This function returns True iff there are no stones on the board board
def is_empty(board):
    for row in range(len(board)):
        for entry in board[row]:
            if entry != " ":
                return False

    return True

'''
This function analyses the sequence of length length that ends at location (y end, x end). The function returns "OPEN" if the sequence is open, "SEMIOPEN" if the sequence if semi-open, and "CLOSED" if the sequence is closed. Assume that the sequence is complete (i.e., you are not just given a subsequence) and valid, and contains stones of only one colour
'''
def is_bounded(board, y_end, x_end, length, d_y, d_x):

    #check boundedness of vertical sequences
    if d_y == 1 and d_x == 0:
        nextx = x_end #never off
        nexty = y_end+1 #off if greater than len(board)-1
        previousx = x_end #never off
        previousy = y_end-length #off if less than 0
        nextoff = False
        previousoff = False

        #check boarder + 1 sqaures
        if nexty > len(board)-1:
            nextoff = True
        if previousy < 0:
            previousoff = True

    #check boundedness of horizontal sequences
    if d_y == 0 and d_x == 1:
        nextx = x_end+1 #off if greater than len(board)-1
        nexty = y_end #never off
        previousx = x_end-length #off if less than 0
        previousy = y_end #never off
        nextoff = False
        previousoff = False

        #check boarder + 1 sqaures
        if nextx > len(board)-1:
            nextoff = True
        if previousx < 0:
            previousoff = True

    #check boundedness of left to right diagonal sequences
    if d_y == 1 and d_x == 1:
        nextx = x_end+1 #off if greater than len(board)-1
        nexty = y_end+1 #off if greater than len(board)-1
        previousx = x_end-length #off if less than 0
        previousy = y_end-length #off if less than 0
        nextoff = False
        previousoff = False

        #check boarder + 1 sqaures
        if max(nextx, nexty) > len(board)-1: #if the max isn't greater, min also not
            nextoff = True
        if min(previousx, previousy) < 0:
            previousoff = True

    #check boundedness of right to left diagonal sequences
    if d_y == 1 and d_x == -1:
        nextx = x_end-1 #off if less than 0
        nexty = y_end+1 #off if greater than len(board)-1
        previousx = x_end+length #off if great than len(board)-1
        previousy = y_end-length #off if less than 0
        nextoff = False
        previousoff = False

        #check boarder + 1 sqaures
        if nextx < 0 or nexty > len(board)-1:
            nextoff = True
        elif nextx >=0 and nexty <= len(board)-1:
            nextoff = False
        if previousx > len(board)-1 or previousy < 0:
            previousoff = True
        elif previousx <= len(board)-1 or previousy>=0:
            previousoff = False


    #if both ends off board, then closed
    if previousoff == True and nextoff == True:
        return "CLOSED"

    #if previous is off but end is on
    if previousoff == True and nextoff == False:
        if board[nexty][nextx] == " ":
            return "SEMIOPEN"
        else:
            return "CLOSED"

    #if previous is on but end is off
    if previousoff == False and nextoff == True:
        if board[previousy][previousx] == " ":
            return "SEMIOPEN"
        else:
            return "CLOSED"

    #if both sides are on
    if previousoff == False and nextoff == False:
        #if both sides empty
        if board[nexty][nextx] == " " and board[previousy][previousx] == " ":
            return "OPEN"
        elif board[nexty][nextx] == " " or board[previousy][previousx] == " ":
            return "SEMIOPEN"
        else:
            return "CLOSED"


'''
This function analyses the row (let’s call it R) of squares that starts at the location (y start,x start)and goes in the direction (d y,d x). Note that this use of the word row is different from “a row in a table”. Here the word row means a sequence of squares, which are adjacent either horizontally,or vertically, or diagonally. The function returns a tuple whose first element is the number of opensequences of colour col of length length in the row R, and whose second element is the number ofsemi-open sequences of colour col of length length in the row R. Assume that (y start,x start) is located on the edge of the board. Only complete sequences count.For example, column 1 in Fig. 1 is considered to contain one open row of length 3, and no other
rows. Assume length is an integer greater or equal to 2.
'''

def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    open_seq_count = 0
    semi_open_seq_count = 0
    consec = 0

    #counting for specified column
    if d_y == 1 and d_x == 0:
        #keep x_start, but start y from 0 because we want to check entire column

        #iterate through rows
        for row in range(len(board)):
            #if current is col, add to consecutive
            if board[row][x_start] == col:
                consec += 1
            elif board[row][x_start] != col:
                consec = 0 #break consecutives if current is not col

            #when consecutive is length, check for desired sequence
            if consec == length:
                if is_bounded(board,row,x_start,length,1,0) == "OPEN":
                    open_seq_count += 1
                    consec = 0
                elif is_bounded(board,row,x_start,length,1,0) == "SEMIOPEN":
                    if row + 1 < len(board) and board[row+1][x_start] == col:
                        # are conditoinals checked sequentially??
                        consec = 0
                    elif row + 1 < len(board) and board[row+1][x_start] != col:
                        semi_open_seq_count += 1
                        consec = 0
                    elif row + 1 >= len(board):
                        semi_open_seq_count += 1
                        consec = 0

        #BUT WHAT IF ROW+1 IS OUT OF BOUNDS, BUT CONSEC IS STILL CONSEC i think i accounted for this, but check logic again.... need to specify what happens if row + 1 < len(board) is false (off board)
        #BUT WHAT IF 3 BY 3 BOARD, DONT U ALSO HAVE TO CHECK IF CLOSEED? oh no its only asking for semi or open



    #counting for specified horizontal row
    if d_y == 0 and d_x == 1:

        #iterate through columns
        for column in range(len(board)):

            #if current is col, add to consecutive
            if board[y_start][column] == col: #DO I NEED TO SAY AND CONSEC < LENGTH??
                consec += 1
            elif board[y_start][column] != col:
                consec = 0 #break consecutives if current is not col

            #when consecutive is length, check for desired sequence
            if consec == length:
                if is_bounded(board,y_start,column,length,0,1) == "OPEN":
                    open_seq_count += 1
                    consec = 0
                elif is_bounded(board,y_start,column,length,0,1) == "SEMIOPEN":
                    if column + 1 < len(board) and board[y_start][column+1] == col:
                        consec = 0
                    elif column + 1 < len(board) and board[y_start][column+1] != col:
                        semi_open_seq_count += 1
                        consec = 0
                    elif column + 1 >= len(board):
                        semi_open_seq_count += 1
                        consec = 0



    #counting for left to right diagonal row
    if d_y == 1 and d_x == 1:

        #find starting position of diagonal
        #subtract from x and y position until one is 0
        while x_start!=0 and y_start!=0:
            x_start-=1
            y_start-=1

        #iterate through diagonal
        for i in range(y_start, len(board)-x_start):

            #if current col is requested and consecutive col is less than length
            if board[i][i-y_start + x_start] == col and consec < length: #THIS GOES OUT OF INDEX WHEN I IS 7............... x and y going out?
                consec +=1

            #if current col is not requested
            elif board[i][i-y_start + x_start] != col:
                consec = 0


            #when consecutive is length, check for desired sequence
            if consec == length:
                if is_bounded(board,i,i-y_start + x_start,length,1,1) == "OPEN":
                    open_seq_count += 1
                    consec = 0
                elif is_bounded(board,i,i-y_start + x_start,length,1,1) == "SEMIOPEN":
                    if max(i+1, i-y_start + x_start+1)<len(board) and board[i+1][i-y_start + x_start+1] == col:
                        consec = 0
                    elif max(i+1, i-y_start + x_start+1)<len(board) and board[i+1][i-y_start + x_start+1] != col:
                        semi_open_seq_count += 1
                        consec = 0
                    elif max(i+1, i-y_start + x_start+1)>=len(board):
                        semi_open_seq_count += 1
                        consec = 0



    #counting for right to left diagonal row
    if d_y == 1 and d_x == -1:


        #find starting position of diagonal
        #subtract from x and y position until x is 7 or y is 0
        while x_start!=7 and y_start!=0:
            x_start+=1
            y_start-=1


        #iterate through column from y_start to end of column
        for i in range(y_start, len(board)):

            #if current col is requested and consecutive col is less than length
            if board[i][x_start + y_start - i] == col and consec < length:
                consec +=1

            #if current col is not requested
            elif board[i][x_start + y_start - i] != col:
                consec = 0


            if consec == length:
                if is_bounded(board,i,x_start + y_start - i,length,1,-1) == "OPEN":
                    open_seq_count += 1
                    consec = 0
                elif is_bounded(board,i,x_start + y_start - i,length,1,-1) == "SEMIOPEN":

                    if i+1<len(board) and x_start + y_start - i -1 >= 0 and board[i+1][x_start + y_start - i -1] == col:
                        consec = 0
                    elif i+1<len(board) and x_start + y_start - i -1 >= 0 and board[i+1][x_start + y_start - i -1] != col:
                        semi_open_seq_count += 1
                        consec = 0
                    elif i+1>=len(board) or x_start + y_start - i -1 < 0:
                        semi_open_seq_count += 1
                        consec = 0



    return open_seq_count, semi_open_seq_count


'''
This function analyses the board board. The function returns a tuple, whose first element is the number of open sequences of colour col of length lengthon the entire board, and whose second element is the number of semi-open sequences of colour col of length length on the entire board. Only complete sequences count. For example, Fig. 1 is considered to contain one open row of length 3, and no other rows. Assume length is an integer greater or equal to 2.
'''

def detect_rows(board, col, length):
    open_seq_count, semi_open_seq_count = 0, 0
    consec = 0

    #but we need to check entire row, not just from y start
    # so for vert checks, need the use x_start and the overall x, and start y from zero
    # for horizontal checks, need use y_start as the overall y, and start x from zero
    # forleft to right diagonal checks, make a loop that subtracts one from x and y starts until one hits zero, and use those two no x and y as the start


    #all vertical checks
    for column in range(len(board)):
        consec = 0
        for sq in range(len(board[column])):
            #if current col is requested and consecutive col is less than length
            if board[sq][column] == col:
                consec +=1

            #if current col is not requested
            elif board[sq][column] != col:
                consec = 0


            if consec == length:
                #if consecutive == length and next pieces == col
                if sq+1 == len(board) or board[sq+1][column] != col:

                    #if consecutive == length requested and open bounds
                    if is_bounded(board, sq, column, length, 1, 0) == "OPEN":
                        open_seq_count +=1
                        consec = 0

                    #if consective == length and semiopen bounds
                    if is_bounded(board, sq, column, length, 1, 0) == "SEMIOPEN":
                        semi_open_seq_count +=1
                        consec = 0

    #all horizontal checks
    for row in range(len(board)):
        consec = 0
        for sq in range(len(board[row])):

            #if current col is requested and consecutive col is less than length
            if board[row][sq] == col:
                consec +=1

            #if current col is not requested
            elif board[row][sq] != col:
                consec = 0


            if consec == length:
                #if consecutive == length and next pieces == col
                #if (sq+1 < len(board) and board[row][sq+1] != col) or :
                if (sq+1 == len(board) or board[row][sq+1] != col): #does this automatically make sure that the sq+1 is possible???#IMPLEMENT THIS FIX EVERYWHERE # the reason why this was wrong is because when there is edge two consec, and i am on secon dlast, the bottom code won't even run to check boundedness'


                    #if consecutive == length requested and open bounds
                    if is_bounded(board, row, sq, length, 0, 1) == "OPEN":
                        open_seq_count +=1
                        consec = 0

                    #if consective == length and semiopen bounds
                    if is_bounded(board, row, sq, length, 0, 1) == "SEMIOPEN":
                        semi_open_seq_count +=1
                        consec = 0


    #all left to right diagonal checks
    #iterate through column from y_start to end of column, x_start always zero
    #checking lower triangular matrix, including central diagonal
    for y_start in range(len(board)):
        consec = 0
        for sq in range(y_start, len(board)):

            #if current col is requested and consecutive col is less than length
            #if board[sq][sq-y_start] == col and consec < length: #THE ISSUE WITH THIS IS IF ITS OVER U DONT COUNT CONSEC, AND ITS JUST GONNA NOT CHECK THAT U WENT OVER
            if board[sq][sq-y_start] == col:
                consec +=1

            #if current col is not requested
            elif board[sq][sq-y_start] != col:
                consec = 0

            if consec == length :
                #if consecutive == length and next pieces == col
                if sq+1 == len(board) or sq-y_start +1 == len(board) or board[sq+1][sq-y_start+1] != col:

                    #if consecutive == length requested and open bounds
                    if is_bounded(board, sq, sq-y_start, length, 1, 1) == "OPEN":
                        open_seq_count +=1
                        consec = 0

                    #if consective == length and semiopen bounds
                    if is_bounded(board, sq, sq-y_start, length, 1, 1) == "SEMIOPEN":
                        semi_open_seq_count +=1
                        consec = 0

    #THE ISSUE IS , IF YOU HAVE 4 IN A ROW AN DU ARE REQUESTING 2 IN A ROW, AFTER U GET TO THE THIRD ONE, CONSEC IS 0 AND THEN IT COUNTS 2 MORE AND THINKS IT IS CONSEC... BUT THAT IS INCORRECT


    #iterate through column from x_start to end of column, y_start always zero
    #check upper triangular matrix, not including central diagonal
    for x_start in range(1, len(board)):
        consec = 0
        for sq in range(x_start, len(board)):

            #if current col is requested and consecutive col is less than length
            if board[sq-x_start][sq] == col:
                consec +=1

            #if current col is not requested
            elif board[sq-x_start][sq] != col:
                consec = 0


            if consec == length:
                #if consecutive == length and next pieces == col
                if (sq+1 == len(board) or sq-x_start +1 == len(board)) or board[sq-x_start+1][sq+1] != col:


                    #if consecutive == length requested and open bounds
                    if is_bounded(board, sq-x_start, sq, length, 1, 1) == "OPEN":
                        open_seq_count +=1
                        consec = 0

                    #if consective == length and semiopen bounds
                    if is_bounded(board, sq-x_start, sq, length, 1, 1) == "SEMIOPEN":
                        semi_open_seq_count +=1
                        consec = 0


    #all right to left diagonal checks
    #iterate through column from y_start to end of column, x_start always zero
    #checking lower triangular matrix, excluding central diagonal
    for y_start in range(1, len(board)):
        consec = 0
        for sq in range(len(board)-1, y_start-1, -1):

            #if current col is requested and consecutive col is less than length
            if board[y_start-sq+len(board)-1][sq] == col:
                consec +=1

            #if current col is not requested
            elif board[y_start-sq+len(board)-1][sq] != col:
                consec = 0


            if consec == length:
                #if consecutive == length and next pieces == col
                if (y_start-sq+len(board) == len(board) or sq-1 < 0) or  board[y_start-sq+len(board)][sq-1] != col:#CHECK THE +1 INDEXING AND STUFF AGIANANIAN

                    #if consecutive == length requested and open bounds
                    if is_bounded(board, y_start-sq+len(board)-1, sq, length, 1, -1) == "OPEN":
                        open_seq_count +=1
                        consec = 0

                    #if consective == length and semiopen bounds
                    if is_bounded(board, y_start-sq+len(board)-1, sq, length, 1, -1) == "SEMIOPEN":
                        semi_open_seq_count +=1
                        consec = 0



    #iterate through column from x_start to end of column, y_start always zero
    #check upper triangular matrix, including central diagonal
    for x_start in range(len(board)-1, -1, -1):
        consec = 0
        for sq in range(0, x_start+1):

            #if current col is requested and consecutive col is less than length
            if board[sq][x_start-sq] == col:
                consec +=1

            #if current col is not requested
            elif board[sq][x_start-sq] != col:
                consec = 0


            if consec == length:
                #if consecutive == length and next pieces == col
                #failing with and first, passing with or first
                if (sq+1 == len(board) or x_start-sq-1  < 0) or board[sq+1][x_start-sq-1] != col:


                        #if consecutive == length requested and open bounds
                        if is_bounded(board, sq, x_start-sq, length, 1, -1) == "OPEN":
                            open_seq_count +=1
                            consec = 0

                        #if consective == length and semiopen bounds
                        if is_bounded(board, sq, x_start-sq, length, 1, -1) == "SEMIOPEN":
                            semi_open_seq_count +=1
                            consec = 0

    return open_seq_count, semi_open_seq_count

'''
This function uses the function score() (provided) to find the optimal move for black. It finds the location (y,x), such that (y,x) is empty and putting a black stone on (y,x) maximizes the score of the board as calculated by score(). The function returns a tuple (y, x) such that putting a black stone in coordinates (y, x) maximizes the potential score (if there are several such tuples, you can return any one of them). After the function returns, the contents of board must remain the same.
'''
def search_max(board):
    move_y = 0
    move_x = 0

    #test all possible moves
    high_score = -100000000
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == " ":
                put_seq_on_board(board, row, column, 1, 1, 1, "b")
                print_board(board)

                if score(board) == 100000:
                    move_y, move_x = row, column
                    put_seq_on_board(board, row, column, 1, 1, 1, " ")
                    return move_y, move_x

                #should this section be in the previous if satement or ?
                else:
                    if score(board) > high_score:
                        high_score = score(board)
                        move_y, move_x = row, column #for one of aayush's tests, i got 6,7 instead of 5,6 but 6,7 comes after ?

                put_seq_on_board(board, row, column, 1, 1, 1, " ")

    return move_y, move_x


def score(board):
    MAX_SCORE = 100000

    open_b = {}
    semi_open_b = {}

    open_w = {}
    semi_open_w = {}


    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)


    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE


    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE

    return (-10000 * (open_w[4] + semi_open_w[4])+
            500  * open_b[4]                     +
            50   * semi_open_b[4]                +
            -100  * open_w[3]                    +
            -30   * semi_open_w[3]               +
            50   * open_b[3]                     +
            10   * semi_open_b[3]                +
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])


'''
This function determines the current status of the game, and returns one of
["White won", "Black won", "Draw", "Continue playing"], depending on the current status on the board. The only situation where "Draw" is returned is when board is full.
'''
def is_win(board):

    consec_hor_b = 0
    consec_hor_w = 0

    #go through each row (inner loop columns) to find horizontal wins
    for row in range(len(board)):
        for column in range(len(board)-1): #minus one length so we can check one preceding without out of range error
            if board[row][column] == "b" and board[row][column] == board[row][column+1]: # does this not go out of range??? i do not think so since you go the len-1
                consec_hor_b += 1

            elif board[row][column] !="b":
                consec_hor_b = 0

            if board[row][column] == "w" and board[row][column] == board[row][column+1]:
                consec_hor_w += 1
            elif board[row][column] !="w":
                consec_hor_w = 0


            if consec_hor_b == 4 and board[row][column+1]!="b":
                return "Black won"
            elif consec_hor_w == 4 and board[row][column+1]!="w":
                return "White won"

        #trying to make it so 6 in a row is not win
            # if consec_hor_b == 4 and column +2 < len(board)-1 and board[row][column+2] !='b':
            #     return "Black won"
            # elif consec_hor_w == 4:
            #     return "White won"

    #go through each column (inner loop rows) to find vertical wins
    consec_ver_b = 0
    consec_ver_w = 0

    for column in range(len(board)):
        for row in range(len(board)-1):
            if board[row][column] == "b" and board[row][column] == board[row+1][column]:
                consec_ver_b += 1
            elif board[row][column] !="b":
                consec_ver_b = 0

            if board[row][column] == "w" and board[row][column] == board[row+1][column]:
                consec_ver_w += 1
            elif board[row][column] !="w":
                consec_ver_w = 0

            if consec_ver_b == 4 and board[row+1][column]!= "b":
                return "Black won"
            elif consec_ver_w == 4 and board[row+1][column]!= "w":
                return "White won"


    consec_diag_b = 0
    consec_diag_w = 0

    #left to right diagonal wins
    for y_start in range(len(board)):
        for sq in range(y_start, len(board)-1):

            #if current is black and same as next
            if board[sq][sq-y_start] == "b" and board[sq][sq-y_start] == board[sq+1][sq-y_start+1]:
                consec_diag_b += 1

            elif board[sq][sq-y_start] != "b":
                consec_diag_b = 0

            if board[sq][sq-y_start] == "w" and board[sq][sq-y_start] == board[sq+1][sq-y_start+1]:
                consec_diag_w += 1

            elif board[sq][sq-y_start] != "w":
                consec_diag_w = 0


            if consec_diag_b == 4 and board[sq+1][sq-y_start+1]!= "b":
                return "Black won"
            elif consec_diag_w == 4 and board[sq+1][sq-y_start+1]!= "w":
                return "White won"

    consec_diag_b = 0
    consec_diag_w = 0

    for x_start in range(1, len(board)):
        for sq in range(x_start, len(board)-1):

            if board[sq-x_start][sq] == "b" and board[sq-x_start][sq] == board[sq-x_start+1][sq+1]:
                consec_diag_b +=1

            elif board[sq-x_start][sq] != "b":
                consec_diag_b =0

            if board[sq-x_start][sq] == "w" and board[sq-x_start][sq] == board[sq-x_start+1][sq+1]:
                consec_diag_w +=1

            elif board[sq-x_start][sq] != "w":
                consec_diag_w =0


            if consec_diag_b == 4 and board[sq-x_start+1][sq+1]!="b":
                return "Black won"
            elif consec_diag_w == 4 and board[sq-x_start+1][sq+1]!="w":
                return "White won"

    consec_diag_b = 0
    consec_diag_w = 0


    #right to left diagonal wins

    for y_start in range(1, len(board)):
        for sq in range(len(board)-1, y_start, -1):

            if board[y_start-sq+len(board)-1][sq] == "b" and board[y_start-sq+len(board)-1][sq] == board[y_start-sq+len(board)][sq-1]:
                consec_diag_b +=1

            elif board[y_start-sq+len(board)-1][sq] != "b":
                consec_diag_b = 0

            if board[y_start-sq+len(board)-1][sq] == "w" and board[y_start-sq+len(board)-1][sq] == board[y_start-sq+len(board)][sq-1]:
                consec_diag_w +=1

            elif board[y_start-sq+len(board)-1][sq] != "w":
                consec_diag_w = 0

            if consec_diag_b == 4 and board[y_start-sq+len(board)][sq-1]!="b":
                return "Black won"
            elif consec_diag_w == 4 and board[y_start-sq+len(board)][sq-1]!="w":
                return "White won"


    consec_diag_b = 0
    consec_diag_w = 0

    for x_start in range(len(board)-1, -1, -1):
        for sq in range(0, x_start):

            if board[sq][x_start-sq] =="b" and board[sq][x_start-sq] == board[sq+1][x_start-sq-1]:
                consec_diag_b +=1
            elif board[sq][x_start-sq] !="b":
                consec_diag_b = 0

            if board[sq][x_start-sq] =="w" and board[sq][x_start-sq] == board[sq+1][x_start-sq-1]:
                consec_diag_w +=1
            elif board[sq][x_start-sq] !="w":
                consec_diag_w = 0

            if consec_diag_b == 4 and board[sq+1][x_start-sq-1] !="b":
                return "Black won"
            elif consec_diag_w == 4 and board[sq+1][x_start-sq-1] !="w":
                return "White won"


    #draw scenario
    total_fill = []

    for row in range(len(board)):
        for entry in board[row]:
            if entry != " ":
                total_fill.append(entry)
    if len(total_fill) == len(board)**2:
        return "Draw"

    return "Continue playing"

def print_board(board):

    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"

    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1])

        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"

    print(s)

def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board

def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))

def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])

    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)

        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res

        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res

def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col
        y += d_y
        x += d_x

def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)

    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


def test_detect_row():
    board = make_empty_board(8)

    #test 1
    # x = 4; y = 4; d_x = 1; d_y = 0; length = 4
    # put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    # print_board(board)
    # if detect_row(board, "w",4, 7,4,0,1) == (0,1):
    #     print("TEST CASE for detect_row PASSED")
    # else:
    #     print("TEST CASE for detect_row FAILED")


    #test 2
    # x = 1; y = 3; d_x = 1; d_y = 1; length = 4
    # put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    # print_board(board)
    # if detect_row(board, "w", 7, 5,4,1,1) == (1,0):
    #     print("TEST CASE for detect_row PASSED")
    # else:
    #     print("TEST CASE for detect_row FAILED")


    #test 3 - if start is on the end of valid consec sequence
    # x = 3; y = 1; d_x = -1; d_y = 1; length = 3
    # put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    # print_board(board)
    # if detect_row(board, "w", 3, 1,3,1,-1) == (1,0):
    #     print("TEST CASE for detect_row PASSED")
    # else:
    #     print("TEST CASE for detect_row FAILED")

    #test 4
#     x = 5; y = 4; d_x = -1; d_y = 1; length = 4
#     put_seq_on_board(board, y, x, d_y, d_x, length, "w")
#     print_board(board)
#     if detect_row(board, "w", 5, 4,4,1,-1) == (0,1):
#         print("TEST CASE for detect_row PASSED")
#     else:
#         print("TEST CASE for detect_row FAILED")


    #test 5
        #'w', 0, 1, 1, 1, 1], l, (1, 0)


    #test 6



def test_detect_rows():
    board = make_empty_board(8)
#     x = 1; y = 1; d_x = 1; d_y = 1; length = 3; col = 'w'
#     put_seq_on_board(board, y, x, d_y, d_x, length, "w")
#     x = 1; y = 5; d_x = 1; d_y = 1; length = 3
#     put_seq_on_board(board, y, x, d_y, d_x, length, "w")
#     x = 2; y = 5; d_x = 0; d_y = 1; length = 3
#     put_seq_on_board(board, y, x, d_y, d_x, length, "w")
#     x = 2; y = 0; d_x = 1; d_y = 0; length2 = 5
#     put_seq_on_board(board, y, x, d_y, d_x, length2, "w")
#     x = 2; y = 0; d_x = -1; d_y = 1; length = 3
#     put_seq_on_board(board, y, x, d_y, d_x, length, "w")
#     x = 6; y = 2; d_x = -1; d_y = 1; length = 3
#     put_seq_on_board(board, y, x, d_y, d_x, length, "w")
#     x = 4; y = 0; d_x = -1; d_y = 1; length = 3
#     put_seq_on_board(board, y, x, d_y, d_x, length, "w")
#     print_board(board)
#     if detect_rows(board, col,length=3) == (1,3):
#         print("TEST CASE for detect_rows PASSED")
#     else:
#         print("TEST CASE for detect_rows FAILED")
#     put_seq_on_board(board, 0, 1, 1, 1, 1, "w")
#     put_seq_on_board(board, 1, 0, 1, 1, 1, "w")
#     put_seq_on_board(board, 1, 1, 1, 1, 4, "b")
#     put_seq_on_board(board, 1, 2, 1, -1, 2, "b")
#     print_board(board)
#
#
#     if detect_rows(board, "b", 2) == (3,2):
#         print("TEST CASE for detect_rows PASSED")
#     else:
#         print("TEST CASE for detect_rows FAILED")

    put_seq_on_board(board, 0, 1, 1, -1, 2, "b")
    put_seq_on_board(board, 0, 2, 1, 1, 1, "w")
    put_seq_on_board(board, 0, 5, 1, 0, 2, "w")
    put_seq_on_board(board, 1, 0, 1, 1, 1, "b")
    put_seq_on_board(board, 1, 4, 1, 1, 1, "b")
    put_seq_on_board(board, 3, 0, 0, 1, 2, "w")
    put_seq_on_board(board, 1, 2, 1, -1, 2, "b")
    put_seq_on_board(board, 3, 4, 1, 1, 2, "w")
    put_seq_on_board(board, 3, 6, 1, 1, 1, "w")
    print_board(board)


    if detect_rows(board, "w", 2) == (2,2):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")





def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)

    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0

    y = 3; x = 5; d_x = -1; d_y = 1; length = 2

    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)

    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #

    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);

    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #
    #
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0 #FAILED, GOT 1 INSTEAD OF 0 fixed, because forgot +! nvm it should be -1 for the next square check
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1 #FAILED, 0 INSTEAD OF 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1 #FAILED, 0 INSTEAD OF 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0


def test_is_win():
    board = make_empty_board(8)
    #case 1 black wins
    # put_seq_on_board(board, 0, 1, 0, 1, 2, "b")
    # put_seq_on_board(board, 1, 1, 0, 1, 3, "b")
    # put_seq_on_board(board, 0, 4, 1, 1, 2, "b")
    # put_seq_on_board(board, 0, 6, 1, 0, 2, "b")
    # put_seq_on_board(board, 4, 4, 1, 0, 1, "b")
    # put_seq_on_board(board, 4, 2, 1, 1, 4, "w")



    #case 2 6 in a row
    #put_seq_on_board(board, 0, 0, 1, 1, 6, "b")#return None
    #put_seq_on_board(board, 0, 0, 1, -1, 5, "w") #IS THIS A VALID BOARD INPUT
    #put_seq_on_board(board, 0, 7, 1, -1, 6, "w")
    #put_seq_on_board(board, 0, 0, 1, 1, 6, "w")#currently not working


    put_seq_on_board(board, 0, 1, 1, 0, 5, "b")
    print_board(board)
    print(is_win(board))

def eval_test_case(fcn, fcn_in, l, correct_ans, show_board=1):
    # if show_board is: 0 -> never show board, 1 -> show board if wrong answer
    # Create an empty 8x8 board
    board = make_empty_board(8)
    fcn = fcn.lower()

    # Place all the sequences on the board
    for seq in l:
        put_seq_on_board(board, *seq)

    # Define a dictionary to map function names to their corresponding functions and expected argument lengths
    function_map = {"is_bounded": (is_bounded, 5), "detect_row": (detect_row, 6), "detect_rows": (detect_rows, 2),
                    "search_max": (search_max, 0), "is_win": (is_win, 0)}

    # Check if the function name is valid
    if fcn in function_map:
        func, expected_args = function_map[fcn]
        if len(fcn_in) != expected_args:
            print("invalid no. of arguments")
            return
        else:
            your_ans = func(board, *fcn_in)
    else:
        print("invalid function")
        return

    # ANSI escape codes for colors and formatting
    class Colors:
        OKGREEN = '\033[92m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

    # Check if the result matches the expected answer
    if your_ans == correct_ans:
        if show_board == 2:  # Always show the board if show_board is 2
            print_board(board)
            print(f"l = {l}")
            print(f"fcn_input_args: {fcn_in}")
            print(f"correct ans: {correct_ans}")
        print(f"{Colors.OKGREEN}Test Case for {fcn} PASSED{Colors.ENDC}")
    else:
        if show_board == 1 or show_board == 2:  # Show the board if the test fails or if show_board is 2
            print("----V----V----V----V----V----V----V----V----V----V----")
            print_board(board)
            print(f"l = {l}")
            print(f"fcn_input_args: {fcn_in}")

        print(
            f"{Colors.FAIL}{Colors.BOLD}{Colors.UNDERLINE}Test Case for {fcn} FAILED. You returned \"{your_ans}\" instead of \"{correct_ans}\".{Colors.ENDC}")
        if show_board == 1 or show_board == 2:
            print("----^----^----^----^----^----^----^----^----^----^----")

def testing():
    print("----------IS_BOUNDED TESTS----------")
    eval_test_case("is_bounded", [3, 5, 3, 1, 0], [[1, 5, 1, 0, 3, "w"]], "OPEN")
    eval_test_case("is_bounded", [6, 1, 3, 1, 0], [[4, 1, 1, 0, 3, "w"]], "OPEN")
    l = [[3, 3, 0, 1, 3, "b"], [3, 6, 0, 1, 1, "w"]]
    eval_test_case("is_bounded", [3, 5, 3, 0, 1], l, "SEMIOPEN")
    l = [[3, 0, 0, 1, 4, "w"], [3, 4, 0, 1, 1, "b"]]
    eval_test_case("is_bounded", [3, 3, 4, 0, 1], l, "CLOSED")
    eval_test_case("is_bounded", [7, 2, 3, 1, 1], [[5, 0, 1, 1, 3, "b"]], "CLOSED")
    eval_test_case("is_bounded", [3, 3, 4, 1, -1], [[0, 6, 1, -1, 4, "w"]], "SEMIOPEN")
    l = [[4, 2, 0, 1, 3, 'b']]  # Sequence starting at (4,2) moving right
    eval_test_case("is_bounded", [4, 4, 3, 0, 1], l, "OPEN")
    l = [[0, 5, 1, 0, 4, 'w']]  # Sequence starting at (0,5) moving down
    eval_test_case("is_bounded", [3, 5, 4, 1, 0], l, "SEMIOPEN")
    l = [[2, 2, 1, 1, 5, 'b'], [1, 1, 0, 0, 1, 'w'], [7, 7, 0, 0, 1, 'w']]
    eval_test_case("is_bounded", [6, 6, 5, 1, 1], l, "CLOSED")
    l = [[4, 2, 0, 1, 3, 'b'], [4, 5, 0, 0, 1, 'b'], [4, 1, 0, 0, 1, 'b']]
    eval_test_case("is_bounded", [4, 4, 3, 0, 1], l, "CLOSED")
    l = [[7, 0, -1, 1, 3, 'w'], [4, 3, 0, 0, 1, 'b']]
    eval_test_case("is_bounded", [7, 0, 3, 1, -1], l, "CLOSED")
    l = [[1, 7, 1, 0, 2, 'b']]  # Sequence starting at (1,7) moving down
    eval_test_case("is_bounded", [2, 7, 2, 1, 0], l, "OPEN")
    l = [[0, 0, 1, 1, 2, 'w'], [2, 2, 0, 0, 1, 'b']]
    eval_test_case("is_bounded", [1, 1, 2, 1, 1], l, "CLOSED")
    l = [[0, 7, 1, -1, 3, 'b']]
    eval_test_case("is_bounded", [2, 5, 3, 1, -1], l, "SEMIOPEN")
    l = [[7, 3, -1, 0, 3, 'w']]
    eval_test_case("is_bounded", [7, 3, 3, 1, 0], l, "SEMIOPEN")
    l = [[0, 5, 0, 1, 3, 'b']]
    eval_test_case("is_bounded", [0, 7, 3, 0, 1], l, "SEMIOPEN")
    print("----------DETECT_ROW TESTS----------")
    eval_test_case("detect_row", ["w", 0, 5, 3, 1, 0], [[1, 5, 1, 0, 3, "w"]], (1, 0))
    l = [[3, 2, 0, 1, 2, 'b']]
    eval_test_case("detect_row", ['b', 3, 0, 2, 0, 1], l, (1, 0))
    l = [[2, 5, 1, 0, 3, 'w']]
    eval_test_case("detect_row", ['w', 0, 5, 3, 1, 0], l, (1, 0))
    l = [[1, 1, 1, 1, 4, 'b']]
    eval_test_case("detect_row", ['b', 0, 0, 4, 1, 1], l, (1, 0))
    l = [[5, 2, 0, 1, 3, 'w'], [5, 5, 0, 1, 1, 'b']]
    eval_test_case("detect_row", ['w', 5, 0, 3, 0, 1], l, (0, 1))
    l = [[1, 6, 1, 0, 2, 'b'], [0, 6, 0, 1, 1, 'w'], [3, 6, 0, 1, 1, 'w']]
    eval_test_case("detect_row", ['b', 0, 6, 2, 1, 0], l, (0, 0))
    l = [[0, 7, 1, -1, 3, 'w']]
    eval_test_case("detect_row", ['w', 0, 7, 3, 1, -1], l, (0, 1))
    l = [[7, 1, 0, 1, 2, 'b'], [7, 0, 0, 1, 1, 'w']]
    eval_test_case("detect_row", ['b', 7, 0, 2, 0, 1], l, (0, 1))
    l = [[0, 0, 1, 1, 2, 'w'], [2, 2, 0, 1, 1, 'b']]
    eval_test_case("detect_row", ['w', 0, 0, 2, 1, 1], l, (0, 0))
    l = [[4, 4, 0, 1, 3, 'b']]
    eval_test_case("detect_row", ['b', 4, 0, 2, 0, 1], l, (0, 0))
    l = [[4, 1, 1, 1, 3, 'w']]
    eval_test_case("detect_row", ['w', 3, 0, 2, 1, 1], l, (0, 0))
    l = [[1, 0, 0, 1, 5, 'b']]
    eval_test_case("detect_row", ['b', 1, 0, 5, 0, 1], l, (0, 1))
    l = [[0, 5, 1, 0, 2, 'w']]
    eval_test_case("detect_row", ['w', 0, 5, 2, 1, 0], l, (0, 1))
    l = [[3, 3, 0, 1, 3, 'b'], [3, 2, 0, 1, 1, 'w'], [3, 6, 0, 1, 1, 'w']]
    eval_test_case("detect_row", ['b', 3, 0, 3, 0, 1], l, (0, 0))
    l = [[0, 7, 1, -1, 8, 'w']]
    eval_test_case("detect_row", ['w', 0, 1, 1, 1, 1], l, (1, 0))
    l = [[4, 0, 0, 1, 2, 'b'], [4, 2, 0, 1, 1, 'w']]
    eval_test_case("detect_row", ['b', 4, 0, 3, 0, 1], l, (0, 0))
    l = [[0, 2, 1, 0, 2, 'b']]
    eval_test_case("detect_row", ['b', 0, 2, 2, 1, 0], l, (0, 1))
    l = [[2, 5, 1, -1, 3, 'w'], [1, 6, 0, 1, 1, 'b']]
    eval_test_case("detect_row", ['w', 0, 7, 3, 1, -1], l, (0, 1))
    l = [[3, 3, 1, 0, 5, 'b']]
    eval_test_case("detect_row", ['b', 0, 3, 5, 1, 0], l, (0, 1))
    l = [[5, 5, 1, 1, 2, 'b'], [5, 6, 1, 1, 1, 'b']]
    eval_test_case("detect_row", ['b', 0, 0, 2, 1, 1], l, (1, 0))
    eval_test_case("detect_row", ['b', 0, 6, 2, 1, 0], l, (1, 0))
    l = [[0, 6, 1, 1, 2, 'b']]
    eval_test_case("detect_row", ['b', 0, 6, 2, 1, 1], l, (0, 0))
    eval_test_case("detect_row", ['b', 1, 7, 2, 1, 1], l, (0, 0))
    eval_test_case("detect_row", ['b', 0, 7, 2, 1, 1], l, (0, 0))
    print("----------DETECT_ROWS/SEARCH_MAX TESTS----------")
    eval_test_case("detect_rows", ["w", 3], [[1, 5, 1, 0, 3, "w"]], (1, 0))
    l = [[0, 5, 1, 0, 4, "w"], [0, 6, 1, 0, 4, "b"]]
    eval_test_case("search_max", [], l, (4, 6))
    l = [[5, 7, 1, -1, 3, 'b'], [0, 7, 1, -1, 2, 'w']]#this one
    eval_test_case("detect_rows", ["b", 3], l, (0, 0))
    eval_test_case("search_max", [], l, (5, 6))
    l = [[1, 3, 1, 1, 3, 'b'], [2, 6, 1, 0, 3, 'w']]
    eval_test_case("detect_rows", ['b', 7], l, (0, 0))
    eval_test_case("search_max", [], l, (1, 6))
    l = [[5, 6, 0, 1, 1, 'b']]
    eval_test_case("detect_rows", ['w', 3], l, (0, 0))
    eval_test_case("search_max", [], l, (4, 5))
    l = [[5, 1, 1, 1, 2, 'b'], [4, 0, 1, 1, 2, 'w'], [4, 5, 0, 1, 3, 'b'], [5, 5, 1, 0, 2, 'b']]
    eval_test_case("detect_rows", ['b', 2], l, (1, 0))
    eval_test_case("search_max", [], l, (3, 5))
    print("----------IS_WIN TESTS----------")
    l = [[0, 0, 1, 1, 5, 'b']]
    eval_test_case("is_win", [], l, "Black won")
    l = [[0, 0, 1, 1, 6, 'b']]
    eval_test_case("is_win", [], l, "Continue playing")
    l = [[0, 0, 1, 1, 7, 'b']]
    eval_test_case("is_win", [], l, "Continue playing")
    l = [[0, 0, 1, 1, 8, 'b']]
    eval_test_case("is_win", [], l, "Continue playing")


if __name__ == '__main__':
    #test_is_empty()
    #test_is_bounded()
    #test_detect_row() #something went wrong with indexing with aayush's test code
    #test_detect_rows()
    #test_search_max() # this needs to be checked
    #some_tests()
    #play_gomoku(8)
    #test_is_win()
    testing()