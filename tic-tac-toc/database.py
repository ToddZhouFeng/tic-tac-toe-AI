import TTTFrame as t3f
import pickle
import numpy as np
import copy

def match(board, tup):
    """判断board是否在tup中"""
    for i in tup:
        #print(board, '\n', i)
        if (board==i).all():
            return True
    return False


while(True):
    try:
        file=open("database.pkl", "rb")#读取已有的数据
        database=pickle.load(file)
        file_bak=open("database.pkl.bak", "wb")#对原数据文件备份
        pickle.dump(database, file_bak)
        file_bak.close()
        file.close()
    except:
        print("读取不了诶~")
        database=[]
    file=open("database.pkl", "wb")#将原数据文件覆盖掉
    board_data=[]
    print("已有",len(database),"组数据")
    while(True):
        for i in database:
            board_data.append(i[0])
        temp=[]
        board=t3f.initBoard()
        t3f.visualize(board)
        player=int(input("先手为玩家1还是玩家2："))
        if player!=1 and player!=2:
            player=2
        while not t3f.judgeAll(board) and  not t3f.isEmpty(board):
            move=int(input("玩家"+str(player)+"下棋（0~8）"))
            while not t3f.judgeMove(board, move):
                move=input("所走处无效，请重新下")

            if player==1:
                data=[copy.deepcopy(board), copy.deepcopy(move)]
                mirror=t3f.mirror(board)
                isin=False
                #对棋盘进行旋转和镜像
                for i in range(4):
                    if match(t3f.rotate(board, i+1), board_data):
                        isin=True
                        break
                    if match(t3f.rotate(mirror, i+1), board_data):
                        isin=True
                        break
                if not isin:
                    print("已获取有效数据")
                    temp.append(data)

            t3f.makeMove(board, move, player)
            t3f.visualize(board)
            if player==1:
                player+=1
            else:
                player-=1

        print("玩家", t3f.judgeAll(board), "获胜")
        if t3f.judgeAll(board)==1 or t3f.judgeAll(board)==0:#
            for i in temp:
                database.append(i)
            print("该局数据有效，贡献了",len(temp),"个数据")
            break
        else:
            print("该局数据无效")
    print("已有",len(database),"组数据")
    pickle.dump(database, file)
    file.close()

    i=input("退出？(y/n)")
    if i=='y':
        break
