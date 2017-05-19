︠17841aab-13e4-41d6-a035-7f28fdcb48c0︠

ROWS=3
COLS=3

class TicTacToe:
    def __init__(self):
        self.heuristicTable=[[-1,-10,-100,-1000],[10,0,0,0],[100,0,0,0],[1000,0,0,0]]
        self.winningPositions=[[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]]
        self.numberOfWinningPositions=8
        self.grid=[[1,2,3],[4,5,6],[7,8,9]]
        self.board=[[0,0,0],[0,0,0],[0,0,0]]
        self.inf=99999
        self.neginf=-99999


    def printBoard(self):
        for i in range(0,ROWS):
            for j in range(0,COLS):
                if self.board[i][j]==0:
                    print self.grid[i][j],
                elif self.board[i][j]==1:
                    print 'M',
                elif self.board[i][j]==2:
                    print 'C',
            print ''

    def aMove(self):
        player=1
        move=input("Where would you like to move?")
        for i in range(0,ROWS*COLS):
            if i==move-1 and self.board[(i-(i%ROWS))/ROWS][i%ROWS]==0:
                self.board[(i-(i%ROWS))/ROWS][i%ROWS]=player
        return self.board

    def copyFunc(self,arr):
        newArray=[]
        for i in range(len(arr)):
            t=[]
            for j in range(len(arr[i])):
                t.append(arr[i][j])
            newArray.append(t)
        return newArray

    def ravelCopy(self,arr):
        newArray=[]
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                newArray.append(arr[i][j])
        return newArray

    def homemade2dWhere(self,arr):
        temp1=[]
        temp2=[]
        nr=[temp1,temp2]
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j] == 0: # condition where state == 0
                    temp1.append(i)
                    temp2.append(j)
        return nr

    def utilityOfState(self,state):
        stateCopy=self.ravelCopy(state)
        heuristic=0
        for i in range(0,self.numberOfWinningPositions):
            maxp=0
            minp=0
            for j in range(0,ROWS):
                if stateCopy[self.winningPositions[i][j]] == 2:
                    maxp+=1
                elif stateCopy[self.winningPositions[i][j]] ==1:
                    minp+=1
            heuristic+=self.heuristicTable[maxp][minp]
        return heuristic

    def checkGameOver(self, state):
        stateCopy=self.copyFunc(state)
        value=self.utilityOfState(stateCopy)
        b=self.homemade2dWhere(stateCopy)
        if (b[0] == []):
            return 2
        if value >=900:
            return 1
        return -1

    def minimax(self,state,alpha,beta,maximizing, depth,maxp,minp):
        if depth==0:
            return self.utilityOfState(state),state
        rowsLeft,columnsLeft=self.homemade2dWhere(state)
        returnState=self.copyFunc(state)
        if len(rowsLeft)==0:
            return self.utilityOfState(state),returnState
        if maximizing == True:
            utility=self.neginf
            for i in range(0,len(rowsLeft)):
                nextState=self.copyFunc(state)
                nextState[rowsLeft[i]][columnsLeft[i]]=maxp
                nutility,nstate=self.minimax(nextState,alpha,beta,False,depth-1,maxp,minp)
                if nutility > utility:
                    utility=nutility
                    returnState=self.copyFunc(nextState)
                if utility >alpha:
                    alpha=utility
                if alpha >= beta:
                    break;
            return utility,returnState
        else:
            utility=self.inf
            for i in range(0,len(rowsLeft)):
                nextState=self.copyFunc(state)
                nextState[rowsLeft[i]][columnsLeft[i]]=minp
                nutility,nstate=self.minimax(nextState,alpha,beta,True,depth-1,maxp,minp)
                if nutility < utility:
                    utility=nutility
                    returnState=self.copyFunc(nextState)
                if utility < beta:
                    beta=utility
                if alpha >=beta:
                    break;
            return utility, returnState

    def main(self):
        num=input('Enter player 1st or 2nd using the number 1 or 2: ')
        value=0

        self.printBoard()
        for turn in range(0,9):
            if (turn+num)%2==1:
                self.aMove()
                self.printBoard()
                value=self.checkGameOver(self.board)
                if value==1:
                    print 'You win. Game Over'
                    return
                if value==2:
                    print "It's a draw"
                    return
                print '\n'
            elif (turn+num)%2==0:
                state=self.copyFunc(self.board)
                value,nextState=self.minimax(state,self.neginf,self.inf,True,2,2,1)
                self.board=self.copyFunc(nextState)
                self.printBoard()
                print '\n'
                value=self.checkGameOver(self.board)
                if value==1:
                    print 'PC wins. Game Over'
                    return
                if value==2:
                    print "It's a draw"
                    return
            else:
                print "It's a draw"
                return

t=TicTacToe()
t.main()



