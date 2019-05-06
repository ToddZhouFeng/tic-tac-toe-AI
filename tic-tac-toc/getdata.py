import TTTFrame as t3f
import pickle
import numpy as np

def match(board, tup):
    for i in tup:
        if (board==tup).all():
            return True
    return False


file=open("database.dat", "ab+")
try:
    database=pickle.load(file)
except:
    database=[]
file.close()
file=open("database.dat", "wb")
board_data=[]

while(True):
    for i in database:
        board_data.append(i[0])
    temp=[]
    board=t3f.initBoard()
    t3f.visualize(board)
    player=1
    while not t3f.judgeAll(board) and  not t3f.isEmpty(board):
        move=int(input("玩家"+str(player)+"下棋（0~8）"))
        while not t3f.judgeMove(board, move):
            move=input("所走处无效，请重新下")
            
        data=[board, move]
        if player==1:
            mirror=t3f.mirror(board)
            isin=False
            for i in range(4):
                if match(t3f.rotate(board, i+1), board_data):
                    isin=True
                    break
                if match(t3f.rotate(mirror, i+1), board_data):
                    isin=True
                    break
            if not isin:
                temp.append(data)

        t3f.makeMove(board, move, player)
        t3f.visualize(board)
        if player==1:
            player+=1
        else:
            player-=1

    print("玩家", t3f.judgeAll(board), "获胜")
    if t3f.judgeAll(board)==1 or t3f.judgeAll(board)==0:
        for i in temp:
            database.append(i)
            print(database)
        break

pickle.dump(database, file)
file.close()
