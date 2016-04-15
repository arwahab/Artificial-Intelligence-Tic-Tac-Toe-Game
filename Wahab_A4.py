__author__ = 'Abdul R. Wahab'
import random
import re
import nt

# CS 4308 - Concepts of Programming Languages
# Assignment #4 - Tic--Tac--Toe
# Start Date: October 20th 2015
# Last Edit: October 29th 2015
# Due Date: October 30th 2015
# Change Log: Fix the AI score keeping [done], Build the main[done], Call methods in the main [done]
# # -- as of 10/29/2015

# class: TheGame -
# initializes and creates a new instance of the game, each time the player chooses to start a new one.
# in charge of creating the board, and keeps count of the score, and validates the moves taken on the board.
# keeps on running the game as long as player wants, and breaks out if player is done.
# pretty much keeps the game going... for now at least that is.
#
def main():
# the main switch for literally everything and anything you can do in this game
# each letter corresponds to what action you would like to do if say, you were
# running this from the command line.
# but if using Eclipse or PyCharm, just hitting the run button will play the
# game
    g = TheGame()
    b = TheBoard()
    p = ThePlayer()
    v = ValidateAllConditions(b)
    ai = AI(b, v, g, p)

    g.initializeGame(v, ai, b, p)

# class: TheGame -
# initializes and creates a new instance of the game, each time the player chooses to start a new one.
# in charge of creating the board, and keeps count of the score, and validates the moves taken on the board.
# keeps on running the game as long as player wants, and breaks out if player is done.
# pretty much keeps the game going... for now at least that is.
#
class TheGame:
    # creates new instance of game, each time user enters 'Y' or 'y' or 'YES' or 'yes'
    # prints the board, and also in charge of score tracking and storing the scores
    # 'resets' the AI, each time a new instance of the game is made
    # resets the board from the previous match
    def createNewGame(player, choice, ai, board, userScoreKeep):
        b = [1, 2, 3, 4, 5, 6, 7, 8, 9] # list implementation, which will be built as a 3x3 matrix
        board.setCurrentBoard(b)
        userScoreKeep.setPlayersChosenMoves([])
        choice.validateBoardReset(board)
        ai.resetAI(board, choice, userScoreKeep)
     # starts the game, once the user decided to play
     # calls the keepPlaying method in 'ThePlayer' class to validate the player's choice to 'keep on playing'
     # retrieves the current state of the board from 'TheBoard' class, and sets it to that specific state
     # also checks to see if player or AI has won, and calls the validatePlayersWin method in 'ValidateAllConditions'
     # class, and displays the result of who won.
    def initializeGame(player, choice, ai, theBoard, currentPlay):
        print("Hello! Let's play some Tic--Tac--Toe! ")
        while True:
            theBoard.printBoard()
            currentPlay.chooseMove(theBoard.getCurrentBoard()) # only runs if the move by either player is valid!!

            if choice.validatePlayersWin(): # checks whether somebody hit the 'jackpot' LOL.
                theBoard.printBoard()
                if not currentPlay.keepPlaying(choice, ai, player, theBoard): # compiles all the scores to display if user says 'no'
                    break
            else:
                ai.storeMovesAI(theBoard)  # stores the AI moves
                if choice.validatePlayersWin(): # validate the user's win
                    player.printBoard()
                    if not player.keepPlaying(choice, ai): # keep playing if nobody has won
                        break
#class: TheBoard -
# in charge of implementing the board as a list, with 9 indices, which essentially takes the form of a 3x3 matrix
# formats the list to print as a 3x3 matrix by calling .format
# prints the board in terms of the players perspective
# gets the current board based on state of game
# returns that board, and the new updated board is played on by the players (User and the AI)
class TheBoard:
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9] # List which will be made into a 3x3 board
    def printBoard(player): # print the board!
        print("_____________")
        print("| {} | {} | {} |".format(player.board[0], player.board[1], player.board[2])) # formatting the board 3x3
        print("_____________")
        print("| {} | {} | {} |".format(player.board[3], player.board[4], player.board[5])) # formatting
        print("_____________")
        print("| {} | {} | {} |".format(player.board[6], player.board[7], player.board[8])) # formatting...
        print("_____________")

    def getCurrentBoard(player): # gets current state of board from player instance
        return player.board
    def setCurrentBoard(player, b): # sets, and,  returns the current state of board to e new instance of board called: b
        player.board = b
# class: ThePlayer -
# creates a list which stores all of the moves the player has made.
# based on user input, either continues the game and creates a newGame or
# chooses moves based on user's input
# re-prompts the user if they enter a number below 1, or any non-integer value.
# gets and stores the players current moves
# also sets the players moves and makes sure that 1 specific moveAI is not visited more than once
class ThePlayer:
    playerMoves = []
    def keepPlaying(player, choice, ai, game, board): # asks user if they want to keep playing or no
        while True:
            userScoreKeepInput = input("Wanna play again? Enter Y or N. ") # keeps running assuming the user still wants to play
            if str(userScoreKeepInput).upper() == "Y":
                game.createNewGame(choice, ai, board, player) # starts a whole new instance with a new board, resetted AI,
                # fresh set of choice and prompting for moves
                return True
            elif str(userScoreKeepInput).upper() == "N":
                return False
            else:
                print("Just say Y or N") # just in case they decide to be... funny.

    def chooseMove(player, board):  # ask them to chose an moveAI, and place it on the board
        while True:
            userScoreKeepInput=input("Pick a spot - ")
            if re.search(r"[1-9]{1}$", userScoreKeepInput): # if choice entered is between 1-9
                userScoreKeepInput = int(userScoreKeepInput) # take it in, and place them on that board

                # if the inout does not match the format required and if they enter 0 or some negative integer
                if not board[userScoreKeepInput-1] == "X" and not board[userScoreKeepInput-1] == "O":

                    # keep it as is
                    board[userScoreKeepInput-1] = "X"
                    # updated players position id appended to the board
                    # call methods playerMoves and tell it where they've moved
                    player.playerMoves.append(userScoreKeepInput)
                    break
                else:
                    print("Can't go there, it's already taken!!") # if they try to make a move that's already been made
            else:
                print("Enter integers 1 through 0 only. ") # nnd if they decide to enter anything other than 1 through 9


    def getPlayersChosenMoves(player): # get their moves by calling playerMoves
        return player.playerMoves

    def setPlayersChosenMoves(player, move): # set the moves, and display on the currently running board
        player.playerMoves = move


# class: AI -
# AI component of the game, which stores all possible winning combinations that the player might enter tin order to win
# keeps a list of all of the players moves as well, and makes counterAttacks, which counteract the players moves in order
# to block them from winning.
class AI:
    board = []
    winningCombinations = []
    counterAttack = None
    playerMoves = []
     # initialize the AI for game
     # get the current Board State, the players moves, and checks
     # all of the possible winning combinations
     # also just to be safe check that all possible winning combinations are perfectly legal and alow the moves to go
    def __init__(player, board, check, game, userScoreKeep):
        player.board = board.getCurrentBoard()
        player.playerMoves = userScoreKeep.getPlayersChosenMoves()
        player.winningCombinations = check.getWinningCombination()


    # validates each move the AI takes, and essentially, counteracts wherever the players move is
    # for every possible winning combinations stored in the list
    # mae some kind of counterattack that 'blocks' the player from moving to
    # the next consecutive block
    # store all the winning combinations, and place the O where it might occur
    def validateMoves(player):
        if not len(player.winningCombinations) == 0 and len(player.playerMoves) > 1:
            for i in player.winningCombinations:
                if player.playerMoves < i:
                    for j in range(0, len(i)):
                        if not i[j] in player.playerMoves:
                            player.counterAttack = i[j]
                    return True
        player.counterAttack = None
        return False
   # place move in desired moveAI
    def moveIndex(player):
        return player.counterAttack
    # store all moves AI can generate, and keep it opposite of the players
    def storeMovesAI(player, b):
        moveChoosen = False
     # choose some random move if haven't chosen one yet
        while not moveChoosen:
            moveAI = random.randint(0, 8)
            # keep going as long as validate method passes
            if player.validateMoves():
                player.board[player.moveIndex() - 1] = "O" # move if valid
                moveChoosen = True # chosen move becomes true and displays on board
            elif not (player.board[moveAI] == "X" or player.board[moveAI] == "O"): # if not then don;t move
               # display some other random position on board
                player.board[moveAI] = "O"
                moveChoosen = True

        b.setCurrentBoard(player.board) # based on what passes from the previous statements, set current board to
        # the current moves
    #RESET AI after allllll moves!!!
    # must be called in the TheGame class...
    def resetAI(player, bd, wc, p): #
        player.board = bd.getCurrentBoard()
        player.playerMoves = p.getPlayersChosenMoves()
        player.winningCombinations = wc.getWinningCombination()

# class: ValidateAllConditions
# so when the AI or the player makes any moves.
# they each store their own moves in their own lists
# but, this class is in large part responsible in making sure that, whatever move is made is
# valid, and shows up on the correct index

class ValidateAllConditions:
    board = [] # store current state of board
    winning = [] # all the winnings

    def __init__(player, board): # initialize the current state of the game
        player.board = board.getCurrentBoard()
  # validate how many steps in each index they have taken
  # update te counter for each move that has been made
    def validateMoveCount(player): #xTally, #oTally):

        xTally = 0;
        oTally = 0;
        for moveAI in player.board:
            if moveAI == "X" :
                xTally = xTally + 1
            else:
                oTally = oTally + 1


        if xTally  > 2 or oTally > 3:
            return True
        else:
            return False
     # alll the possible ways a player can win given the combinations down below
    # including diagonals right from bottom, left from bottom etc.
    def validateBoard(player, consecMove):
        if player.board[0] == consecMove and player.board[1] == consecMove and player.board[2] == consecMove:
            return True
        elif player.board[3] == consecMove and player.board[4] == consecMove and player.board[5] == consecMove:
            return True
        elif player.board[6] == consecMove and player.board[7] == consecMove and player.board[8] == consecMove:
            return True
        elif player.board[0] == consecMove and player.board[3] == consecMove and player.board[6] == consecMove:
            return True
        elif player.board[1] == consecMove and player.board[4] == consecMove and player.board[7] == consecMove:
            return True
        elif player.board[2] == consecMove and player.board[5] == consecMove and player.board[8] == consecMove:
            return True
        elif player.board[0] == consecMove and player.board[4] == consecMove and player.board[8] == consecMove:
            return True
        elif player.board[6] == consecMove and player.board[4] == consecMove and player.board[2] == consecMove:
            return True
        else:
            return False

    def validateOMoves(player):   # move AI to certain index since move is valid
        return player.validateBoard("O")

    def validateXMoves(player):    # move player to certain index since move is valid
        return player.validateBoard("X")

      # moves that need to constitute winning combos and returned back into the list
    def getMove(player, consecMove):
        if player.board[0] == consecMove and player.board[1] == consecMove and player.board[2] == consecMove:
                 return [1, 2, 3]
        elif player.board[3] == consecMove and player.board[4] == consecMove and player.board[5] == consecMove:
                 return [4, 5, 6]
        elif player.board[6] == consecMove and player.board[7] == consecMove and player.board[8] == consecMove:
                 return [7, 8, 9]
        elif player.board[0] == consecMove and player.board[3] == consecMove and player.board[6] == consecMove:
                 return [1, 4, 7]
        elif player.board[1] == consecMove and player.board[4] == consecMove and player.board[7] == consecMove:
                 return [2, 5, 8]
        elif player.board[2] == consecMove and player.board[5] == consecMove and player.board[8] == consecMove:
                 return [3, 6, 9]
        elif player.board[0] == consecMove and player.board[4] == consecMove and player.board[8] == consecMove:
                 return [1, 5, 9]
        elif player.board[6] == consecMove and player.board[4] == consecMove and player.board[2] == consecMove:
                 return [3, 5, 7]

    # def checkForTies(player):
    #     for x in range(0, len(player.board)):
    #         if player.board[x] == (x + 1):
    #             return False
    #     return True


# validates the players win
# gets the move count and the players moves and based on that, decides if player won or not
# with a simple elif it does the opposite assuming the AI wrecked the Player and
# prints "Sorry You Lost"
# and also if they both have tied, calls the checkTies method and validates the Ties through that.
    def validatePlayersWin(player):
        if player.validateMoveCount():
            if player.validateXMoves():
                player.winning.append(player.getMove("X"))

                print("You Won!!")
                return True
            elif player.validateOMoves():

                print("Sorry Player, You Lost!")
                return True
            elif player.checkForTies():
                print("Tied!!! xD")

                return True
            else:
                return False
        else:
            return False
# checks for any ties between the 2 players
# if there is one, game ends and no counters are updated
    def checkForTies(player):
        for x in range(0, len(player.board)):
            if player.board[x] == (x + 1):
                return False
        return True
# gets the winning combination and adds +1 to the counter of whichever player won
    def getWinningCombination(player):
        return player.winning
# resets the new board and make sure its valid
    def validateBoardReset(player, b):
        player.board = b.getCurrentBoard()

if __name__ == "__main__":
    main()

