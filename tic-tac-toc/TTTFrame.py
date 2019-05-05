#井字棋的框架
#井字棋的简介：井字棋（Tic-Tac-Toe），是一种在3*3格子上进行的连珠游戏，和五子棋类似，最先连成3子的一方获胜。

import numpy as np

def initBoard():
    """初始化棋盘"""
    return np.array( [ [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]) #好像array内不支持[0 for i int (0, 10)]的形式

def getEmpty(board):
    """返回棋盘中的空格"""
    return board[0]

def getPlayerA(board):
    """返回棋盘中玩家A下的格子"""
    return board[1]

def getPlayerB(board):
    """返回棋盘中玩家B下的格子"""
    return board[2]

def judgePlayer(player):
    """判断输赢，用1表示赢，0未赢"""
    for i in range(0,3):
        if player[i*3]==player[i*3+1] and play[i*3+1]==player[i*3+2]:#横
            return 1
        if player[i]==player[i+3] and play[i+3]==player[i+6]:#竖
            return 1
    if player[2]==player[4] and player[4]==player[6]:#捺
        return 1
    elif player[0]==player[4] and player[4]==play[8]:#撇
        return 1

def judgeAll(board):
    """判断谁赢，用0表示打平，1表示A赢，-1表示B赢"""
    if judgePlayer(getPlayerA[board]):
        return 1
    elif judgePlayer(getPlayerB[board]):
        return -1
    else:
        return 0

def judgeMove(board, move):
    """判断能否走那一个格"""
    if move in getEmpty(board):
        return True
    else:
        return False

def makeMove(board, move, player=1):
    """下子，player参数默认为1"""
    if not judgeMove(move):
        return False
    else:
        if np.sum(board[1])>np.sum(board[2]):
            board[2][move]=1
            board[0][move]=0
            return True
        elif np.sum(board[1])<np.sum(board[2]):
            board[1][move]=1
            board[0][move]=0
            return True
        elif player==1 or play=="A":
            board[1][move]=1
            board[0][move]=0
            return True
        elif player==0 or play=="B":
            board[2][move]=1
            board[0][move]=0
            return True
    return False

def visualize(board):
    """将棋盘可视化输出"""
    vision=[' ' for i in range(0, 10) ]
    for i in range(0, 10):
        if board[1][i]==1:
            vision[i]='x'
    for i in range(0, 10):
        if board[2][i]==1:
            vision[i]='o'
    output="-----------\n"+vision[0]+" | "+vision[1]+" | "+vision[2]+" |\n"
