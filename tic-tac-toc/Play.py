#这是一个简单的双人对弈程序
import TTTFrame as t3f

board=t3f.initBoard()
t3f.visualize(board)
player=1
while not t3f.judgeAll(board) and  not t3f.isEmpty(board):
    move=int(input("玩家"+str(player)+"下棋（0~8）"))
    while not t3f.judgeMove(board, move):
        move=int(input("所走处无效，请重新下"))
    t3f.makeMove(board, move, player)
    t3f.visualize(board)
    if player==1:
        player+=1
    else:
        player-=1

print("玩家", t3f.judgeAll(board), "获胜")
   
    
