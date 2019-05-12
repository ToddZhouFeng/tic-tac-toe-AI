# coding: utf-8
#这是一个简单的双人对弈程序
import sys, os
sys.path.append(os.pardir)

from two_layer_net import TwoLayerNet
import pickle
import numpy as np
import TTTFrame as t3f
print("与AI对战！")
print("Ai是玩家1，你是玩家2")

file=open("net.pkl", "rb")
#network=TwoLayerNet(input_size=27, hidden_size=200, output_size=9)
network=pickle.load(file)
while(True):
    board=t3f.initBoard()
    t3f.visualize(board)
    player=int(input("你想先下还是后下：(1为先，2为后)"))

    if player==1:
        player=2
    else:
        player=1

    while not t3f.judgeAll(board) and not t3f.isEmpty(board):
        if player==2:
            move=int(input("玩家"+str(player)+"下棋（0~8）"))
            while not t3f.judgeMove(board, move):
                move=int(input("所走处无效，请重新下"))
        else:
            y=network.predict(board.flatten())
            y=y.tolist()
            #print(y)
            y_copy=y[:]
            y.sort(reverse=True)
            i=0
            move=y_copy.index(y[i])
            while not t3f.judgeMove(board, move):
                i+=1
                move=y_copy.index(y[i])
        t3f.makeMove(board, move, player)
        t3f.visualize(board)
        if player==1:
            player+=1
        else:
            player-=1

    print("玩家", t3f.judgeAll(board), "获胜")
input("按下回车键退出")
